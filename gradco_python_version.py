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


def get_gdv(G):

    unique_id = uuid.uuid1()
    edgelist_file = 'G_{}.txt'.format(unique_id)
    gdv_file = 'G_gdv_{}.txt'.format(unique_id)
    # H=convert_node_labels_to_integers(G) #node ordering is same as G.nodes()
    H = G
    H.remove_edges_from(nx.selfloop_edges(H))

    try:
        with open(edgelist_file, 'w') as o_stream:
            o_stream.write("{} {}\n".format(
                H.number_of_nodes(), H.number_of_edges()))
            for line in nx.generate_edgelist(H, data=False):
                o_stream.write("{}\n".format(line))

        command = ['./orca', 'node', str(4), edgelist_file, gdv_file]
        # print(" ".join(command))
        subprocess.call(command, stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        # subprocess.call(command)
        return np.loadtxt(gdv_file)

    finally:
        os.remove(gdv_file)
        os.remove(edgelist_file)


def generate_subgraph_permutations(k):

    max_edges = (k*(k-1))/2
    assert max_edges.is_integer()
    max_edges = int(max_edges)

    for integer in range(2**max_edges):
        bit_array, str_bit_array = get_binary_array(integer, max_edges)

        A = squareform(bit_array)
        yield A, integer, str_bit_array


def get_little_endian_string(integer):
    return format(integer, "b")[::-1]


def get_binary_array(integer, array_length):

    str_bit_array = get_little_endian_string(integer)
    str_bit_array = str_bit_array + \
        "".join(["0"]*(array_length-len(str_bit_array)))

    bit_array = [int(bit) for bit in str_bit_array]

    return bit_array, str_bit_array


def compute_A12_12(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c == a:
                    continue
                for d in G.neighbors(c):
                    if d == a or d == b:
                        continue
                    if G.has_edge(b, d) and \
                       G.has_edge(a, d) and \
                       not G.has_edge(a, c):
                        A[a, c] += 1
                    if G.has_edge(a, c) and \
                       G.has_edge(b, d) and \
                       not G.has_edge(a, d):
                        A[a, d] += 1
    A /= 4
    orbit_count = get_gdv(G)[:, 12]
    assert np.array_equal(np.sum(A, axis=1), orbit_count)
    return A


def compute_A12_13(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c == a:
                    continue
                for d in G.neighbors(c):
                    if d == a or d == b:
                        continue
                    if G.has_edge(b, d) and \
                       G.has_edge(a, d) and \
                       not G.has_edge(a, c):
                        A[a, b] += 1
                        A[a, d] += 1
                    if G.has_edge(a, c) and \
                       G.has_edge(b, d) and \
                       not G.has_edge(a, d):
                        A[a, b] += 1
                        A[a, c] += 1
    A /= 4  # overcount correction
    orbit_count = get_gdv(G)[:, 12]
    assert np.array_equal(np.sum(A, axis=1)/2, orbit_count)
    return A


def compute_A13_12(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c == a:
                    continue
                for d in G.neighbors(c):
                    if d == a or d == b:
                        continue
                    if G.has_edge(a, c) and \
                       G.has_edge(a, d) and \
                       not G.has_edge(d, b):
                        A[a, b] += 1
                        A[a, d] += 1

    A /= 2  # overcount correction
    orbit_count = get_gdv(G)[:, 13]
    assert np.array_equal(np.sum(A, axis=1)/2, orbit_count)
    return A


def compute_A13_13(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c == a:
                    continue
                for d in G.neighbors(c):
                    if d == a or d == b:
                        continue
                    if G.has_edge(a, c) and \
                       G.has_edge(a, d) and \
                       not G.has_edge(d, b):
                        A[a, c] += 1

    A /= 2  # overcount correction
    orbit_count = get_gdv(G)[:, 13]
    assert np.array_equal(np.sum(A, axis=1)/1, orbit_count)
    return A


def compute_A14_14(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c == a:
                    continue
                for d in G.neighbors(c):
                    if d == a or d == b:
                        continue
                    if G.has_edge(a, c) and \
                       G.has_edge(a, d) and \
                       G.has_edge(d, b):
                        A[a, b] += 1
                        A[a, c] += 1
                        A[a, d] += 1

    A /= 6  # overcount correction
    orbit_count = get_gdv(G)[:, 14]
    assert np.array_equal(np.sum(A, axis=1)/3, orbit_count)
    return A


def compute_A12_12_fast(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    for a in G.nodes():
        for b in G.neighbors(a):
            neighbours_connected = []
            neighbours_not_connected = []

            for z in G.neighbors(b):
                if z == a:
                    continue
                if G.has_edge(a, z):
                    neighbours_connected.append(z)
                else:
                    neighbours_not_connected.append(z)
            for c in neighbours_connected:
                for d in neighbours_not_connected:
                    if G.has_edge(c, d):
                        A[a, d] += 1

    A /= 2
    orbit_count = get_gdv(G)[:, 12]
    assert np.array_equal(np.sum(A, axis=1), orbit_count)
    return A


def compute_A12_12_digraph(G):

    G_digraph = nx.DiGraph(nodes=G.nodes())
    G_digraph.add_edges_from(G.edges())
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    print(G_digraph.edges())

    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(b):
                if G.has_edge(a, c):
                    # check if b,c have triangle neighbours
                    # a is on orbit 12
                    for d in G_digraph.successors(c):
                        if d != a and d != b:
                            if G.has_edge(d, b):
                                if not G.has_edge(d, a):
                                    # print(a, b, c, d)
                                    A[a, d] += 1
                                    A[d, a] += 1
                    # check if a,b have triangle neighbours
                    # a is on orbit 13
                    # for d in G_digraph.neighbors(b):
                    #     if d != c and d != a:
                    #         if G_digraph.has_edge(d, a):
                    #             if not G.has_edge(c, d):
                    #                 A[c, d] += 1
                    #                 # A[d, c] += 1
                    #                 print('hit', a, b, c, d)
                    for d in G_digraph.neighbors(a):
                        if d != c and d != b:
                            if G.has_edge(d, b):
                                if not G.has_edge(c, d):
                                    A[c, d] += 1
                                    A[d, c] += 1
                                    print('hat', a, b, c, d)
    return A


def compute_A12_12_fastest(G):
    # no overcounting
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    # a on orbit 12
    for a in G.nodes():
        for b in G.neighbors(a):
            neighbours_connected = []
            neighbours_not_connected = []

            for z in G.neighbors(b):
                if z == a:
                    continue
                if G.has_edge(a, z):
                    if z > b:
                        neighbours_connected.append(z)
                elif z < a:
                    neighbours_not_connected.append(z)
            for c in neighbours_connected:
                for d in neighbours_not_connected:
                    if G.has_edge(c, d):
                        if c > b:
                            # should be able to be made faster -> register a,d and d,a at the same time
                            A[a, d] += 1

    # a on orbit 13
    for a in G.nodes():
        for b in G.neighbors(a):
            if b < a:
                continue
            neighbours_connected = []

            for z in G.neighbors(b):
                if z == a:
                    continue
                if G.has_edge(a, z):
                    neighbours_connected.append(z)
            for i in range(len(neighbours_connected)):
                c = neighbours_connected[i]
                for j in range(i+1, len(neighbours_connected)):
                    d = neighbours_connected[j]
                    if not G.has_edge(c, d):
                        # should be able to be made faster -> register c,d and d,c at the same time
                        A[c, d] += 1

    A /= 1
    orbit_count = get_gdv(G)[:, 12]
    assert np.array_equal(np.sum(A, axis=1), orbit_count)
    return A


def compute_A8_8_single_hop(G):
    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]
    print('A', A)
    triu = gradco.count(A, n, 1)
    AG1 = squareform(triu)

    k = G.number_of_nodes()
    A8_8 = np.zeros((k, k))
    for a in G.nodes():
        for b in G.neighbors(a):
            if b > a:
                for c in G.neighbors(b):
                    if c != a and A[a, c] == 0:
                        if AG1[a, c] > 1:
                            A8_8[a, b] += (AG1[a, c]) - 1
                            A8_8[b, a] += AG1[a, c] - 1
                            # A8_8[a, c] += (AG1[a, c] - 1)/2

    orbit_count = get_gdv(G)[:, 8]
    # if np.sum(orbit_count) > 0:
    print('')
    print(A)
    print(A8_8)
    print(orbit_count)
    print((np.sum(A8_8, axis=1)/2))
    print(AG1)
    assert np.allclose(np.sum(A8_8, axis=1)/2,
                       orbit_count, atol=1e-1, rtol=1e-1)
    return A8_8


def compute_AG7(G):

    A12_13 = compute_A12_13(G)
    # A12_12 = compute_A12_12(G)
    A13_12 = compute_A13_12(G)
    A12_12 = compute_A12_12_fastest(G)
    A13_13 = compute_A13_13(G)
    AG7 = A12_13 + A13_12 + A12_12 + A13_13
    return AG7


def compute_A12_12_c(G):

    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]
    triu_counts = gradco.count(A, n, 1212)
    return squareform(triu_counts)


def compute_A4_4_G(G):

    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]

    k = G.number_of_nodes()
    A4_4 = np.zeros((k, k), dtype=int)

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c != a and not G.has_edge(a, c):
                    for d in G.neighbors(c):
                        if d != b and not G.has_edge(a, d)\
                                and not G.has_edge(b, d):
                            A4_4[a, d] += 1

    # orbit_count = get_gdv(G)[:, 4]
    # assert np.allclose(np.sum(A4_4, axis=1),
    #                    orbit_count, atol=1e-1, rtol=1e-1)
    return A4_4


def compute_A4_3_double_hop(G):

    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]

    k = G.number_of_nodes()
    A4_3 = np.zeros((k, k), dtype=int)

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c != a and not G.has_edge(a, c):
                    for d in G.neighbors(c):
                        if d != b and not G.has_edge(a, d)\
                                and not G.has_edge(b, d):
                            A4_3[a, c] += 1

    # orbit_count = get_gdv(G)[:, 4]
    # assert np.allclose(np.sum(A4_3, axis=1),
    #                    orbit_count, atol=1e-1, rtol=1e-1)
    return A4_3


def compute_A4_3_single_hop(G):

    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]

    k = G.number_of_nodes()
    A4_3 = np.zeros((k, k), dtype=int)

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c != a and not G.has_edge(a, c):
                    for d in G.neighbors(c):
                        if d != b and not G.has_edge(a, d)\
                                and not G.has_edge(b, d):
                            A4_3[a, b] += 1

    return A4_3


def compute_A5_5(G):

    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]

    k = G.number_of_nodes()
    A5_5 = np.zeros((k, k), dtype=int)

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c != a and not G.has_edge(a, c):
                    for d in G.neighbors(c):
                        if d != b and not G.has_edge(a, d)\
                                and not G.has_edge(b, d):
                            A5_5[b, c] += 1

    # orbit_count = get_gdv(G)[:, 5]
    # assert np.allclose(np.sum(A5_5, axis=1),
    #                    orbit_count, atol=1e-1, rtol=1e-1)
    return A5_5


def compute_A5_4_double_hop(G):

    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]

    k = G.number_of_nodes()
    A5_4 = np.zeros((k, k), dtype=int)

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c != a and not G.has_edge(a, c):
                    for d in G.neighbors(c):
                        if d != b and not G.has_edge(a, d)\
                                and not G.has_edge(b, d):
                            A5_4[b, d] += 1

    # orbit_count = get_gdv(G)[:, 5]
    # assert np.allclose(np.sum(A5_4, axis=1),
    #                    orbit_count, atol=1e-1, rtol=1e-1)
    return A5_4


def compute_A5_4_single_hop(G):

    A = nx.to_numpy_array(G, dtype=int)
    n = A.shape[0]

    k = G.number_of_nodes()
    A5_4 = np.zeros((k, k), dtype=int)

    for a in G.nodes():
        for b in G.neighbors(a):
            for c in G.neighbors(b):
                if c != a and not G.has_edge(a, c):
                    for d in G.neighbors(c):
                        if d != b and not G.has_edge(a, d)\
                                and not G.has_edge(b, d):
                            A5_4[b, a] += 1

    # orbit_count = get_gdv(G)[:, 5]
    # if np.sum(orbit_count) > 0:
    # print('')
    # print(A)
    # print(A5_5)
    # print(orbit_count)
    # print((np.sum(A5_5, axis=1)))
    # assert np.allclose(np.sum(A5_4, axis=1),
    #                    orbit_count, atol=1e-1, rtol=1e-1)
    return A5_4


def compute_AG3(G):

    k = G.number_of_nodes()
    AG3 = np.zeros((k, k), dtype=int)
    AG3 += compute_A4_4_G(G)
    AG3 += compute_A4_3_double_hop(G)
    AG3 += compute_A4_3_single_hop(G)
    AG3 += compute_A5_5(G)
    AG3 += compute_A5_4_double_hop(G)
    AG3 += compute_A5_4_single_hop(G)
    return AG3


def compute_A8_8_digraph(G):

    G = nx.convert_node_labels_to_integers(G)
    G_digraph = nx.DiGraph(nodes=G.nodes())
    G_digraph.add_edges_from(G.edges())
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    # ESCAPE, FIG 4 (A)
    # b=i, c=j
    print('ESCAPE (A)')
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                if b != c and not G.has_edge(b, c):
                    if c < b:
                        for d in G_digraph.predecessors(c):
                            if d != a and not G.has_edge(a, d):
                                if d > a:
                                    if G_digraph.has_edge(d, b):
                                        # print('loop (a)', a, b, c, d)
                                        A[a, b] += 1
                                        A[a, c] += 1
                                        A[a, d] += 1
                                        A[b, a] += 1
                                        A[b, c] += 1
                                        A[b, d] += 1
                                        A[c, a] += 1
                                        A[c, b] += 1
                                        A[c, d] += 1
                                        A[d, a] += 1
                                        A[d, b] += 1
                                        A[d, c] += 1

    # ESCAPE, FIG 4 (b)
    # b = i, c = j
    print('ESCAPE (B)')
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.predecessors(a):
                if b != c and not G.has_edge(b, c):
                    for d in G_digraph.successors(c):
                        if d != a and not G.has_edge(a, d):
                            if d > a:
                                if G_digraph.has_edge(d, b):
                                    # print('loop (b)', a, b, c, d)
                                    A[a, b] += 1
                                    A[a, c] += 1
                                    A[a, d] += 1
                                    A[b, a] += 1
                                    A[b, c] += 1
                                    A[b, d] += 1
                                    A[c, a] += 1
                                    A[c, b] += 1
                                    A[c, d] += 1
                                    A[d, a] += 1
                                    A[d, b] += 1
                                    A[d, c] += 1
    # ESCAPE, FIG 4 (c)
    # b = i, c = j
    print('ESCAPE (C)')
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                if b != c and not G.has_edge(b, c):
                    for d in G_digraph.successors(c):
                        if not G.has_edge(a, d):
                            if G_digraph.has_edge(d, b):
                                # print('loop (c)', a, b, c, d)
                                A[a, b] += 1
                                A[a, c] += 1
                                A[a, d] += 1
                                A[b, a] += 1
                                A[b, c] += 1
                                A[b, d] += 1
                                A[c, a] += 1
                                A[c, b] += 1
                                A[c, d] += 1
                                A[d, a] += 1
                                A[d, b] += 1
                                A[d, c] += 1

    A /= 1  # overcount correction
    # orbit_count = get_gdv(G)[:, 8]
    # print('')
    # print(nx.to_numpy_array(G))
    # print(A)
    # print(orbit_count)
    # print((np.sum(A, axis=1))/3)
    # assert np.array_equal(np.sum(A, axis=1)/3, orbit_count)
    return A


def compute_AG7_digraph(G):

    G = nx.convert_node_labels_to_integers(G)
    G_digraph = nx.DiGraph(nodes=G.nodes())
    G_digraph.add_edges_from(G.edges())
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    # ESCAPE, FIG 4 (A)
    # b=i, c=j
    print('ESCAPE (A)')
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                if b < c and G.has_edge(b, c):
                    for d in G_digraph.predecessors(c):
                        if d > a and not G.has_edge(a, d):
                            if G_digraph.has_edge(d, b):
                                A[a, b] += 1
                                A[a, c] += 1
                                A[a, d] += 1
                                A[b, a] += 1
                                A[b, c] += 1
                                A[b, d] += 1
                                A[c, a] += 1
                                A[c, b] += 1
                                A[c, d] += 1
                                A[d, a] += 1
                                A[d, b] += 1
                                A[d, c] += 1

    # ESCAPE, FIG 4 (c)
    # b = i, c = j
    print('ESCAPE (C)')
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                if b < c and G.has_edge(b, c):
                    for d in G_digraph.successors(b):
                        if not G.has_edge(a, d):
                            if G.has_edge(d, c):
                                A[a, b] += 1
                                A[a, c] += 1
                                A[a, d] += 1
                                A[b, a] += 1
                                A[b, c] += 1
                                A[b, d] += 1
                                A[c, a] += 1
                                A[c, b] += 1
                                A[c, d] += 1
                                A[d, a] += 1
                                A[d, b] += 1
                                A[d, c] += 1

    print('ESCAPE B')
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                if b != c and G_digraph.has_edge(b, c):
                    # assert b < d
                    for d in G_digraph.successors(a):
                        if c < d and d != b and not G.has_edge(d, c):
                            if G_digraph.has_edge(b, d):
                                # print('B1', a, b, c, d)
                                A[a, b] += 1
                                A[a, c] += 1
                                A[a, d] += 1
                                A[b, a] += 1
                                A[b, c] += 1
                                A[b, d] += 1
                                A[c, a] += 1
                                A[c, b] += 1
                                A[c, d] += 1
                                A[d, a] += 1
                                A[d, b] += 1
                                A[d, c] += 1
                        elif d != c and G_digraph.has_edge(d, b) and not G.has_edge(d, c):
                            # print('B2', a, b, c, d)
                            A[a, b] += 1
                            A[a, c] += 1
                            A[a, d] += 1
                            A[b, a] += 1
                            A[b, c] += 1
                            A[b, d] += 1
                            A[c, a] += 1
                            A[c, b] += 1
                            A[c, d] += 1
                            A[d, a] += 1
                            A[d, b] += 1
                            A[d, c] += 1
                elif b != c and G_digraph.has_edge(c, b):
                    for d in G_digraph.successors(a):
                        if d < b and d > c:
                            if G_digraph.has_edge(d, b) and not G.has_edge(c, d):
                                # print('B3', a, b, c, d)
                                A[a, b] += 1
                                A[a, c] += 1
                                A[a, d] += 1
                                A[b, a] += 1
                                A[b, c] += 1
                                A[b, d] += 1
                                A[c, a] += 1
                                A[c, b] += 1
                                A[c, d] += 1
                                A[d, a] += 1
                                A[d, b] += 1
                                A[d, c] += 1

    A /= 1  # overcount correction
    # orbit_count = get_gdv(G)[:, 8]
    # print('')
    # print(nx.to_numpy_array(G))
    # print(A)
    # print(orbit_count)
    # print((np.sum(A, axis=1))/3)
    # assert np.array_equal(np.sum(A, axis=1)/3, orbit_count)
    return A


def compute_AG3_digraph(G):
    G_digraph = to_digraph(G)
    A = init_adjacency(G)

    # ESCAPE, FIG 4 (A)
    # b=i, c=j
    print("out out")
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(b):
                # out out wedge
                if not G.has_edge(a, c):
                    for d in G_digraph.successors(c):
                        if not G.has_edge(d, a) and not G.has_edge(d, b):
                            # print('loop (1 and 8) ', a, b, c)
                            A = __add_count(A, (a, b, c, d))

                    for d in G_digraph.predecessors(c):
                        if d != b and d != a and not G.has_edge(d, b) and not G.has_edge(d, a):
                            # print('loop (2 and 4) ', a, b, c)
                            A = __add_count(A, (a, b, c, d))
                    for d in G_digraph.successors(a):
                        if d < b and not G.has_edge(b, d) and not G.has_edge(c, d):
                            print('loop (5b) ', a, b, c)
                            A = __add_count(A, (a, b, c, d))
                    for d in G_digraph.successors(a):
                        if d > b and not G.has_edge(b, d) and not G.has_edge(c, d):
                            print('loop (7a) ', a, b, c)
                            A = __add_count(A, (a, b, c, d))
                        

    print('in out')
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                # in out wedge
                if b < c and not G.has_edge(b, c):

                    for d in G_digraph.predecessors(c):
                        if d != b and d != a and not G.has_edge(d, b) and not G.has_edge(d, a):
                            # print('loop 6a ', a, b, c)
                            A = __add_count(A, (a, b, c, d))
                    for d in G_digraph.predecessors(b):
                        if d < c and d != a and not G.has_edge(c, d) and not G.has_edge(d, a):
                            # print('loop 3b ', a, b, c)
                            A = __add_count(A, (a, b, c, d))
                    
                    # for d in G_digraph.successors(c):
                    #     if d != b and d != a and not G.has_edge(d, b) and not G.has_edge(d, a):
                    #         # print('loop 5a ', a, b, c)
                    #         A = __add_count(A, (a, b, c, d))
                    # for d in G_digraph.successors(b):
                    #     if d != c and d != a and not G.has_edge(d, c) and not G.has_edge(d, a):
                    #         # print('loop 7b', a, b, c)
                    #         A = __add_count(A, (a, b, c, d))
    
    # print('out in')
    # for a in G_digraph.nodes():
    #     for b in G_digraph.successors(a):
    #         for c in G_digraph.predecessors(b):
    #             if c > a and not G.has_edge(a, c):
    #                 for d in G_digraph.successors(a):
    #                     if d != b and not G.has_edge(b, d) and not G.has_edge(c,d):
    #                         print('loop (3a)', a, b, c)
    #                         A = __add_count(A, (a, b, c, d))
                    
    #                 for d in G_digraph.successors(c):
    #                     if d!=b and not G.has_edge(b, d) and not G.has_edge(a,d):
    #                         print('loop (6b)', a, b, c)
    #                         A = __add_count(A, (a, b, c, d))

    return A


def __add_count(A, nodes):
    for a, b in combinations(nodes, 2):
        A[a, b] += 1
        A[b, a] += 1
    return A

# def compute_AG3_digraph(G):
#     G = nx.convert_node_labels_to_integers(G)
#     G_digraph = nx.DiGraph(nodes=G.nodes())
#     G_digraph.add_edges_from(G.edges())
#     k = G.number_of_nodes()
#     A = np.zeros((k, k))

#     # ESCAPE, FIG 4 (A)
#     # b=i, c=j
#     print('ESCAPE (A)')
#     for a in G_digraph.nodes():
#         for b in G_digraph.successors(a):
#             for c in G_digraph.successors(b):
#                 if not G.has_edge(a, c):
#                     for d in G_digraph.successors(c):
#                         if not G.has_edge(d, a) and not G.has_edge(d, b):
#                             print('loop (A, 1)', a, b, c)
#                             A[a, b] += 1
#                             A[a, c] += 1
#                             A[a, d] += 1
#                             A[b, a] += 1
#                             A[b, c] += 1
#                             A[b, d] += 1
#                             A[c, a] += 1
#                             A[c, b] += 1
#                             A[c, d] += 1
#                             A[d, a] += 1
#                             A[d, b] += 1
#                             A[d, c] += 1
#     # ESCAPE, FIG 4 (b)
#     # b = i, c = j
#     print('(B)')
#     for a in G_digraph.nodes():
#         # b and c are swapped places
#         # can be optimised by having a list of sucessors
#         # get b and c from the list so that b<c and try extend  either b or c
#         for b in G_digraph.successors(a):
#             for c in G_digraph.successors(a):
#                 if b != c and not G.has_edge(b, c):
#                     # for d in G_digraph.predecessors(b):
#                     for d in G.neighbors(b):
#                         if d != a and d != c and not G.has_edge(d, c) and not G.has_edge(d, a):
#                             print('loop (B)', a, b, c)
#                             A[a, b] += 1
#                             A[a, c] += 1
#                             A[a, d] += 1
#                             A[b, a] += 1
#                             A[b, c] += 1
#                             A[b, d] += 1
#                             A[c, a] += 1
#                             A[c, b] += 1
#                             A[c, d] += 1
#                             A[d, a] += 1
#                             A[d, b] += 1
#                             A[d, c] += 1

#     print('(C)')
#     for a in G_digraph.nodes():
#         for b in G_digraph.successors(a):
#             for c in G_digraph.successors(b):
#                 if not G.has_edge(a, c):
#                     for d in G_digraph.predecessors(c):
#                         if d != b and d != a and not G.has_edge(d, b) and not G.has_edge(d, a):
#                             print('loop (C)', a, b, c)
#                             A[a, b] += 1
#                             A[a, c] += 1
#                             A[a, d] += 1
#                             A[b, a] += 1
#                             A[b, c] += 1
#                             A[b, d] += 1
#                             A[c, a] += 1
#                             A[c, b] += 1
#                             A[c, d] += 1
#                             A[d, a] += 1
#                             A[d, b] += 1
#                             A[d, c] += 1

#     A /= 1  # overcount correction
#     # orbit_count = get_gdv(G)[:, 8]
#     # print('')
#     # print(nx.to_numpy_array(G))
#     # print(A)
#     # print(orbit_count)
#     # print((np.sum(A, axis=1))/3)
#     # assert np.array_equal(np.sum(A, axis=1)/3, orbit_count)
#     return A


def compute_AG2_digraph(G):

    A = init_adjacency(G)
    for a, b, c in triangle_iterator(G):
        # print('loop (a)', a, b, c)
        A[a, b] += 1
        A[a, c] += 1
        A[b, a] += 1
        A[b, c] += 1
        A[c, a] += 1
        A[c, b] += 1

    return A


# def triangle_iterator(G):
#     G_digraph = to_digraph(G)
#     for a in G_digraph.nodes():
#         successors = [s for s in G_digraph.successors(a)]
#         for i in range(len(successors)):
#             b = successors[i]
#             for j in range(i+1, len(successors)):
#                 c = successors[j]
#                 if G_digraph.has_edge(b, c):
#                     yield a, b, c

def triangle_iterator(G):
    G_digraph = to_digraph(G)
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(b):
                if G_digraph.has_edge(a, c):
                    yield a, b, c


def path_iterator(G):
    G_digraph = to_digraph(G)
    # in out wedge
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                if b < c and not G.has_edge(b, c):
                    yield b, a, c  # orbit (1, 2, 1)
    # out out wedge
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(b):
                if not G.has_edge(a, c):
                    yield a, b, c  # orbit (1, 2, 1)

    # out in wedge
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.predecessors(b):
                if c > a and not G.has_edge(a, c):
                    yield a, b, c  # orbit (1, 2, 1)


def init_adjacency(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))
    return A


def compute_A1_1(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))
    for x, y, z in path_iterator(G):
        A[x, z] += 1
        A[z, x] += 1
    return A


def compute_A1_2(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))
    for x, y, z in path_iterator(G):
        A[x, y] += 1
        A[z, y] += 1
    return A


def compute_A2_1(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))
    for x, y, z in path_iterator(G):
        A[y, x] += 1
        A[y, z] += 1
    return A


def compute_AG7_digraph_two(G):
    G = nx.convert_node_labels_to_integers(G)
    G_digraph = nx.DiGraph(nodes=G.nodes())
    G_digraph.add_edges_from(G.edges())
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    degrees = G.degree(G.nodes)

    # ESCAPE, FIG 4 (A)
    # b=i, c=j
    print('ESCAPE (A)')
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                if b != c and G.has_edge(b, c):
                    if b < c:
                        for d in G_digraph.successors(a):
                            if d != c and d != b:
                                if G.has_edge(b, d) and c < d and not G.has_edge(c, d):
                                    # print('(a)', a, b, c, d)
                                    A[a, b] += 1
                                    A[a, c] += 1
                                    A[a, d] += 1
                                    A[b, a] += 1
                                    A[b, c] += 1
                                    A[b, d] += 1
                                    A[c, a] += 1
                                    A[c, b] += 1
                                    A[c, d] += 1
                                    A[d, a] += 1
                                    A[d, b] += 1
                                    A[d, c] += 1
                                elif G.has_edge(c, d) and b < d and not G.has_edge(b, d):
                                    # print('(b)', a, b, c, d)
                                    A[a, b] += 1
                                    A[a, c] += 1
                                    A[a, d] += 1
                                    A[b, a] += 1
                                    A[b, c] += 1
                                    A[b, d] += 1
                                    A[c, a] += 1
                                    A[c, b] += 1
                                    A[c, d] += 1
                                    A[d, a] += 1
                                    A[d, b] += 1
                                    A[d, c] += 1

                        # possible optimisation:
                        # instead of choosing the one with the lowest degree
                        # choose the one with the fewest neighbours > a
                        # via binary search.
                        # can the same be achieved by choosing the one with the smallest in degree?
                        if degrees[b] < degrees[c]:
                            z = b
                            y = c
                        else:
                            z = c
                            y = b

                        for d in G.neighbors(z):
                            if d > a and d != y and G.has_edge(y, d) and not G.has_edge(a, d):
                                A[a, b] += 1
                                A[a, c] += 1
                                A[a, d] += 1
                                A[b, a] += 1
                                A[b, c] += 1
                                A[b, d] += 1
                                A[c, a] += 1
                                A[c, b] += 1
                                A[c, d] += 1
                                A[d, a] += 1
                                A[d, b] += 1
                                A[d, c] += 1

    A /= 1  # overcount correction
    # orbit_count = get_gdv(G)[:, 8]
    # print('')
    # print(nx.to_numpy_array(G))
    # print(A)
    # print(orbit_count)
    # print((np.sum(A, axis=1))/3)
    # assert np.array_equal(np.sum(A, axis=1)/3, orbit_count)
    return A


def to_digraph(G):
    G = nx.convert_node_labels_to_integers(G)
    G_digraph = nx.DiGraph(nodes=G.nodes())
    G_digraph.add_edges_from(G.edges())
    return G_digraph


def compute_AG1_digraph(G):
    k = G.number_of_nodes()
    A = np.zeros((k, k))

    for x, y, z in path_iterator(G):
        A[x, y] += 1
        A[y, x] += 1
        A[x, z] += 1
        A[z, x] += 1
        A[y, z] += 1
        A[z, y] += 1
    return A


def compute_AG1_orbit_sum(G):

    k = G.number_of_nodes()
    A = np.zeros((k, k))

    A += compute_A1_1(G)
    A += compute_A1_2(G)
    A += compute_A2_1(G)
    return A

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

    A = A[:, order]
    A = A[order, :]


    n = A.shape[0]
    rows, cols = np.nonzero(A)
    return rows, cols, n

def count(G, adj_type):

    match adj_type:
        case 'A1_1':
            rows, cols, n = format_gradco_input(G)
            if len(rows)>0:
                A_sparse = gradco.count(rows, cols, n, 2)
                return format_gradco_output(A_sparse, n)
            else:
                return np.zeros((n, n))
            # return compute_A1_1(G)
            # return count_all(G)['A1_1']
        case 'A1_2':
            # return compute_A2_1(G).transpose()
            # return count_all(G)['A1_2']
            # return compute_A1_2(G)
            rows, cols, n = format_gradco_input(G)
            if len(rows)>0:
                A_sparse = gradco.count(rows, cols, n, 2)
                return format_gradco_output(A_sparse, n)
            else:
                return np.zeros((n, n))
        case 'A2_1':
            # return compute_A2_1(G)
            return count_all(G)['A1_2'].transpose()
        case 1:
            # return compute_AG1_orbit_sum(G)
            return compute_AG1_digraph(G)
        case 2:
            # return compute_AG2_digraph(G)
            # return count_all(G)['A3_3']
            rows, cols, n = format_gradco_input(G)
            if len(rows)>0:
                A_sparse = gradco.count(rows, cols, n, 2)
                return format_gradco_output(A_sparse, n)
            else:
                return np.zeros((n, n))

        case 'A6_6':
            return compute_A6_6(G)

        case 'A6_7':
            return compute_A6_7(G)

        case 'A7_6':
            return compute_A7_6(G)
        case 3:
            # return compute_AG3(G)
            return compute_AG3_digraph(G)

        case 4:
            return compute_AG4_orbit_sum(G)
        case 5:
            return compute_AG5_orbit_sum(G)
        case 6:
            return compute_AG6_orbit_sum(G)

        case 'A11_10':
            return compute_A11_10(G)
        case 'A10_11':
            return compute_A10_11(G)  # implemented as transpose

        case 'A11_9':
            return compute_A11_9(G)
        case 'A9_11':
            return compute_A9_11(G)  # implemented as transpose

        case 'A10_9':
            return compute_A10_9(G)

        case 'A9_10':
            return compute_A9_10(G)

        case 'A10_10':
            return compute_A10_10(G)


        case 'A12_12':
            return compute_A12_12_fastest(G)
            # return compute_A12_12_c(G)
            # return compute_A12_12_digraph(G)
        case 'A13_12':
            return compute_A13_12(G)
        case 7:
            return compute_AG7_digraph_two(G)
            # return compute_AG7_digraph(G)
            # return compute_AG7(G)
        case 'A12_13':
            return compute_A12_13(G)
        case 'A13_13':
            return compute_A13_13(G)
        case 'A14_14':
            # return compute_A14_14_oriented_in_out(G)
            # return compute_A14_14_oriented_out_out(G)
            A = nx.to_numpy_array(G, dtype=int)
            A = A+A.transpose()
            A[A>0]=1
            n = A.shape[0]
            rows, cols = np.nonzero(A)
            if len(rows)>0:
                # print(rows, cols)
                A_14_14_sparse = gradco.count(rows, cols, n, 2)
                A = np.zeros((n, n))
                if A.shape[1] >0:
                    A[A_14_14_sparse[0,:], A_14_14_sparse[1,:]] = A_14_14_sparse[2,:]
            return A
            # return count_all(G)['A14_14']
        case _:
            ValueError('invalid adjacency type')


def compute_A11_10(G):

    A2_1 = compute_A2_1(G)
    A = - compute_A13_12(G)
    for x, y, z in triangle_iterator(G):

        A[x, y] += A2_1[x, y]
        A[x, z] += A2_1[x, z]

        A[y, x] += A2_1[y, x]
        A[y, z] += A2_1[y, z]

        A[z, x] += A2_1[z, x]
        A[z, y] += A2_1[z, y]

    return A


def compute_A10_10(G):
    A1_2 = compute_A1_2(G)
    A = - compute_A12_13(G)
    for x, y, z in triangle_iterator(G):
        A[x, z] += A1_2[x, y]
        A[z, x] += A1_2[z, y]

        A[x, y] += A1_2[x, z]
        A[y, x] += A1_2[y, z]

        A[y, z] += A1_2[y, x]
        A[z, y] += A1_2[z, x]

    return A


def compute_A10_11(G):
    return compute_A11_10(G).transpose()


def compute_A11_9(G):
    return compute_A9_11(G).transpose()


def compute_A9_11(G):
    A = -compute_A12_13(G)
    A2_2 = compute_AG2_digraph(G)
    for x, y, z in path_iterator(G):
        A[x, y] += A2_2[y, z]
        A[z, y] += A2_2[y, x]
    A = A/2
    return A


def compute_A9_10(G):
    A = - 2 * compute_A12_12(G)
    A2_2 = compute_AG2_digraph(G)
    for x, y, z in path_iterator(G):
        A[x, z] += A2_2[y, z]
        A[z, x] += A2_2[y, x]
    return A


def compute_A10_9(G):
    return compute_A9_10(G).transpose()


def compute_AG6_orbit_sum(G):
    A = init_adjacency(G)
    A += compute_A9_10(G)
    A += compute_A10_9(G)
    A += compute_A9_11(G)
    A += compute_A11_9(G)
    A += compute_A10_10(G)
    A += compute_A10_11(G)
    A += compute_A11_10(G)

    return A


def compute_A6_6(G):

    A = - compute_A9_10(G)
    A1_2 = compute_A1_2(G)
    for x, y, z in path_iterator(G):
        A[x, z] += A1_2[x, y] - 1
        A[z, x] += A1_2[z, y] - 1
    return A


def compute_A6_7(G):

    A = - 2 * compute_A9_11(G)
    A1_2 = compute_A1_2(G)
    for x, y, z in path_iterator(G):
        A[x, y] += A1_2[x, y] - 1
        A[z, y] += A1_2[z, y] - 1
    A /= 2
    return A


def compute_A7_6(G):
    return compute_A6_7(G).transpose()


def compute_AG4_orbit_sum(G):
    A = init_adjacency(G)
    A += compute_A6_6(G)
    A += compute_A6_7(G)
    A += compute_A7_6(G)
    return A


def compute_A8_8_double_hop_equation_based(G):
    A = - 2 * compute_A12_12(G)
    A1_1 = compute_A1_1(G)
    for x, y, z in path_iterator(G):
        A[x, z] += A1_1[x, z] - 1
        A[z, x] += A1_1[z, x] - 1
    A /= 2
    return A


def compute_A8_8_single_hop_equation_based(G):
    A = - 1 * compute_A12_13(G)
    A1_1 = compute_A1_1(G)
    for x, y, z in path_iterator(G):
        A[x, y] += A1_1[x, z] - 1
        A[z, y] += A1_1[z, x] - 1
    return A


def compute_AG5_orbit_sum(G):
    A = init_adjacency(G)
    A += compute_A8_8_single_hop_equation_based(G)
    A += compute_A8_8_double_hop_equation_based(G)
    return A

def compute_A14_14_oriented_out_out(G):

    G_digraph = to_digraph(G)
    A = init_adjacency(G)
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(b):
                if G_digraph.has_edge(a, c):
                    for d in G_digraph.successors(c):
                        if G_digraph.has_edge(a, d) and \
                                G_digraph.has_edge(b, d):
                               A[a, b] += 1
                               A[a, c] += 1
                               A[a, d] += 1
                               A[b, a] += 1
                               A[b, c] += 1
                               A[b, d] += 1
                               A[c, a] += 1
                               A[c, b] += 1
                               A[c, d] += 1
                               A[d, a] += 1
                               A[d, b] += 1
                               A[d, c] += 1
    return A

def compute_A14_14_oriented_in_out(G):

    G_digraph = to_digraph(G)
    A = init_adjacency(G)
    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                if (b!=c) and G_digraph.has_edge(b, c):
                    for d in G_digraph.successors(a):
                        if (d!= c) and (d!=b) and G_digraph.has_edge(b,d) and G_digraph.has_edge(c,d):
                                   A[a, b] += 1
                                   A[a, c] += 1
                                   A[a, d] += 1
                                   A[b, a] += 1
                                   A[b, c] += 1
                                   A[b, d] += 1
                                   A[c, a] += 1
                                   A[c, b] += 1
                                   A[c, d] += 1
                                   A[d, a] += 1
                                   A[d, b] += 1
                                   A[d, c] += 1
    return A

def count_all(G):

    G_digraph = to_digraph(G)
    A14_14 = init_adjacency(G)
    A3_3 = init_adjacency(G)
    A1_1 = init_adjacency(G)
    A1_2 = init_adjacency(G)

    for a in G_digraph.nodes():
        for b in G_digraph.successors(a):
            for c in G_digraph.successors(a):
                # in out wedge
                if (b<c):
                    if G_digraph.has_edge(b, c):
                        A3_3 = __add_count(A3_3, (a, b, c))
                        for d in G_digraph.successors(a):
                            if (c<d) and G_digraph.has_edge(b,d) and G_digraph.has_edge(c,d):
                                A14_14 = __add_count(A14_14, (a, b, c, d))
                    else:
                        A1_1 = __add_count(A1_1, (b, c))
                        A1_2[b, a] +=1
                        A1_2[c, a] +=1

            for c in G_digraph.successors(b):
                # out out wedge
                if not G.has_edge(a, c):
                    A1_1 = __add_count(A1_1, (a, c))
                    A1_2[a, b] +=1
                    A1_2[c, b] +=1

            for c in G_digraph.predecessors(b):
                # out in wedge
                # if c > a and not G.has_edge(a, c):
                # if c < a and not G.has_edge(c, a):
                    A1_1 = __add_count(A1_1, (a, c))
                    A1_2[a, b] +=1
                    A1_2[c, b] +=1
     
    return  {'A1_1': A1_1,
            'A1_2': A1_2,
            'A3_3': A3_3,
            'A14_14': A14_14}


def main():

   
    # G = nx.scale_free_graph(5)
    G = nx.read_edgelist('PPI_biogrid_yeast.edgelist')
    # format_gradco_input(G)
    # return
    compute_AG3_digraph(G)
    return
    G = nx.read_edgelist('COEX7_human_0.01_LCM.edgelist')
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
