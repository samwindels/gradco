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
            'A6_7': 8,
            'A8_8': 9,
            'A8_8_bis': 10,
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
        A += compute_orbit_adjacency(G, 'A4_5_bis') 
        A += A.transpose()  # A5_4 and 5_4_bis
        A += compute_orbit_adjacency(G, 'A4_4')
        A += compute_orbit_adjacency(G, 'A5_5')
        return A

def compute_graphlet_adjacency_8(G):

        A = compute_orbit_adjacency(G, 'A14_14')
        return A

def compute_graphlet_adjacency_5(G):

        A = compute_orbit_adjacency(G, 'A8_8')
        A += compute_orbit_adjacency(G, 'A8_8_bis')
        return A

def compute_A12_12_equation_based(G):

    A = -2* compute_orbit_adjacency(G, 'A8_8_bis')
    A1_1 = compute_orbit_adjacency(G, 'A1_1')

    for a, b, c in path_iterator(G):

        A[a, c] += A1_1[a, c] - 1
        A[c, a] += A1_1[c, a] - 1

    A /= 2
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
            # return compute_A6_7(G)
            return compute_orbit_adjacency(G, adj_type)
        case 'A8_8':
            # return compute_A8_8_single_hop_equation_based(G)
            return compute_orbit_adjacency(G, adj_type)
        case 'A11_10':
            return compute_A11_10(G)
        case 'A11_9':
            return compute_A11_9(G)
        case 'A9_11':
            # return compute_A9_11(G)  # implemented as transpose
            return compute_orbit_adjacency(G, adj_type)
        case 'A10_9':
            return compute_A10_9(G)
        case 'A9_10':
            return compute_A9_10(G)
            # return compute_orbit_adjacency(G, 'A9_10')
        case 'A10_10':
            # return compute_A10_10(G)
            # return compute_A10_10_equation_based(G)
            return compute_orbit_adjacency(G, 'A10_10')
        case 'A10_11':
            # return compute_A10_11_equation_based(G)
            return compute_orbit_adjacency(G, 'A10_11')
        case 'A12_12':
            # return compute_A12_12_equation_based(G)
            return compute_orbit_adjacency(G, adj_type)

        case 'A13_12':
            return compute_A13_12_equation_based(G)
        case 'A12_13':
            # return compute_A12_13(G)
            # return compute_A12_13_equation_based(G)
            return compute_orbit_adjacency(G, 'A12_13')
        case 'A13_13':
            # return compute_A13_13(G)
            return compute_orbit_adjacency(G, 'A13_13')
            # return compute_A13_13_equation_based(G)
        case 'A14_14':
            return compute_orbit_adjacency(G, adj_type)
            # return compute_A14_14_oriented_in_out(G)
            # return compute_A14_14_oriented_out_out(G)
            # return count_all(G)['A14_14']
        case 1:
            return compute_graphlet_adjacency_1(G)
        case 2:
            return compute_graphlet_adjacency_2(G)
        case 3:
            return compute_graphlet_adjacency_3(G)
        case 5:
            return compute_graphlet_adjacency_5(G)
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

    for A, integer, str_bit_array in generate_subgraph_permutations(5):
        G = nx.from_numpy_array(A)
        # compute_A8_8_digraph(G)
        # compute_A12_12_digraph(G)
        # compute_A4_4_G(G)
        # compute_A4_3_double_hop(G)
        # compute_A4_3_single_hop(G)
        # compute_A4_4_G(G)
        # compute_A5_5(G)
        # compute_A5_4_double_hop(G)
        # compute_A5_4_single_hop(G)
        # A12_13 = compute_A12_13(G)
        # A12_12 = compute_A12_12(G)
        # A13_12 = compute_A13_12(G)
        # A12_12 = compute_A12_12_faster(G)
        # A13_13 = compute_A13_13(G)
        # A14_14 = compute_A14_14(G)
        # A12_12 = compute_A12_12_fast(G)
        # A12_12 = compute_A12_12_fastest(G)
        # A8_8_single = compute_A8_8_single_hop(G)
        # AG7 = compute_AG7(G)
        # AG5 = compute_AG5(G)
        # compute_AG7_digraph(G)

"""
TODO:

- sanity checks
    - no self edges
    - no duplicate edges
- input: edelist of ints
    alternatives:
        leda, which is too much hastle
        mapping in gradco, but then we also have to return the mapping, to much hastle. have the user do it
- (to undirected graph)
- get node ordering nodes
    - degree based : arg sort on the degree  list 
        (reading twice can be avoided by storing the edges in a queue)
    - k core: 
        - argsort on the core numbers
- network to c data structure
    - multi/doubly linked list (https://stackoverflow.com/questions/22808713/doubly-linked-list-vs-multi-linked-list-in-c-c ,
    https://webdocs.cs.ualberta.ca/~holte/T26/mlinked-lists.html#sparse-matrices)
- triangle iterator
- path iterator
- G3
- (G4)
- G7
- G8

"""

if __name__ == "__main__":
    main()