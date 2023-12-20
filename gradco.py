import gradco_c_routines
import numpy as np

class Counter(object):

    """Docstring for Counter. """

    def __init__(self, A):
        """TODO: to be defined.

        :A: TODO

        """

        self.__A, self.__order, self.__reverse_order = self.__apply_degree_ordering(A)
        assert A.shape[0] == A.shape[1]
        self.__n = A.shape[0]
        self.__orbit_adjacencies = None
        self.__adj2index = {
                            'A1_1': 0,
                            'A1_2': 1,
                            'A3_3': 2,
                            'A4_4': 3,
                            'A4_5': 4,
                            'A4_5_bis': 5,
                            'A5_5': 6,
                            'A6_6': 7,
                            'A6_7': 8,
                            'A8_8': 9,
                            'A8_8_bis': 10,
                            'A9_10': 11,
                            'A9_11': 12,
                            'A10_10': 13,
                            'A10_11': 14,
                            'A12_12': 15,
                            'A12_13': 16,
                            'A13_13': 17,
                            'A14_14': 18
                }

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

    def count(self):
        rows, cols = np.nonzero(self.__A)
        # self.__orbit_adjacencies = gradco_c_routines.count(rows, cols, self.__n)
        self.__orbit_adjacencies = gradco_c_routines.gradco_c_count(rows, cols, self.__n)

    def generate_orbit_adjacencies(self, matrix_format=None):
        for label, i in self.__adj2index.items():
            A = np.zeros((self.__n, self.__n))
            A_sparse = self.__orbit_adjacencies[i]
            A[A_sparse[0,:], A_sparse[1,:]] = A_sparse[2,:]
            return self.__apply_degree_ordering(A)

    def get_graphlet_adjacency(self, graphlet):

        match graphlet:
            case 0:
                return self.__graphlet_adjacency_0()
            case 1:
                return self.__graphlet_adjacency_1()
            case 2:
                return self.__graphlet_adjacency_2()
            case 3:
                return self.__graphlet_adjacency_3()
            case 4:
                return self.__graphlet_adjacency_4()
            case 5:
                return self.__graphlet_adjacency_5()
            case 6:
                return self.__graphlet_adjacency_6()
            case 7:
                return self.__graphlet_adjacency_7()
            case 8:
                return self.__graphlet_adjacency_8()
            case _:
                raise ValueError('Graphlet index must be between 0 and 8')

    def generate_graphlet_adjacencies(self):

        yield self.__graphlet_adjacency_0()
        yield self.__graphlet_adjacency_1()
        yield self.__graphlet_adjacency_2()
        yield self.__graphlet_adjacency_3()
        yield self.__graphlet_adjacency_4()
        yield self.__graphlet_adjacency_5()
        yield self.__graphlet_adjacency_6()
        yield self.__graphlet_adjacency_7()
        yield self.__graphlet_adjacency_8()


    def get_orbit_adjacency(self, adj_type):
        A = np.zeros((self.__n, self.__n))
        A_sparse = self.__orbit_adjacencies[self.__adj2index[adj_type]]
        A[A_sparse[0,:], A_sparse[1,:]] = A_sparse[2,:]
        return A


    def __graphlet_adjacency_0(self):
        A = self.__apply_reverse_ordering(self.__A)
        return A

    def __graphlet_adjacency_1(self):
        A = self.get_orbit_adjacency('A1_2')
        A += A.transpose()  # A2_1
        A += self.get_orbit_adjacency('A1_1')
        A = self.__apply_reverse_ordering(A)
        return A


    def __graphlet_adjacency_2(self):
        A = self.get_orbit_adjacency('A3_3')
        A = self.__apply_reverse_ordering(A)
        return A

    def __graphlet_adjacency_3(self):
        
        A = self.get_orbit_adjacency('A4_5')
        A = self.get_orbit_adjacency('A4_5_bis')
        A += A.transpose()  # A5_4 and 5_4_bis
        A = self.get_orbit_adjacency('A5_5')
        A = self.get_orbit_adjacency('A4_4')
        A = self.__apply_reverse_ordering(A)
        return A

    def __graphlet_adjacency_4(self):
        A = self.get_orbit_adjacency('A6_7')
        A += A.transpose()  # A7_6
        A += self.get_orbit_adjacency('A6_6')
        A = self.__apply_reverse_ordering(A)
        return A

    def __graphlet_adjacency_5(self):
        A = self.get_orbit_adjacency('A8_8')
        A += self.get_orbit_adjacency('A8_8_bis')
        A = self.__apply_reverse_ordering(A)
        return A

    def __graphlet_adjacency_6(self):
        A = self.get_orbit_adjacency('A9_10')
        A += self.get_orbit_adjacency('A9_11')
        A += self.get_orbit_adjacency('A10_11')
        A += A.transpose()
        A += self.get_orbit_adjacency('A10_10')
        A = self.__apply_reverse_ordering(A)
        return A

    def __graphlet_adjacency_7(self):
        A = self.get_orbit_adjacency('A12_13')
        A += A.transpose()
        A += self.get_orbit_adjacency('A12_12')
        A += self.get_orbit_adjacency('A13_13')
        A = self.__apply_reverse_ordering(A)
        return A

    def __graphlet_adjacency_8(self):
        A = self.get_orbit_adjacency('A14_14')
        A = self.__apply_reverse_ordering(A)
        return A
