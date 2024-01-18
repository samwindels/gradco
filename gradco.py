import gradco_c_routines
import numpy as np
from scipy.sparse import csr_array, save_npz, load_npz

# global __ORBIT_ADJ_2_C_INDEX 


class Counter(object):

    # (hop, orbit1, orbit2) -> c_index
    __ORBIT_ADJ_2_C_INDEX = {# single hop
                             (1, 0, 0): -1,  # standard adjacency matrix, not stored in c arrays
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
        # self.__assert_unweighted(A)
        # self.__assert_symmetric(A)
       
        # apply degree ordering
        self.__A, self.__order, self.__reverse_order = self.__apply_degree_ordering(A)

        # book keeping
        self.__n = A.shape[0]            # number of nodes
        self.__orbit_adjacencies = None  # where c counts will be stored
    
        

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
        rowsum = np.asarray(A.sum(axis=1)).squeeze() # scipy returns numpy matrix instead of array
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
        rows, cols = self.__A.nonzero()
        self.__orbit_adjacencies = gradco_c_routines.gradco_c_count(rows, cols, self.__n)

    # GRAPHLET ADJACENCIES
    def get_graphlet_adjacency(self, graphlet):

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
        A = self.get_orbit_adjacency(1, 1, 2) # A1_2, single hop
        A += A.transpose()  # A2_1
        A += self.get_orbit_adjacency(2, 1, 1) # A1_1, double hop
        return A
    
    def __get_graphlet_adjacency_2(self):
        A = self.get_orbit_adjacency(1, 3, 3) # A3_3, single hop 
        return A


    def __get_graphlet_adjacency_3(self):
        
        A = self.get_orbit_adjacency(1, 4, 5) # A4_5, single hop
        A += self.get_orbit_adjacency(2, 4, 5) # A4_5, double hop
        A += A.transpose()  # A5_4 and 5_4_bis
        A += self.get_orbit_adjacency(1, 5, 5) # A5_5, single hop
        A += self.get_orbit_adjacency(3, 4, 4)  # A4_4, triple hop
        return A

    def __get_graphlet_adjacency_4(self):
        A = self.get_orbit_adjacency(1, 6, 7) # A6_7, single hop
        A += A.transpose()  # A7_6
        A += self.get_orbit_adjacency(2, 6, 6) # A6_6, double hop
        return A

    def __get_graphlet_adjacency_5(self):
        A = self.get_orbit_adjacency(1, 8, 8) # A8_8, single hop
        A += self.get_orbit_adjacency(2, 8, 8) # A8_8, double hop
        return A

    def __get_graphlet_adjacency_6(self):
        A = self.get_orbit_adjacency(2, 9, 10) # A9_10, double hop
        A += self.get_orbit_adjacency(1, 9, 11) # A9_11, single hop
        A += self.get_orbit_adjacency(1, 10, 11) # A10_11, single hop
        A += A.transpose()
        A += self.get_orbit_adjacency(1, 10, 10) # A10_10, single hop
        return A

    def __get_graphlet_adjacency_7(self):
        A = self.get_orbit_adjacency(1, 12, 13)  #A12_13 single hop
        A += A.transpose()
        A += self.get_orbit_adjacency(2, 12, 12)  #A12_12 double hop
        A += self.get_orbit_adjacency(1, 13, 13)  #A13_13 double hop
        return A

    def __get_graphlet_adjacency_8(self):
        A = self.get_orbit_adjacency(1, 14, 14)
        return A

    # ORBIT ADJACENCIES
    def generate_orbit_adjacencies(self, hop=None):

        for (_hop, o1, o2), c_index in self.__ORBIT_ADJ_2_C_INDEX.items():
            if hop is None or _hop == hop:
                A = self.__get_orbit_adjacency_from_c_index(c_index)
                yield _hop, o1, o2, A
                if o1 != o2:
                    yield _hop, o2, o1, A.T

    def generate_edge_orbit_adjacencies(self):
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

            A_sparse = self.__orbit_adjacencies[i]
            A = csr_array((A_sparse[2,:], (A_sparse[0,:], A_sparse[1,:])), shape=(self.__n, self.__n))
            A = self.__apply_reverse_ordering(A)
            return A
    
    # def compute_A12_12_digraph(adj):
   
    #     G_digraph = nx.from_numpy_array(adj, using=nx.DiGraph)
    #     # G_digraph = nx.DiGraph(nodes=G.nodes())
    #     # G_digraph.add_edges_from(G.edges())
    #     # k = G_digraph.number_of_nodes()
    #     A = np.zeros(A.shape)
    
    #     print(G_digraph.edges())
    
    #     for a in G_digraph.nodes():
    #         for b in G_digraph.successors(a):
    #             for c in G_digraph.successors(a):
    #                 if c>b:
    #                     if G.has_edge(a, c): # check if b,c have triangle neighbours
    #                         # a is on orbit 12
    #                         for d in G_digraph.successors(c):
    #                             if d != a and d != b:
    #                                 if G.has_edge(d, b):
    #                                     if not G.has_edge(d, a):
    #                                         # print(a, b, c, d)
    #                                         A[a, d] += 1
    #                                         A[d, a] += 1
    #                         # check if a,b have triangle neighbours
    #                         # a is on orbit 13
    #                         # for d in G_digraph.neighbors(b):
    #                         #     if d != c and d != a:
    #                         #         if G_digraph.has_edge(d, a):
    #                         #             if not G.has_edge(c, d):
    #                         #                 A[c, d] += 1
    #                         #                 # A[d, c] += 1
    #                         #                 print('hit', a, b, c, d)
    #                         for d in G_digraph.neighbors(a):
    #                             if d != c and d != b:
    #                                 if G.has_edge(d, b):
    #                                     if not G.has_edge(c, d):
    #                                         A[c, d] += 1
    #                                         A[d, c] += 1
    #     return A
    
    def get_orbit_adjacency(self, hop, o1, o2):
        # if hop==1 and o1==12 and o2==12:
        #     return self.compute_A12_12_digraph(self.__A)

        if o1 < o2: 
            key = (hop, o1, o2)
        else:
            key = (hop, o2, o1)
        
        if key not in self.__ORBIT_ADJ_2_C_INDEX: 
            raise ValueError(f"Orbits {o1} and {o2} are not a valid '{hop}'-hop pair")
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
            save_npz(f'{prefix}orbit_adjacency_hop_{_hop}_o1_{o1}_o2_{o2}.npz', A)
    
    def save_edge_orbit_adjacencies(self, prefix):
        for e, A in self.generate_edge_orbit_adjacencies():
            save_npz(f'{prefix}edge_orbit_adjacency_e_{e}.npz', A)


# METHODS FOR ITERATING OVER ADJACENCIES FROM FILES
def iterate_graphlet_adjacencies_from_files(prefix):
        for graphlet in range(9):
            yield graphlet, load_npz(f'{prefix}graphlet_adjacency_{graphlet}.npz')

def iterate_orbit_adjacencies_from_files(prefix, hop=None):
    for (_hop, o1, o2), c_index in Counter._Counter__ORBIT_ADJ_2_C_INDEX.items():
        if hop is None or _hop == hop:
            A = load_npz(f'{prefix}orbit_adjacency_hop_{_hop}_o1_{o1}_o2_{o2}.npz')
            yield _hop, o1, o2, A
            if o1 != o2:
                A = load_npz(f'{prefix}orbit_adjacency_hop_{_hop}_o1_{o2}_o2_{o1}.npz')
                yield _hop, o2, o1, A

def iterate_edge_orbit_adjacencies_from_files(prefix):
    e = 0 
    for (_hop, o1, o2), c_index in Counter._Counter__ORBIT_ADJ_2_C_INDEX.items():
        if _hop == 1:
            A = load_npz(f'{prefix}edge_orbit_adjacency_e_{e}.npz')
            yield e, A
            e += 1

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
                                  
    gdvs = [ None ] * 12
    e = 0
    for _hop, o1, o2, A in iterate_orbit_adjacencies_from_files(prefix):
        key = (o1, o2)
        if o1 ==0 and o2 == 0:
            rows, cols = A.nonzero()
            triu_indices = rows<cols
            rows = rows[triu_indices]
            cols = cols[triu_indices]

        if key in node_orbits:
            if o1 != o2:
                A += A.T
            gdvs[e] = A[rows, cols].A1
            e += 1
        if _hop>1:
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
                                  
    gdvs = [ None ] * 15
    incumbent_orbit = 0
    for _hop, o1, o2, A in iterate_orbit_adjacencies_from_files(prefix):
        key = (_hop, o1, o2)
        if key in orbit_2_scaling:
            scaling = orbit_2_scaling[key]
            gdvs[o1] = A.sum(axis=1).A1.squeeze() / scaling
        if _hop>1:
            break
    return np.stack(gdvs).T


# CENTRALITIES
def __normalise_symmetric(A):
    """
        Divide each entry of an adjacency matrix by square root of the
        rowsum and colsum. Implementation assumes M is symmetric.
    """
    D_array= A.sum(axis=1).squeeze()
    D_array= np.power(D_array,0.5) + np.finfo(float).eps
    A = A / D_array[:,None]
    A = A / D_array[None,:]
    # __assert_rows_sum_to_max_one(A)
    # __assert_cols_sum_to_max_one(A)
    return A

def __normalise_rows(A):
    """
        Divide each entry of an adjacency matrix by the rowsum.
    """
    D_array = A.sum(axis=1).squeeze()
    D_array = D_array + np.finfo(float).eps
    A = A / D_array[:,None]

    # __assert_rows_sum_to_one(A)
    # __assert_rows_sum_to_max_one(A)
 
    return A

# def __assert_rows_sum_to_one(A):
#     if not np.allclose(np.sum(A, axis=1), 1): 
#         raise ValueError("Not all rows of A sum to 1")

# def __assert_rows_sum_to_max_one(A):
#     if not np.all(np.sum(A, axis=1) <= 1): 
#         raise ValueError("Not all rows of A sum to 1 at most")

# def __assert_cols_sum_to_max_one(A):
#     if not np.all(np.sum(matrix, axis=0) <= 1): 
#         raise ValueError("Not all colls of A sum to 1 at most")

def __power_iteration(matrix, num_iterations, convergence_threshold=1e-15):
    # Generate a random initial guess for the dominant eigenvector
    n = matrix.shape[0]
    eigen_vector = np.random.rand(n)
    # eigen_vector = np.ones(n)

    for iteration in range(num_iterations):
        # Compute the matrix-vector product
        matrix_times_vector = np.dot(matrix, eigen_vector)

        # Normalize the result to prevent divergence
        eigen_vector = matrix_times_vector / np.linalg.norm(matrix_times_vector)

        # Compute the eigenvalue estimate
        eigen_value = np.dot(np.dot(eigen_vector, matrix), eigen_vector)

        # Check for convergence
        if iteration > 0:
            eigen_value_change = abs(eigen_value - prev_eigen_value)
            if eigen_value_change < convergence_threshold:
                print(f"Poweriteration converged after {iteration} iterations.")
                break

        prev_eigen_value = eigen_value

    return eigen_value, eigen_vector

def __normalise(A, normalisation):
    match normalisation:
        case "rows":
            A = __normalise_rows(A)
        case "symmetric":
            A = __normalise_symmetric(A)
        case _:
            raise ValueError("normalise must be either 'rows' or 'symmetric'")

def generate_graphlet_centrality_from_precomputed(prefix, normalisation=None, num_iterations=1000):
    for graphlet, A in iterate_graphlet_adjacencies_from_files(prefix):
        A = A.toarray()
        if normalisation is not None:
            __normalise(A, normalisation)
        eigen_value, eigen_vector = __power_iteration(A, num_iterations)
        yield graphlet, eigen_value, eigen_vector

def generate_orbit_centrality_from_precomputed(prefix, normalisation=None, hop=None, num_iterations=1000):
    for hop, o1, o2, A in iterate_orbit_adjacencies_from_files(prefix, hop):
        A = A.toarray()
        A += 1  # add identity matrix to make sure it is irreducible
        if normalisation is not None:
            __normalise(A, normalisation)
        
        eigen_value, eigen_vector = __power_iteration(A, num_iterations)
        yield hop, o1, o2, eigen_value, eigen_vector
        if o1 != o2:
            eigen_value, eigen_vector = __power_iteration(A.T, num_iterations)
            yield hop, o2, o1, eigen_value, eigen_vector

def generate_edge_orbit_centrality_from_precomputed(prefix, normalisation=None, num_iterations=1000):
    for e, A in iterate_edge_orbit_adjacencies_from_files(prefix):
        A = A.toarray()
        if normalisation is not None:
            __normalise(A, normalisation)
        eigen_value, eigen_vector = __power_iteration(A, num_iterations)
        yield e, eigen_value, eigen_vector


def main():

    import gradco as gradco
    import numpy as np
    import networkx as nx
    
    n = 1000
    m = 4
    G = nx.barabasi_albert_graph(n, m, seed=0)
    # A = nx.to_scipy_sparse_array(G)
    A = nx.adjacency_matrix(G)
    A = A.todense()
    # A = csr_matrix(A)
    # A = np.array(A)

    counter = gradco.Counter(A)
    counter.count()

    # dense_c = gradco.Counter(A)
    # dense_c.count()
    
    # sparse_c = gradco.Counter(csr_array(A))
    # sparse_c.count()

    # for ((hop, o1, o2, A), (_, _,_, A_sparse))  in zip(dense_c.generate_orbit_adjacencies(), sparse_c.generate_orbit_adjacencies()):
    #     print(A_sparse.todense())
    #     if np.sum(A - A_sparse) != 0:
    #         print("ERROR")
    #         print(hop, o1, o2)
    #         print(A-A_sparse)
    #         # break 

    prefix = "scratch/"
    counter.save_graphlet_adjacencies(prefix)
    counter.save_orbit_adjacencies(prefix)
    counter.save_edge_orbit_adjacencies(prefix)
    for graphlet, A in gradco.iterate_graphlet_adjacencies_from_files(prefix):
        print("read GA:", graphlet)
    for o1, o2, hop, A in gradco.iterate_orbit_adjacencies_from_files(prefix):
        print("read OA:", o1, o2, hop)
    for e, A in gradco.iterate_edge_orbit_adjacencies_from_files(prefix):
        print("read EA:", e)
    for graphlet, eigen_value, eigen_vector in gradco.generate_graphlet_centrality_from_precomputed(prefix):
        print("graphlet:", graphlet)
    for hop, o2, o1, eigen_value, eigen_vector in gradco.generate_orbit_centrality_from_precomputed(prefix):
        print("orbit:", hop, o1, o2)
    for e, eigen_value, eigen_vector in gradco.generate_edge_orbit_centrality_from_precomputed(prefix, num_iterations=1000):
        print("edge orbit:", e)
    
    orca_counts = gradco.run_orca(G, "node")
    w_counts = gradco.get_gdv_from_precomputed(prefix)
    for i in range(15):
        print(i, np.sum(orca_counts[:, i] - w_counts[:, i]))
    
    orca_counts = gradco.run_orca(G, "edge")
    w_counts = gradco.get_edge_gdv_from_precomputed(prefix)
    print(orca_counts.shape)
    print(w_counts.shape)

    for i in range(12):
        print(i, np.sum(orca_counts[:, i] - w_counts[:, i]))
        pass
    
 
def run_orca(G, mode):
    import uuid
    import networkx as nx 
    import time
    import subprocess
    import pandas as pd
    import os

    unique_id = uuid.uuid1()
    edgelist_file='G_{}.txt'.format(unique_id)
    gdv_file='G_{}_gdv_{}.txt'.format(mode, unique_id)

    G = nx.convert_node_labels_to_integers(G)
    with open(edgelist_file, 'w') as ostr:
        ostr.write(f"{G.number_of_nodes()} {G.number_of_edges()}\n")
        for edge in G.edges():
            if edge[0] < edge[1]:
                ostr.write(f"{edge[0]} {edge[1]}\n")

    command=['./orca', mode,str(4),edgelist_file, gdv_file]
    start_time = time.time()
    subprocess.call(command,
                    # stdout=subprocess.DEVNULL,
                    # stderr=subprocess.DEVNULL,
                    timeout=24*60*60)

    df_counts = pd.read_csv(gdv_file, sep=' ', header=None)
    #cleanup
    os.remove(edgelist_file)
    os.remove(gdv_file)

    return df_counts.values


if __name__ == "__main__":
    main()
