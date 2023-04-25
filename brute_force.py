import argparse
import numpy as np
import uuid
import networkx as nx
import subprocess
import os
from scipy.spatial.distance import squareform
import pandas as pd


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


def compute_A12_12_fastest(G):
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
                    neighbours_connected.append(z)
                else:
                    neighbours_not_connected.append(z)
            for c in neighbours_connected:
                for d in neighbours_not_connected:
                    if G.has_edge(c, d):
                        if c > b and a > d:
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
                        A[c, d] += 1

    A /= 1
    orbit_count = get_gdv(G)[:, 12]
    assert np.array_equal(np.sum(A, axis=1), orbit_count)
    return A


def main():

    for A, integer, str_bit_array in generate_subgraph_permutations(5):
        G = nx.from_numpy_array(A)
        # A12_13 = compute_A12_13(G)
        # A12_12 = compute_A12_12(G)
        # A13_12 = compute_A13_12(G)
        # A13_13 = compute_A13_13(G)
        # A14_14 = compute_A14_14(G)
        # A12_12 = compute_A12_12_fast(G)
        A12_12 = compute_A12_12_fastest(G)


if __name__ == "__main__":
    main()
