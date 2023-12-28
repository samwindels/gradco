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
        A = self.get_orbit_adjacency(1, 12, 13)
        A += A.transpose()
        A += self.get_orbit_adjacency(2, 12, 12)
        A += self.get_orbit_adjacency(1, 13, 13)
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

    def __get_orbit_adjacency_from_c_index(self, i):
        if i == -1:
            return self.__get_graphlet_adjacency_0()
        else:
            # A = np.zeros((self.__n, self.__n))
            # A_sparse = self.__orbit_adjacencies[i]
            # A[A_sparse[0,:], A_sparse[1,:]] = A_sparse[2,:]
            # A = self.__apply_reverse_ordering(A)

            A_sparse = self.__orbit_adjacencies[i]
            A = csr_array((A_sparse[2,:], (A_sparse[0,:], A_sparse[1,:])), shape=(self.__n, self.__n))
            A = self.__apply_reverse_ordering(A)
            return A
    
    def get_orbit_adjacency(self, hop, o1, o2):

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


# METHODS FOR ITERATING OVER ADJACENCIES FROM FILES
def iterate_graphlet_adjacencies_from_files(prefix):
        for graphlet in range(9):
            yield graphlet, load_npz(f'{prefix}graphlet_adjacency_{graphlet}.npz')

def iterate_orbit_adjacencies_from_files(prefix, hop=None):
    for (_hop, o1, o2), c_index in Counter._Counter__ORBIT_ADJ_2_C_INDEX.items():
        if hop is None or _hop == hop:
            A = load_npz(f'{prefix}orbit_adjacency_hop_{_hop}_o1_{o1}_o2_{o2}.npz')
            yield _hop, o1, o2, A

# CENTRALITIES
def __normalize_symmetric(A):
    """
        Divide each entry of an adjacency matrix by square root of the
        rowsum and colsum. Implementation assumes M is symmetric.
    """
    D_array= np.array(A.sum(axis=1)).squeeze()
    D_array= np.power(D_array,0.5) + np.finfo(float).eps
    A = A / D_array[:,None]
    A = A / D_array[None,:]
    # __assert_rows_sum_to_max_one(A)
    # __assert_cols_sum_to_max_one(A)
    return A

def __normalize_rows(A):
    """
        Divide each entry of an adjacency matrix by the rowsum.
    """
    D_array = np.array(A.sum(axis=1)).squeeze()
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

def generate_graphlet_centrality_from_precomputed(prefix, normalize=None, num_iterations=1000):
    for graphlet, A in iterate_graphlet_adjacencies_from_files(prefix):
        A = A.toarray()
        if normalize is not None:
            case normalize:
                match "rows":
                    A = __normalize_rows(A)
                match "symmetric":
                    A = __normalize_symmetric(A)
                match _:
                    raise ValueError("normalize must be either 'rows' or 'symmetric'")

        eigen_value, eigen_vector = __power_iteration(A, num_iterations)
        yield graphlet, eigen_value, eigen_vector

def generate_orbit_centrality_from_precomputed(prefix, normalize=None, hop=None, num_iterations=1000):
    for hop, o1, o2, A in iterate_orbit_adjacencies_from_files(prefix, hop):
        A = A.toarray()
        A += 1  # add identity matrix to make sure it is irreducible
        
        if normalize is not None:
            case normalize:
                match "rows":
                    A = __normalize_rows(A)
                match "symmetric":
                    A = __normalize_symmetric(A)
                match _:
                    raise ValueError("normalize must be either 'rows' or 'symmetric'")

        eigen_value, eigen_vector = __power_iteration(A, num_iterations)
        yield hop, o1, o2, eigen_value, eigen_vector
        if o1 != o2:
            eigen_value, eigen_vector = __power_iteration(A.T, num_iterations)
            yield hop, o2, o1, eigen_value, eigen_vector




def main():

    import gradco as gradco
    import numpy as np
    import networkx as nx
    
    n = 8
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
    # for graphlet, A in gradco.iterate_graphlet_adjacencies_from_files(prefix):
    #     print("read GA:", graphlet)
    # for o1, o2, hop, A in gradco.iterate_orbit_adjacencies_from_files(prefix):
    #     print("read OA:", o1, o2, hop)


    for graphlet, eigen_value, eigen_vector in gradco.generate_graphlet_centrality_from_precomputed(prefix, 
                                                                                                    num_iterations=1000):
        print("graphlet:", graphlet)

    for hop, o2, o1, eigen_value, eigen_vector in gradco.generate_orbit_centrality_from_precomputed(prefix, 
                                                                                                      num_iterations=1000):
        print("orbit:", hop, o1, o2)

if __name__ == "__main__":
    main()
