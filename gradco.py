import gradco_c_routines
import numpy as np

class Counter(object):

    """Docstring for Counter. """

    def __init__(self, A):
        """TODO: to be defined.

        :A: TODO

        """
        
        # assert A is a valid adjacency matrix
        self.__assert_has_entries(A)
        self.__assert_equal_dims(A)
        self.__assert_unweighted(A)
        self.__assert_symmetric(A)
       
        # apply degree ordering
        self.__A, self.__order, self.__reverse_order = self.__apply_degree_ordering(A)

        # book keeping
        self.__n = A.shape[0]
        self.__orbit_adjacencies = None
        self.__orbits_singlehop_2_c_index = {
                                          (1, 2): 1,
                                          (3, 3): 2,
                                          (4, 5): 4, 
                                          (5, 5): 6,
                                          (6, 7): 8,
                                          (8, 8): 9,
                                          (9, 11): 12,
                                          (10, 10): 13,
                                          (10, 11): 14,
                                          (12, 13): 16,
                                          (13, 13): 17,
                                          (14, 14): 18
                                          }
        self.__orbits_doublehop_2_c_index = {(1, 1): 0,
                                           (4, 5): 5, 
                                           (6, 6): 7,
                                           (8, 8): 10,
                                           (9, 10): 11,
                                           (12, 12): 15}
        self.__orbits_tripplehop_2_c_index = {(4, 4): 3}

    """ SANITY CHECKS ON ADJACENCY MATRIX"""
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

    """ APPLY DEGREE ORDERING """
    def __apply_degree_ordering(self, A):
        rowsum = np.sum(A, axis=1)
        order = np.argsort(rowsum)
        reverse_order = np.argsort(order)
        A = A[order, :]
        A = A[:, order]
        return A, order, reverse_order

    def __apply_reverse_ordering(self, A):
        A = A[self.__reverse_order, :]
        A = A[:, self.__reverse_order]
        return A

    """ COUNT """
    def count(self):
        rows, cols = np.nonzero(self.__A)
        self.__orbit_adjacencies = gradco_c_routines.gradco_c_count(rows, cols, self.__n)

    """ GRAPHLET ADJACENCIES """
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
        return A

    def __get_graphlet_adjacency_1(self):
        A = self.get_orbit_adjacency(1, 2, 1) # A1_2, single hop
        A += A.transpose()  # A2_1
        A += self.get_orbit_adjacency(1, 1, 2) # A1_1, double hop
        return A
    
    def __get_graphlet_adjacency_2(self):
        A = self.get_orbit_adjacency(3, 3, 1) # A3_3, single hop 
        return A


    def __get_graphlet_adjacency_3(self):
        
        A = self.get_orbit_adjacency(4, 5, 1) # A4_5, single hop
        A += self.get_orbit_adjacency(4, 5, 2) # A4_5, double hop
        A += A.transpose()  # A5_4 and 5_4_bis
        A += self.get_orbit_adjacency(5, 5, 1) # A5_5, single hop
        A += self.get_orbit_adjacency(4, 4, 3)  # A4_4, triple hop
        return A

    def __get_graphlet_adjacency_4(self):
        A = self.get_orbit_adjacency(6, 7, 1) # A6_7, single hop
        A += A.transpose()  # A7_6
        A += self.get_orbit_adjacency(6, 6, 2) # A6_6, double hop
        return A

    def __get_graphlet_adjacency_5(self):
        A = self.get_orbit_adjacency(8, 8, 1) # A8_8, single hop
        A += self.get_orbit_adjacency(8, 8, 2) # A8_8, double hop
        return A

    def __get_graphlet_adjacency_6(self):
        A = self.get_orbit_adjacency(9, 10, 2) # A9_10, double hop
        A += self.get_orbit_adjacency(9, 11, 1) # A9_11, single hop
        A += self.get_orbit_adjacency(10, 11, 1) # A10_11, single hop
        A += A.transpose()
        A += self.get_orbit_adjacency(10, 10, 1) # A10_10, single hop
        return A

    def __get_graphlet_adjacency_7(self):
        A = self.get_orbit_adjacency(12, 13, 1)
        A += A.transpose()
        A += self.get_orbit_adjacency(12, 12, 2)
        A += self.get_orbit_adjacency(13, 13, 1)
        return A

    def __get_graphlet_adjacency_8(self):
        A = self.get_orbit_adjacency(14, 14, 1)
        return A

    """ ORBIT ADJACENCIES """
    def generate_orbit_adjacencies(self):
        for hop in range(1,4):
            for o1, o2, A in self.generate_orbit_adjacencies_for_hop(hop):
                yield o1, o2, hop, A 

    def generate_orbit_adjacencies_for_hop(self, hop):
        if hop == 1:
            yield 0, 0, self.__get_graphlet_adjacency_0()

        orbits_2_c_index = self.__hop_to_obit_c_index_map(hop)
        for (o1, o2), i in orbits_2_c_index.items():
            if (o1, o2) == (0, 0):
                A = self.__get_graphlet_adjacency_0()
            else:
                A = self.__get_orbit_adjacency_from_c_index(i)
            yield o1, o2, A
    
    def __hop_to_obit_c_index_map(self, hop):
        
        match hop:
            case 1:
                orbits_2_c_index = self.__orbits_singlehop_2_c_index
            case 2:
                orbits_2_c_index = self.__orbits_doublehop_2_c_index
            case 3:
                orbits_2_c_index = self.__orbits_tripplehop_2_c_index
            case _:
                raise ValueError('Hop must be between 1 and 3')

        return orbits_2_c_index

    def __get_orbit_adjacency_from_c_index(self, i):
        A = np.zeros((self.__n, self.__n))
        A_sparse = self.__orbit_adjacencies[i]
        A[A_sparse[0,:], A_sparse[1,:]] = A_sparse[2,:]
        A = self.__apply_reverse_ordering(A)
        return A
    
    """ get individual orbit adjacencies"""
    def get_orbit_adjacency(self, o1, o2, hop):

        if (o1, o2) == (0, 0):
            A = self.__get_graphlet_adjacency_0()
            return A

        orbit_2_c_index = self.__hop_to_obit_c_index_map(hop)
        if o1 <= o2:
            if (o1, o2) in orbit_2_c_index:
                i = orbit_2_c_index[(o1, o2)]
                A = self.__get_orbit_adjacency_from_c_index(i)
                return A
            else:
                raise ValueError(f"Orbits {o1} and {o2} are not a valid '{hop}'-hop pair")
        else:
            if (o2, o1) in orbit_2_c_index:
                i = orbit_2_c_index[(o1, o2)]
                A = self.__get_orbit_adjacency_from_c_index(i)
                return A.T
            else:
                raise ValueError(f"Orbits {o1} and {o2} are not a valid '{hop}'-hop pair")

    """ IO """
    def save_graphlet_adjacencies(self, prefix):
        for i, A in enumerate(self.generate_graphlet_adjacencies()):
            np.save(f'{prefix}graphlet_adjacency_{i}.npy', A)
    
    def save_orbit_adjacencies(self, prefix):
        for o1, o2, hop, A in self.generate_orbit_adjacencies():
            np.save(f'{prefix}orbit_adjacency_o1_{o1}_o2_{o2}_hop_{hop}.npy', A)


# METHODS FOR ITERATING OVER ADJACENCIES FROM FILES

def iterate_graphlet_adjacencies_from_files(prefix):
        for graphlet in range(9):
            yield graphlet, np.load(f'{prefix}graphlet_adjacency_{graphlet}.npy')

# def iterate_orbit_adjacencies_from_files(prefix):
        
#         o1=0 
#         o2=0
#         hop=1
#         yield o1, o2, hop, np.load(f'{prefix}orbit_adjacency_o1_{o1}_o2_{o2}_hop_{hop}.npy')
        
#         for (o1, o2) in self.__orbits_singlehop_2_c_index.keys():
#             A = np.load(f'{prefix}orbit_adjacency_o1_{o1}_o2_{o2}_hop_{hop}.npy')
#             yield o1, o2, hop, A
       
#         hop = 2
#         for (o1, o2) in self.__orbits_doublehop_2_c_index.keys():
#             A = np.load(f'{prefix}orbit_adjacency_o1_{o1}_o2_{o2}_hop_{hop}.npy')
#             yield o1, o2, hop, A
        
#         hop = 3
#         for (o1, o2) in self.__orbits_triplehop_2_c_index.keys():
#             A = np.load(f'{prefix}orbit_adjacency_o1_{o1}_o2_{o2}_hop_{hop}.npy')
#             yield o1, o2, hop, A
