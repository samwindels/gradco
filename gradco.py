import gradco_c_routines
import numpy as np
from scipy.sparse import csr_array, save_npz, load_npz
import time
from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def time_it() -> Iterator[None]:
    tic: float = time.perf_counter()
    try:
        yield
    finally:
        toc: float = time.perf_counter()
        elapsed = toc - tic
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        print(f"Computation time = {minutes}m {seconds}s")


class Counter(object):

    # (hop, orbit1, orbit2) -> c_index
    __ORBIT_ADJ_2_C_INDEX = {  # single hop
        # standard adjacency matrix, not stored in c arrays
        (1, 0, 0): -1,
        (1, 1, 2): 1,
        (1, 3, 3): 2,
        (1, 4, 5): 4,
        (1, 5, 5): 6,
        (1, 6, 7): 8,
        (1, 8, 8): 9,
        (1, 9, 11): 12,
        (1, 10, 10): 13,
        (1, 10, 11): 14,
        (1, 12, 13): 16,
        (1, 13, 13): 17,
        (1, 14, 14): 18,
        # double hop
        (2, 1, 1): 0,
        (2, 4, 5): 5,
        (2, 6, 6): 7,
        (2, 8, 8): 10,
        (2, 9, 10): 11,
        (2, 12, 12): 15,
        # triple hop
        (3, 4, 4): 3}

    def __init__(self, A):

        # assert A is a valid adjacency matrix
        self.__assert_has_entries(A)
        self.__assert_equal_dims(A)

        # apply degree ordering
        self.__A, self.__order, self.__reverse_order = self.__apply_degree_ordering(
            A)

        # book keeping
        self.__n = A.shape[0]  # number of nodes
        self.orbit_adjacencies = None  # where c counts will be stored

    # SANITY CHECKS ON ADJACENCY MATRIX

    def __assert_unweighted(self, A):
        if not np.all(np.logical_or(A == 0, A == 1)):
            raise ValueError('Adjacency matrix is not unweighted')

    def __assert_has_entries(self, A):
        if A.sum().sum() == 0:
            raise ValueError('Adjacency matrix is empty')

    def __assert_equal_dims(self, A):
        if A.shape[0] != A.shape[1]:
            raise ValueError('Adjacency matrix is not square')

    def __assert_symmetric(self, A):
        if not np.array_equal(A, A.T):
            raise ValueError('Adjacency matrix is not symmetric')

    # DEGREE ORDERING
    def __apply_degree_ordering(self, A):
        # scipy returns numpy matrix instead of array
        rowsum = np.asarray(A.sum(axis=1)).squeeze()
        order = np.argsort(rowsum, axis=0)
        reverse_order = np.argsort(order)
        A = A[order, :]
        A = A[:, order]
        return A, order, reverse_order

    def __apply_reverse_ordering(self, A):
        A = A[self.__reverse_order, :]
        A = A[:, self.__reverse_order]
        return A

    # CALL C ROUTINES
    def count(self):
        # A = self.__A.toarray()
        rows, cols = self.__A.nonzero()
        if len(rows) > 0:
            self.orbit_adjacencies = list(
                gradco_c_routines.gradco_c_count(rows, cols, self.__n))
            self.__compute_A4_4()

    def __to_float_array(self, A):
        return A.astype(np.float32, order='C')

    def __compute_A4_4(self):

        print('Computing A4_4')
        with time_it():
            # float matmul is more optimised in BLAS than int matmul
            A4_4 = self.__to_float_array(
                self.get_orbit_adjacency(2, 1, 1).toarray())
            A4_4 = A4_4 @ self.__to_float_array(
                self.get_orbit_adjacency(1, 0, 0).toarray())
            A4_4 -= self.__to_float_array(
                self.get_orbit_adjacency(1, 8, 8).toarray())
            A4_4 -= self.__to_float_array(
                self.get_orbit_adjacency(1, 12, 13).toarray())
            A4_4 -= self.__to_float_array(
                self.get_orbit_adjacency(2, 9, 10).toarray())
            A4_4 -= self.__to_float_array(
                self.get_orbit_adjacency(1, 1, 2).toarray())
            A4_4 = A4_4[self.__order, :]
            A4_4 = A4_4[:, self.__order]
            A4_4 = A4_4.astype(np.int32, order='C')

            c_index = self.__ORBIT_ADJ_2_C_INDEX[3, 4, 4]
            rows, cols = A4_4.nonzero()
            vals = A4_4[rows, cols]
            if len(rows) > 0:
                self.orbit_adjacencies[c_index] = np.vstack((rows, cols, vals))

    # def __compute_A4_4(self):
    #         print('HOOT')
    #         with time_it():
    #             A = self.__apply_reverse_ordering(self.__A)
    #             try:
    #                 A3 = np.linalg.matrix_power(A, 3)
    #             except:
    #                 A3 = np.linalg.matrix_power(A.toarray(), 3)
    #         with time_it():
    #             A3 -=  self.get_orbit_adjacency(1, 0, 0)
    #             A3 -=  self.get_orbit_adjacency(1, 1, 2).toarray()
    #             A3 -=  self.get_orbit_adjacency(1, 2, 1).toarray()
    #             A3 -=  2 * self.get_orbit_adjacency(1, 3, 3).toarray()
    #             A3 -= self.get_orbit_adjacency(1, 8, 8).toarray()
    #             A3 -= self.get_orbit_adjacency(2, 9, 10).toarray()
    #             A3 -= self.get_orbit_adjacency(2, 10, 9).toarray()
    #             A3 -= self.get_orbit_adjacency(1, 12, 13).toarray()
    #             A3 -= self.get_orbit_adjacency(1, 13, 12).toarray()
    #             A3 -= 2 * self.get_orbit_adjacency(2, 12, 12).toarray()
    #             A3 -= 2 * self.get_orbit_adjacency(1, 14, 14).toarray()
    #             np.fill_diagonal(A3, 0)
    #             A3 = A3[self.__order, :]
    #             A3 = A3[:, self.__order]
    #             c_index = self.__ORBIT_ADJ_2_C_INDEX[3, 4, 4]
    #             rows, cols = A3.nonzero()
    #             vals = A3[rows, cols]
    #             if len(rows) > 0:
    #                 print('hiet')
    #                 self.orbit_adjacencies[c_index] = np.vstack((rows, cols, vals))

    # GRAPHLET ADJACENCIES

    def get_graphlet_adjacency(self, graphlet):
        """ Return the adjacency matrix for a given graphlet.

        Reference:
            Windels, Sam FL, Noël Malod-Dognin, and Nataša Pržulj. "Graphlet
            Laplacians for topology-function and topology-disease
            relationships." Bioinformatics 35.24 (2019): 5226-5234.
        """

        match graphlet:
            case 0:
                return self.__get_graphlet_adjacency_0()
            case 1:
                return self.__get_graphlet_adjacency_1()
            case 2:
                return self.__get_graphlet_adjacency_2()
            case 3:
                return self.__get_graphlet_adjacency_3()
            case 4:
                return self.__get_graphlet_adjacency_4()
            case 5:
                return self.__get_graphlet_adjacency_5()
            case 6:
                return self.__get_graphlet_adjacency_6()
            case 7:
                return self.__get_graphlet_adjacency_7()
            case 8:
                return self.__get_graphlet_adjacency_8()
            case _:
                raise ValueError('Graphlet index must be between 0 and 8')

    def generate_graphlet_adjacencies(self):

        yield self.__get_graphlet_adjacency_0()
        yield self.__get_graphlet_adjacency_1()
        yield self.__get_graphlet_adjacency_2()
        yield self.__get_graphlet_adjacency_3()
        yield self.__get_graphlet_adjacency_4()
        yield self.__get_graphlet_adjacency_5()
        yield self.__get_graphlet_adjacency_6()
        yield self.__get_graphlet_adjacency_7()
        yield self.__get_graphlet_adjacency_8()

    def __get_graphlet_adjacency_0(self):
        A = self.__apply_reverse_ordering(self.__A)
        A = csr_array(A)
        return A

    def __get_graphlet_adjacency_1(self):
        A = self.get_orbit_adjacency(1, 1, 2)  # A1_2, single hop
        A += A.transpose()  # A2_1
        A += self.get_orbit_adjacency(2, 1, 1)  # A1_1, double hop
        return A

    def __get_graphlet_adjacency_2(self):
        A = self.get_orbit_adjacency(1, 3, 3)  # A3_3, single hop
        return A

    def __get_graphlet_adjacency_3(self):

        A = self.get_orbit_adjacency(1, 4, 5)  # A4_5, single hop
        A += self.get_orbit_adjacency(2, 4, 5)  # A4_5, double hop
        A += A.transpose()  # A5_4 and 5_4_bis
        A += self.get_orbit_adjacency(1, 5, 5)  # A5_5, single hop
        A += self.get_orbit_adjacency(3, 4, 4)  # A4_4, triple hop
        return A

    def __get_graphlet_adjacency_4(self):
        A = self.get_orbit_adjacency(1, 6, 7)  # A6_7, single hop
        A += A.transpose()  # A7_6
        A += self.get_orbit_adjacency(2, 6, 6)  # A6_6, double hop
        return A

    def __get_graphlet_adjacency_5(self):
        A = self.get_orbit_adjacency(1, 8, 8)  # A8_8, single hop
        A += self.get_orbit_adjacency(2, 8, 8)  # A8_8, double hop
        return A

    def __get_graphlet_adjacency_6(self):
        A = self.get_orbit_adjacency(2, 9, 10)  # A9_10, double hop
        A += self.get_orbit_adjacency(1, 9, 11)  # A9_11, single hop
        A += self.get_orbit_adjacency(1, 10, 11)  # A10_11, single hop
        A += A.transpose()
        A += self.get_orbit_adjacency(1, 10, 10)  # A10_10, single hop
        return A

    def __get_graphlet_adjacency_7(self):
        A = self.get_orbit_adjacency(1, 12, 13)  # A12_13 single hop
        A += A.transpose()
        A += self.get_orbit_adjacency(2, 12, 12)  # A12_12 double hop
        A += self.get_orbit_adjacency(1, 13, 13)  # A13_13 double hop
        return A

    def __get_graphlet_adjacency_8(self):
        A = self.get_orbit_adjacency(1, 14, 14)
        return A

    # ORBIT ADJACENCIES
    def generate_orbit_adjacencies(self, hop=None):
        """ Generate all node orbit adjacencies. """

        for (_hop, o1, o2), c_index in self.__ORBIT_ADJ_2_C_INDEX.items():
            if hop is None or _hop == hop:
                A = self.__get_orbit_adjacency_from_c_index(c_index)
                yield _hop, o1, o2, A
                if o1 != o2:
                    yield _hop, o2, o1, A.T

    def generate_edge_orbit_adjacencies(self):
        """ Generate all edge orbit adjacencies.

        Reference:
            Rossi, Ryan A., Nesreen K. Ahmed, and Eunyee Koh. "Higher-order
            network representation learning." Companion Proceedings of the The
            Web Conference 2018. 2018.
        """
        e = 0
        for (_hop, o1, o2), c_index in self.__ORBIT_ADJ_2_C_INDEX.items():
            if _hop == 1:
                A = self.__get_orbit_adjacency_from_c_index(c_index)
                if o1 == o2:
                    yield e, A
                    e += 1
                else:
                    A += A.T
                    yield e, A
                    e += 1

    def __get_orbit_adjacency_from_c_index(self, i):
        if i == -1:
            return self.__get_graphlet_adjacency_0()
        else:

            A_sparse = self.orbit_adjacencies[i]
            A = csr_array(
                (A_sparse[2, :], (A_sparse[0, :], A_sparse[1, :])), shape=(self.__n, self.__n))
            A = self.__apply_reverse_ordering(A)
            return A

    def get_GDVs(self):
        """ Return the graphlet degree vectors (GDVs) for the graph.

        Reference:
            Milenković, Tijana, and Nataša Pržulj. "Uncovering biological
            network function via graphlet degree signatures." Cancer
            informatics 6 (2008): CIN-S680.

        """

        # (hop, o1, o2): scaling_constant
        orbit_2_scaling = {(1, 0, 0): 1,
                           (1, 1, 2): 1,
                           (1, 2, 1): 2,
                           (1, 3, 3): 2,
                           (1, 4, 5): 1,
                           (1, 5, 5): 1,
                           (1, 6, 7): 1,
                           (1, 7, 6): 3,
                           (1, 8, 8): 2,
                           (1, 9, 11): 1,
                           (1, 10, 10): 1,
                           (1, 11, 9): 1,
                           (1, 12, 13): 2,
                           (1, 13, 12): 2,
                           (1, 14, 14): 3,
                           }

        GDVs = [None] * 15
        incumbent_orbit = 0
        for _hop, o1, o2, A in self.generate_orbit_adjacencies(hop=1):
            key = (_hop, o1, o2)
            if key in orbit_2_scaling:
                scaling = orbit_2_scaling[key]
                GDVs[o1] = A.sum(axis=1).squeeze() / scaling
        return np.stack(GDVs).T

    def get_edge_GDVs(self):
        """ Return the edge graphlet degree vectors (GDVs) for the graph.

        Reference:
            Solava, Ryan W., Ryan P. Michaels, and Tijana Milenković.
            "Graphlet-based edge clustering reveals pathogen-interacting
            proteins." Bioinformatics 28.18 (2012): i480-i486.  
        """

        # (hop, o1, o2): scaling_constant
        node_orbits = {(1, 2),
                       (3, 3),
                       (4, 5),
                       (5, 5),
                       (6, 7),
                       (8, 8),
                       (9, 11),
                       (10, 10),
                       (10, 11),
                       (12, 13),
                       (13, 13),
                       (14, 14),
                       }

        gdvs = [None] * 12
        e = 0
        for _, o1, o2, A in self.generate_orbit_adjacencies(hop=1):
            key = (o1, o2)
            if o1 == 0 and o2 == 0:
                rows, cols = A.nonzero()
                triu_indices = rows < cols
                rows = rows[triu_indices]
                cols = cols[triu_indices]

            if key in node_orbits:
                if o1 != o2:
                    A += A.T
                # gdvs[e] = A[rows, cols].A1
                gdvs[e] = A[rows, cols]
                e += 1
        return np.stack(gdvs).T

    def compute_A12_12_digraph(self, adj):
        import networkx as nx

        G = nx.from_numpy_array(adj, create_using=nx.Graph)
        G_digraph = nx.DiGraph(nodes=G.nodes())
        # G_digraph = nx.from_numpy_array(adj, create_using=nx.DiGraph)
        G_digraph.add_edges_from(G.edges())
        # k = G_digraph.number_of_nodes()
        A = np.zeros(adj.shape)

        for i in range(6):
            G_isoforms = nx.read_edgelist(
                f"determine_G7_directed_isoforms/G7_isoforms/G7_{i}.edgelist", create_using=nx.DiGraph)
            if nx.is_isomorphic(G_digraph, G_isoforms):
                print(f"ISOFORM {i}")

        print(G_digraph.edges())
        for a in G_digraph.nodes():
            for b in G_digraph.successors(a):
                if b > a:
                    for c in G_digraph.successors(a):
                        if c > b:
                            for d in G_digraph.successors(a):
                                if d > c:
                                    if G_digraph.has_edge(b, c):
                                        if G_digraph.has_edge(b, d):
                                            if not G_digraph.has_edge(c, d):
                                                print("iso 0:", a, b, c, d)
                                                A[c, d] += 1
                                                A[d, c] += 1
                                        elif G_digraph.has_edge(c, d):
                                            print("iso 1:", a, b, c, d)
                                            A[b, d] += 1
                                            A[d, b] += 1
                                    elif G_digraph.has_edge(b, d) and G.has_edge(c, d):
                                        print("iso 2:", a, b, c, d)
                                        A[c, b] += 1
                                        A[b, c] += 1
        # a is on orbit 13
        for a in G_digraph.nodes():
            for b in G_digraph.successors(a):
                if b > a:
                    for c in G_digraph.successors(a):
                        if c > b:
                            for d in G_digraph.successors(b):
                                if G_digraph.has_edge(b, c) and G.has_edge(c, d) and not G_digraph.has_edge(a, d):
                                    print("iso 3 and 4:", a, b, c, d)
                                    A[a, d] += 1
                                    A[d, a] += 1
                            for d in G_digraph.predecessors(b):
                                if d > a:
                                    if G_digraph.has_edge(b, c) and G_digraph.has_edge(d, c) and not G_digraph.has_edge(a, d):
                                        print("iso 5", a, b, c, d)
                                        A[a, d] += 1
                                        A[d, a] += 1

        return A

    def get_orbit_adjacency(self, hop, o1, o2):
        # print(hop, o1, o2)
        # if hop==2 and o1==12 and o2==12:
        #     return self.compute_A12_12_digraph(self.__A)

        if o1 < o2:
            key = (hop, o1, o2)
        else:
            key = (hop, o2, o1)

        if key not in self.__ORBIT_ADJ_2_C_INDEX:
            raise ValueError(
                f"Orbits {o1} and {o2} are not a valid '{hop}'-hop pair")
        else:
            c_index = self.__ORBIT_ADJ_2_C_INDEX[key]
            A = self.__get_orbit_adjacency_from_c_index(c_index)
            if o1 < o2:
                return A
            else:
                return A.T

    # IO
    def save_graphlet_adjacencies(self, prefix):
        for i, A in enumerate(self.generate_graphlet_adjacencies()):
            save_npz(f'{prefix}graphlet_adjacency_{i}.npz', A)

    def save_orbit_adjacencies(self, prefix, hop=None):
        for _hop, o1, o2, A in self.generate_orbit_adjacencies(hop):
            save_npz(
                f'{prefix}orbit_adjacency_hop_{_hop}_o1_{o1}_o2_{o2}.npz', A)

    def save_edge_orbit_adjacencies(self, prefix):
        for e, A in self.generate_edge_orbit_adjacencies():
            save_npz(f'{prefix}edge_orbit_adjacency_e_{e}.npz', A)


# METHODS FOR ITERATING OVER ADJACENCIES FROM FILES

def generate_graphlet_adjacency_file_handles(prefix):
    for graphlet in range(9):
        yield graphlet, f'{prefix}graphlet_adjacency_{graphlet}.npz'


def generate_orbit_adjacency_file_handles(prefix, hop=None):
    for (_hop, o1, o2), c_index in Counter._Counter__ORBIT_ADJ_2_C_INDEX.items():
        if hop is None or _hop == hop:
            yield _hop, o1, o2, f'{prefix}orbit_adjacency_hop_{_hop}_o1_{o1}_o2_{o2}.npz'
            if o1 != o2:
                yield _hop, o2, o1, f'{prefix}orbit_adjacency_hop_{_hop}_o1_{o2}_o2_{o1}.npz'


def generate_edge_orbit_adjacency_file_handles(prefix):
    e = 0
    for (_hop, o1, o2), c_index in Counter._Counter__ORBIT_ADJ_2_C_INDEX.items():
        if _hop == 1:
            yield e, f'{prefix}edge_orbit_adjacency_e_{e}.npz'
            e += 1


def iterate_graphlet_adjacencies_from_files(prefix):
    for graphlet, file_handle in enumerate(generate_graphlet_adjacency_file_handles(prefix)):
        yield graphlet, load_npz(f'{prefix}graphlet_adjacency_{graphlet}.npz')


def iterate_orbit_adjacencies_from_files(prefix, hop=None):
    for hop, o1, o2, file_handle in generate_orbit_adjacency_file_handles(prefix, hop):
        A = load_npz(file_handle)
        yield hop, o1, o2, A


def iterate_edge_orbit_adjacencies_from_files(prefix):
    for e, file_handle in generate_edge_orbit_adjacency_file_handles(prefix):
        A = load_npz(file_handle)
        yield e, A


def get_edge_gdv_from_precomputed(prefix):

    # (hop, o1, o2): scaling_constant
    node_orbits = {(1, 2),
                   (3, 3),
                   (4, 5),
                   (5, 5),
                   (6, 7),
                   (8, 8),
                   (9, 11),
                   (10, 10),
                   (10, 11),
                   (12, 13),
                   (13, 13),
                   (14, 14),
                   }

    gdvs = [None] * 12
    e = 0
    for _, o1, o2, A in iterate_orbit_adjacencies_from_files(prefix, hop=1):
        key = (o1, o2)
        if o1 == 0 and o2 == 0:
            rows, cols = A.nonzero()
            triu_indices = rows < cols
            rows = rows[triu_indices]
            cols = cols[triu_indices]

        if key in node_orbits:
            if o1 != o2:
                A += A.T
            gdvs[e] = A[rows, cols].A1
            e += 1
        if _hop > 1:
            break
    return np.stack(gdvs).T


def get_gdv_from_precomputed(prefix):

    # (hop, o1, o2): scaling_constant
    orbit_2_scaling = {(1, 0, 0): 1,
                       (1, 1, 2): 1,
                       (1, 2, 1): 2,
                       (1, 3, 3): 2,
                       (1, 4, 5): 1,
                       (1, 5, 5): 1,
                       (1, 6, 7): 1,
                       (1, 7, 6): 3,
                       (1, 8, 8): 2,
                       (1, 9, 11): 1,
                       (1, 10, 10): 1,
                       (1, 11, 9): 1,
                       (1, 12, 13): 2,
                       (1, 13, 12): 2,
                       (1, 14, 14): 3,
                       }

    gdvs = [None] * 15
    incumbent_orbit = 0
    for _, o1, o2, A in iterate_orbit_adjacencies_from_files(prefix, hop):
        key = (_hop, o1, o2)
        if key in orbit_2_scaling:
            scaling = orbit_2_scaling[key]
            gdvs[o1] = A.sum(axis=1).A1.squeeze() / scaling
    return np.stack(gdvs).T


def get_graphlet_counts_from_precomputed(prefix):
    gdvs = get_gdv_from_precomputed(prefix)

    count_0 = gdvs[:, 0]
    count_1 = gdvs[:, 1] + gdvs[:, 2]
    count_2 = gdvs[:, 3]
    count_3 = gdvs[:, 4] + gdvs[:, 5]
    count_4 = gdvs[:, 6] + gdvs[:, 7]
    count_5 = gdvs[:, 8]
    count_6 = gdvs[:, 9] + gdvs[:, 10] + gdvs[:, 11]
    count_7 = gdvs[:, 12] + gdvs[:, 13]
    count_8 = gdvs[:, 14]

    gc = np.column_stack((count_0, count_1, count_2, count_3, count_4, count_5,
                          count_6, count_7, count_8))
    return gc


def main():

    import gradco as gradco
    import numpy as np
    import networkx as nx

    n = 1000
    m = 4
    G = nx.barabasi_albert_graph(n, m, seed=0)
    A = nx.adjacency_matrix(G)
    A = A.toarray()

    counter = gradco.Counter(A)
    counter.count()

    orca_counts = gradco.run_orca(G, "node")
    w_counts = counter.get_GDVs()
    for i in range(15):
        print(i, np.sum(orca_counts[:, i] - w_counts[:, i]))

    orca_counts = gradco.run_orca(G, "edge")
    w_counts = counter.get_edge_GDVs()

    for i in range(12):
        print(i, np.sum(orca_counts[:, i] - w_counts[:, i]))


def run_orca(G, mode):
    import uuid
    import networkx as nx
    import time
    import subprocess
    import pandas as pd
    import os

    unique_id = uuid.uuid1()
    edgelist_file = 'G_{}.txt'.format(unique_id)
    gdv_file = 'G_{}_gdv_{}.txt'.format(mode, unique_id)

    G = nx.convert_node_labels_to_integers(G)
    with open(edgelist_file, 'w') as ostr:
        ostr.write(f"{G.number_of_nodes()} {G.number_of_edges()}\n")
        for edge in G.edges():
            if edge[0] < edge[1]:
                ostr.write(f"{edge[0]} {edge[1]}\n")

    command = ['./orca', mode, str(4), edgelist_file, gdv_file]
    start_time = time.time()
    subprocess.call(command,
                    # stdout=subprocess.DEVNULL,
                    # stderr=subprocess.DEVNULL,
                    timeout=24*60*60)

    df_counts = pd.read_csv(gdv_file, sep=' ', header=None)
    # cleanup
    os.remove(edgelist_file)
    os.remove(gdv_file)

    return df_counts.values


if __name__ == "__main__":
    main()
