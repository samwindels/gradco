import argparse
import numpy as np
import uuid
import networkx as nx
import subprocess
import os
from scipy.spatial.distance import squareform
import pandas as pd
import gradco
from itertools import combinations
from python_count_functions import *

adj2index = {

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


def format_gradco_output(A_sparse, n):
    A = np.zeros((n, n))
    if A.shape[1] >0:
        A[A_sparse[0,:], A_sparse[1,:]] = A_sparse[2,:]
    return A

def format_gradco_input(G):
    A = nx.to_numpy_array(G, dtype=int)
    A = A+A.transpose()
    A[A>0]=1

    rowsum = np.sum(A, axis=1)
    order = np.argsort(rowsum)

    # A = A[:, order]
    # A = A[order, :]


    n = A.shape[0]
    rows, cols = np.nonzero(A)
    return rows, cols, n

def compute_orbit_adjacency(G, adj_type):
        global adj2index
        rows, cols, n = format_gradco_input(G)
        tuple_index = adj2index[adj_type]
        if len(rows)>0:
            As_sparse = gradco.count(rows, cols, n, 2)
            A = As_sparse[tuple_index]
            return format_gradco_output(A, n)
        else:
            return np.zeros((n, n))

def compute_graphlet_adjacency_1(G):

        A = compute_orbit_adjacency(G, 'A1_2')
        A += A.transpose()  # A2_1
        A += compute_orbit_adjacency(G, 'A1_1')
        return A

def compute_graphlet_adjacency_2(G):

        A = compute_orbit_adjacency(G, 'A3_3')
        return A

def compute_graphlet_adjacency_3(G):
        
        A = compute_orbit_adjacency(G, 'A4_5')
        # A = compute_A4_5_equation_based(G)
        # assert np.sum(A<0)==0
        # return np.zeros((5, 5))
        A += compute_orbit_adjacency(G, 'A4_5_bis') 

        A_4_5_bis = compute_orbit_adjacency(G, 'A4_5_bis') 
        if np.sum(A_4_5_bis<0)!=0:
            print(f"{A_4_5_bis=}")
        
        # A_4_5 = compute_A4_5_equation_based(G)
        A_4_5 = compute_orbit_adjacency(G, 'A4_5') 
        if np.sum(A_4_5<0)!=0:
            # print(A_4_5)
            print(f"{A_4_5=}")
        
        A_5_5 = compute_orbit_adjacency(G, 'A5_5') 
        if np.sum(A_5_5<0)!=0:
            # print(A_5_5)
            print(f"{A_5_5=}")
        
        A_4_4 = compute_orbit_adjacency(G, 'A4_4') 
        if np.sum(A_4_4<0)!=0:
            print(f"{A_4_4=}")
        A += A.transpose()  # A5_4 and 5_4_bis
        A += compute_orbit_adjacency(G, 'A4_4')
        A += compute_orbit_adjacency(G, 'A5_5')
        return A

def compute_graphlet_adjacency_4(G):

        A = compute_orbit_adjacency(G, 'A6_7')
        A += A.transpose()  # A7_6
        A += compute_orbit_adjacency(G, 'A6_6')
        return A

def compute_graphlet_adjacency_5(G):

        A = compute_orbit_adjacency(G, 'A8_8')
        A += compute_orbit_adjacency(G, 'A8_8_bis')
        return A

def compute_graphlet_adjacency_6(G):

        A = compute_orbit_adjacency(G, 'A9_10')
        A += compute_orbit_adjacency(G, 'A9_11')
        A += compute_orbit_adjacency(G, 'A10_11')
        return A

def compute_graphlet_adjacency_7(G):

        A = compute_orbit_adjacency(G, 'A12_13')
        A += A.transpose()
        A += compute_orbit_adjacency(G, 'A12_12')
        A += compute_orbit_adjacency(G, 'A13_13')
        return A

def compute_graphlet_adjacency_8(G):

        A = compute_orbit_adjacency(G, 'A14_14')
        return A

def compute_A10_10_equation_based(G):

    A = - compute_orbit_adjacency(G, 'A12_13')
    A1_2 = compute_orbit_adjacency(G, 'A1_2')

    for a, b, c in triangle_iterator(G):

        A[a, b] += A1_2[a, c] 
        A[b, a] += A1_2[b, c] 

        A[a, c] += A1_2[a, b] 
        A[c, a] += A1_2[c, b] 

        A[b, c] += A1_2[b, a] 
        A[c, b] += A1_2[c, a] 

    return A

def compute_A10_11_equation_based(G):

    A1_2 = compute_A1_2(G)
    A = - compute_A12_13(G)
    for a, b, c in triangle_iterator(G):

        A[a, b] += A1_2[a, b]
        A[a, c] += A1_2[a, c]

        A[b, a] += A1_2[b, a]
        A[b, c] += A1_2[b, c]

        A[c, a] += A1_2[c, a]
        A[c, b] += A1_2[c, b]

    return A


def count(G, adj_type):

    match adj_type:
        case 'A1_1':
            return compute_orbit_adjacency(G, adj_type)
        case 'A1_2':
            return compute_orbit_adjacency(G, adj_type)
        case 'A2_1':
            return compute_orbit_adjacency(G, adj_type)
        case 'A3_3':
            return compute_orbit_adjacency(G, adj_type)
        case 'A4_4':
            return compute_orbit_adjacency(G, adj_type)
        case 'A4_5':
            return compute_orbit_adjacency(G, adj_type)
        case 'A5_5':
            return compute_orbit_adjacency(G, adj_type)
        case 'A6_7':
            return compute_orbit_adjacency(G, adj_type)
        case 'A6_6':
            return compute_orbit_adjacency(G, adj_type)
        case 'A8_8':
            return compute_orbit_adjacency(G, adj_type)
        case 'A9_10':
            return compute_orbit_adjacency(G, adj_type)
        case 'A9_11':
            return compute_orbit_adjacency(G, adj_type)
        case 'A10_10':
            # return compute_A10_10_equation_based(G)
            return compute_orbit_adjacency(G, adj_type)
        case 'A10_11':
            return compute_A10_11_equation_based(G)
            # return compute_orbit_adjacency(G, adj_type)
        case 'A12_12':
            return compute_orbit_adjacency(G, adj_type)
        case 'A12_13':
            return compute_orbit_adjacency(G, adj_type)
        case 'A13_12':
            return compute_orbit_adjacency(G, 'A12_13').transpose()
        case 'A13_13':
            return compute_orbit_adjacency(G, adj_type)
        case 'A14_14':
            return compute_orbit_adjacency(G, adj_type)
        case 1:
            return compute_graphlet_adjacency_1(G)
        case 2:
            return compute_graphlet_adjacency_2(G)
        case 3:
            return compute_graphlet_adjacency_3(G)
        case 4:
            return compute_graphlet_adjacency_4(G)
        case 5:
            return compute_graphlet_adjacency_5(G)
        case 6:
            return compute_graphlet_adjacency_6(G)
        case 7:
            return compute_graphlet_adjacency_7(G)
        case 8:
            return compute_graphlet_adjacency_8(G)
        case _:
            ValueError('invalid adjacency type')




def main():

   
    # G = nx.scale_free_graph(100)
    # compute_A9_11(G)
    # return
    # G = nx.read_edgelist('PPI_biogrid_yeast.edgelist')
    # format_gradco_input(G)
    # compute_AG3_digraph(G)
    # return
    G = nx.read_edgelist('COEX7_human_0.01_LCM.edgelist')
    format_gradco_input(G)
    # G = nx.read_edgelist('COEX7_human_0.01_LCM.edgelist')
    rows, cols, n = format_gradco_input(G)
    As_sparse = gradco.count(rows, cols, n, 2)
    return
    # G = nx.read_edgelist('orientation/nets/COEX_human_degenerate.edgelist')
    # compute_A8_8_digraph(G)
    # compute_AG7_digraph(G)
    # compute_AG7_digraph_two(G)
    # G = nx.read_edgelist('degenerate_tests/nets/PPI_yeast_degenerate.edgelist')
    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]
    rows, cols = np.nonzero(A)
    # print(rows)
    # print(cols)
    # rows = np.ascontiguousarray(rows) 
    # cols = np.ascontiguousarray(cols) 
    As = gradco.count(rows, cols, n, 2)
    print(As[2])
    return

    A = np.zeros((n, n))
    A[A_14_14_sparse[0,:], A_14_14_sparse[1,:]] = A_14_14_sparse[2,:]
    print(A)
    # print(np.sum(triu_counts/3))
    return


if __name__ == "__main__":
    main()
