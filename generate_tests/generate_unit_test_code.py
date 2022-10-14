"""
File: generate_connected_subgraph_vectors.py
Author: sam windels
Email: sam.windels@gmail.com
"""

import argparse
import numpy as np
import uuid
import networkx as nx
import subprocess
import os
from scipy.spatial.distance import squareform
import pandas as pd

def write_leda(net, file_name):
    """ Output the network into LEDA format"""
    vertices = []
    vertex_map = {}
    nb_vertex = 0
    noNeighbours = 0
    for i in net.nodes():
        neighbours = list(net.neighbors(i))
        # if len(neighbours) > 0:
        vertices.append(i)
        vertex_map[i] = nb_vertex
        nb_vertex += 1
        # else:
        #     noNeighbours += 1

    ofile = open(file_name, "w")
    ofile.write("LEDA.GRAPH\nstring\nshort\n-2\n")
    ofile.write("%i\n" % (nb_vertex))

    for vertex in vertices:
        ofile.write("|{%s}|\n" % (vertex))

    adjacent = []
    for i in range(nb_vertex):
        row = []
        for j in range(nb_vertex):
            row.append(0)
        adjacent.append(row)

    nb_edge = 0
    for edge in net.edges():
        ind1 = vertex_map[edge[0]]
        ind2 = vertex_map[edge[1]]
        adjacent[ind1][ind2] = 1
        adjacent[ind2][ind1] = 1
        nb_edge += 1

    ofile.write("%i\n" % (nb_edge))

    count_write = 0
    for i in range(nb_vertex):
        for j in range(i + 1, nb_vertex):
            if adjacent[i][j] == 1:
                ofile.write("%i %i 0 |{}|\n" % (i + 1, j + 1))
                count_write += 1
    # print("edges: ", nb_edge, "actually printed: ", count_write)
    ofile.close()
    # print ("-- %i nodes, %i edges\n" % (nb_vertex, nb_edge))
    # print ("no neighbours: ", noNeighbours)
    return vertices


def get_graphlet_adjacency(G, graphlet):
    
        unique_id = uuid.uuid1()
        edgelist_file ='G_{}'.format(unique_id)
        # H=convert_node_labels_to_integers(G) #node ordering is same as G.nodes()
        H = G
        H.remove_edges_from(nx.selfloop_edges(H)) 

        write_leda(H, edgelist_file)
   
        command = ['./ncount2', '-i', edgelist_file]
        subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # subprocess.call(command)
        L_file = f"{edgelist_file}_{graphlet}.edgelist" 
        L = np.zeros((5,5), dtype=int)
        for line in open(L_file):
            i, j, v = line.strip().split()
            i = int(i)
            j = int(j)
            v = -int(round(float(v) * (graphlet2size[graphlet]-1)))
            if i != j:
                L[i,j] = v
                L[j,i] = v
        os.remove(edgelist_file)
        for i in range(9):
            os.remove(f"{edgelist_file}_{i}.edgelist")
        return L


def get_gdv(G):
    
    try:
        unique_id = uuid.uuid1()
        edgelist_file ='G_{}.txt'.format(unique_id)
        gdv_file ='G_gdv_{}.txt'.format(unique_id)
        # H=convert_node_labels_to_integers(G) #node ordering is same as G.nodes()
        H = G
        H.remove_edges_from(nx.selfloop_edges(H)) 
   
        with open(edgelist_file,'w') as o_stream:
            o_stream.write("{} {}\n".format(H.number_of_nodes(), H.number_of_edges()))
            for line in nx.generate_edgelist(H,data=False):
               o_stream.write("{}\n".format(line))
        
        command = ['./orca', 'node', str(4), edgelist_file, gdv_file]
        # print(" ".join(command))
        subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # subprocess.call(command)
        return np.loadtxt(gdv_file)
    
    finally:
        os.remove(gdv_file)
        os.remove(edgelist_file)


def get_little_endian_string(integer):
    return format(integer, "b")[::-1]

def get_binary_array(integer, array_length):

    str_bit_array = get_little_endian_string(integer)
    str_bit_array = str_bit_array + "".join(["0"]*(array_length-len(str_bit_array)))

    bit_array = [ int(bit) for bit in str_bit_array]
    
    return bit_array, str_bit_array


def generate_subraph_permutations(k):
    
    max_edges = (k*(k-1))/2
    assert max_edges.is_integer()
    max_edges = int(max_edges)
    
    for integer in range(2**max_edges):
        bit_array, str_bit_array = get_binary_array(integer, max_edges) 
     
        A = squareform(bit_array)
        yield A, integer, str_bit_array


def assert_touches_graphlet(gdv, orbits):

    counts = gdv[:, orbits]
    if np.sum(np.sum(counts)) == 0:
        return 0
    print(counts)
    return 1


def main():


    graphlets = range(1, 9)

    graphlet2orbits = [[],
                       [1, 2],
                       [3],
                       [4,5],
                       [6,7],
                       [8],
                       [9,10,11],
                       [12,13],
                       [14]
                      ]


    for graphlet in graphlets:
        print(f"generating tests for graphlet {graphlet}")
        with open(f"generate_tests/tests/test_G{graphlet}_orca.py", 'w') as ostr_orca:
            with open(f"generate_tests/tests/test_G{graphlet}_windels.py", 'w') as ostr_windels:
                
                ostr_orca.write("from test.test_helper import matches_count_orca\n\n\n")
                ostr_windels.write("from test.test_helper import matches_count_windels\n\n\n")

                for A, integer, str_bit_array in generate_subraph_permutations(5):
    
                        # ORCA tests
                        G = nx.from_numpy_matrix(A)
                        gdv = get_gdv(G)
                        counts = np.sum(gdv[:, graphlet2orbits[graphlet]], axis=1)
                        expected_counts_orca = np.asarray(counts * (graphlet2size[graphlet] - 1), dtype=int)
                        str_expected_counts_orca = [str(c) for c in expected_counts_orca]
                        
                        ostr_orca.write(f"def test_{integer}():\n\n")
                        ostr_orca.write(f"    triu = [{', '.join(str_bit_array)}]\n")
                        ostr_orca.write(f"    expected_counts = [{', '.join(str_expected_counts_orca)}]\n")
                        ostr_orca.write(f"    assert matches_count_orca(triu, {graphlet}, expected_counts_orca)\n\n\n")
    
                        # Graphlet adjacency tests
                        AG = get_graphlet_adjacency(G, graphlet)

                        # make sure windels et. al. match orca
                        if not np.array_equal(np.sum(AG, axis=1), expected_counts_orca):
                            print(A)
                            print(np.sum(AG, axis=1), expected_counts_orca)
                            write_leda(G, 'debug.leda')
                        assert np.array_equal(np.sum(AG, axis=1), expected_counts_orca)

                        expected_counts_windels = AG[np.triu_indices(5, 1)]
                        str_expected_counts_windels = [str(c) for c in expected_counts_windels]
                       
                        ostr_windels.write(f"def test_{integer}():\n\n")
                        ostr_windels.write(f"    triu = [{', '.join(str_bit_array)}]\n")
                        ostr_windels.write(f"    expected_counts = [{', '.join(str_expected_counts_windels)}]\n")
                        ostr_windels.write(f"    assert matches_count_windels(triu, {graphlet}, expected_counts)\n\n\n")
    


                # bits_str = ', '.join([str(bit) for bit in bits])
                # ostr.write(f"    A = squareform([{bits_str}])\n")
                # if row == 1:
                #     ostr.write("    assert contains_graphlet(A, graphlet)\n\n")
                # else:
                #     ostr.write("    assert not_contains_graphlet(A, graphlet)\n\n")

    # Three node graphlets
    # records = []
    # for A, integer, str_bit_array in generate_subraph_permutations(3):
    #     G = nx.from_numpy_matrix(A)
    #     gdv = get_gdv(G)

    #     G1 = assert_touches_graphlet(gdv, [1,2])
    #     G2 = assert_touches_graphlet(gdv, [3])
    #     records.append((integer, str_bit_array, G1, G2))
    # df = pd.DataFrame.from_records(data=records, 
    #                                columns=["int","bits", "G1", "G2"],
    #                                index='int')
    # df = df.T
    # df.to_csv("bit_array_to_graphlet_signatures_3nodes.csv")

    # Four node graphlets
    # records = []
    # for A, integer, str_bit_array in generate_subraph_permutations(4):
    #     G = nx.from_numpy_matrix(A)
    #     gdv = get_gdv(G)

        # G3 = assert_touches_graphlet(gdv, [4, 5])
        # G4 = assert_touches_graphlet(gdv, [6, 7])
        # G5 = assert_touches_graphlet(gdv, [8])
        # G6 = assert_touches_graphlet(gdv, [9, 10, 11])
        # G7 = assert_touches_graphlet(gdv, [12, 13])
        # G8 = assert_touches_graphlet(gdv, [14])
        # records.append((integer, str_bit_array, G3, G4, G5, G6, G7, G8))
    
    # df = pd.DataFrame.from_records(data=records, 
        #                            columns=["int","bits", "G3", "G4", "G5", "G6", "G7", "G8"],
        #                            index='int')
    # df = df.T
    # df.to_csv("bit_array_to_graphlet_signatures_4nodes.csv")
    

if __name__ == "__main__":
    graphlet2size =[2, 3, 3, 4, 4, 4, 4, 4, 4]
    assert get_little_endian_string(2) == "01"  # sanity check is little endian
    main()
