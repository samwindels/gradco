import argparse
import numpy as np
import uuid
import networkx as nx
import subprocess
from scipy.spatial.distance import squareform
import os


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


def get_binary_array(integer, array_length):

    str_bit_array = get_little_endian_string(integer)
    str_bit_array = str_bit_array + \
        "".join(["0"]*(array_length-len(str_bit_array)))

    bit_array = [int(bit) for bit in str_bit_array]

    return bit_array, str_bit_array


def get_little_endian_string(integer):
    return format(integer, "b")[::-1]


def get_test_filepath(adj_type):
    return f"generate_tests/orbit_adjacency_tests/test_{adj_type}_orca.py"


def write_tests_A_orbits(orbit_1, orbit_2):
    print(orbit_1, orbit_2)

    orbitcombo2correction = {(1, 1): 1,
                             (1, 2): 1,
                             (2, 1): 2,
                             (10, 10): 1,
                             (9, 10): 2,
                             (10, 9): 1,
                             (9, 11): 1,
                             (10, 11): 1,
                             (11, 9): 1,
                             (11, 10): 2,
                             (12, 12): 1,
                             (12, 13): 2,
                             (13, 12): 2,
                             (13, 13): 1}

    adj_type = f'A{orbit_1}_{orbit_2}'
    fp = get_test_filepath(adj_type)
    correction = orbitcombo2correction[(orbit_1, orbit_2)]
    with open(fp, 'w') as ostr:
        ostr.write("from test.test_helper import matches_orca\n\n\n")
        for A, integer, str_bit_array in generate_subgraph_permutations(5):
            # ORCA tests
            G = nx.from_numpy_array(A)
            counts = get_gdv(G)[:, orbit_1]
            exp_counts = counts * correction
            str_exp_counts = [str(c) for c in exp_counts]

            ostr.write(f"def test_{integer}():\n\n")
            ostr.write(f"    triu = [{', '.join(str_bit_array)}]\n")
            ostr.write(f"    exp_counts = [{', '.join(str_exp_counts)}]\n")
            ostr.write(
                f"    assert matches_orca(triu, '{adj_type}', exp_counts)\n\n\n")


def main():
    # write_tests_A_orbits(1, 1)
    # write_tests_A_orbits(1, 2)
    # write_tests_A_orbits(2, 1)
    # write_tests_A_orbits(11, 10)
    # write_tests_A_orbits(10, 11)
    # write_tests_A_orbits(9, 11)
    # write_tests_A_orbits(9, 10)
    # write_tests_A_orbits(10, 9)
    write_tests_A_orbits(10, 10)
    # write_tests_A_orbits(11, 9)
    # write_tests_A_orbits(12, 12)
    # write_tests_A_orbits(12, 13)
    # write_tests_A_orbits(13, 12)
    # write_tests_A_orbits(13, 13)


if __name__ == "__main__":
    main()
