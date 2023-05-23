import argparse
import numpy as np
import uuid
import networkx as nx
import subprocess
import os
from scipy.spatial.distance import squareform
import pandas as pd
import gradco


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

        command = ['./orca_mac', str(4), edgelist_file, gdv_file]
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


# def compute_AG5(G):
#     A = nx.to_numpy_array(G)
#     AG1 = A @ A

#     # n = A.shape[0]
#     # print('A', A)
#     # triu = gradco.count(A, n, 1)
#     # AG1 = squareform(triu)

#     k = G.number_of_nodes()
#     AG5 = np.zeros((k, k))
#     for a in G.nodes():
#         for b in G.neighbors(a):
#             if b > a:
#                 for c in G.neighbors(b):
#                     if c != a and A[a, c] == 0:
#                         if AG1[a, c] > 1:
#                             AG5[a, b] += (AG1[a, c]) - 1
#                             AG5[b, a] += AG1[a, c] - 1
#                             AG5[a, c] += (AG1[a, c] - 1)/2
#         for b in G.neighbors(a):
#             if b > a:
#                 for c in G.neighbors(a):
#                     if c != b and A[b, c] == 0:
#                         if AG1[b, c] > 1:
#                             AG5[b, c] += ((AG1[b, c]) - 1)/2
#                             # AG5[c, b] += (AG2[b, c]) - 1
#                             # AG5[b, a] += AG2[a, c] - 1
#                             # AG5[a, c] += (AG2[b, c] - 1)/2

#     orbit_count = get_gdv(G)[:, 8]
#     # if np.sum(orbit_count) > 0:
#     print('')
#     print(A)
#     print(AG5)
#     print(orbit_count)
#     print((np.sum(AG5, axis=1)/3))
#     print(AG1)
#     assert np.allclose(np.sum(AG5, axis=1)/3,
#                        orbit_count, atol=1e-1, rtol=1e-1)
#     return AG5

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

                            # # ESCAPE, FIG 4 (b)
                            # # b = blanc, c = i
                            # for a in G_digraph.nodes():
                            #     for b in G_digraph.successors(a):
                            #         for c in G_digraph.successors(a):
                            #             if b != c and G_digraph.has_edge(b, c):
                            #                 for d in G_digraph.predecessors(a):
                            #                     print(a, b, c, d)
                            #                     if not G.has_edge(c, d):
                            #                         if G_digraph.has_edge(d, b):
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

                            # if b < c:
                            # b=i, c=j
                            # print('orbit 13')
                            # for a in G_digraph.nodes():
                            #     for b in G_digraph.successors(a):
                            #         for c in G_digraph.successors(a):
                            #             if b != c and G_digraph.has_edge(b, c):
                            #                 # if b < c:
                            #                 for d in G_digraph.successors(a):
                            #                     if d != c and d != b and not G.has_edge(d, c):
                            #                         if G_digraph.has_edge(b, d) and c < d:
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
                            #                         elif G_digraph.has_edge(d, b):
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

    A /= 1  # overcount correction
    # orbit_count = get_gdv(G)[:, 8]
    # print('')
    # print(nx.to_numpy_array(G))
    # print(A)
    # print(orbit_count)
    # print((np.sum(A, axis=1))/3)
    # assert np.array_equal(np.sum(A, axis=1)/3, orbit_count)
    return A


def count(G, adj_type):

    match adj_type:
        case 'A12_12':
            # return compute_A12_12_fastest(G)
            # return compute_A12_12_c(G)
            return compute_A12_12_digraph(G)
        case 'A13_12':
            return compute_A13_12(G)
        case 3:
            return compute_AG3(G)
        case 7:
            return compute_AG7_digraph(G)
            # return compute_AG7(G)
        case 5:
            return compute_A8_8_digraph(G)
        case 'A12_13':
            return compute_A12_13(G)
        case 'A13_13':
            return compute_A13_13(G)
        case _:
            ValueError('invalid adjacency type')


def main():

    G = nx.read_edgelist('PPI_biogrid_yeast.edgelist')
    # G = nx.read_edgelist('COEX7_human_0.01_LCM.edgelist')
    # compute_A8_8_digraph(G)
    compute_AG7_digraph(G)
    # G = nx.read_edgelist('degenerate_tests/nets/PPI_yeast_degenerate.edgelist')
    # A = nx.to_numpy_array(G, dtype=int)
    # n = A.shape[0]
    # triu_counts = gradco.count(A, n, 2)
    # print(np.sum(triu_counts/3))
    return

    for A, integer, str_bit_array in generate_subgraph_permutations(5):
        G = nx.from_numpy_array(A)
        # compute_A8_8_digraph(G)
        # compute_A12_12_digraph(G)
        # compute_A4_4_G(G)
        # compute_A4_3_double_hop(G)
        # compute_A4_3_single_hop(G)
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
        compute_AG7_digraph(G)


if __name__ == "__main__":
    main()
