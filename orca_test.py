import gradco as gradco
import numpy as np
import networkx as nx


def run_orca(G, mode):
    import uuid
    import networkx as nx
    import time
    import subprocess
    import pandas as pd
    import os

    unique_id = uuid.uuid1()
    edgelist_file = 'G_{}.txt'.format(unique_id)
    gdv_file = 'G_{}_gdv_{}.txt'.format(mode, unique_id)

    G = nx.convert_node_labels_to_integers(G)
    with open(edgelist_file, 'w') as ostr:
        ostr.write(f"{G.number_of_nodes()} {G.number_of_edges()}\n")
        for edge in G.edges():
            if edge[0] < edge[1]:
                ostr.write(f"{edge[0]} {edge[1]}\n")

    command = ['./orca_mac', mode, str(4), edgelist_file, gdv_file]
    start_time = time.time()
    subprocess.call(command,
                    # stdout=subprocess.DEVNULL,
                    # stderr=subprocess.DEVNULL,
                    timeout=24*60*60)

    df_counts = pd.read_csv(gdv_file, sep=' ', header=None)
    # cleanup
    os.remove(edgelist_file)
    os.remove(gdv_file)

    return df_counts.values


def main():

    n = 1000
    m = 4
    G = nx.barabasi_albert_graph(n, m, seed=0)
    A = nx.adjacency_matrix(G)
    A = A.toarray()

    counter = gradco.Counter(A)
    counter.count()

    orca_counts = run_orca(G, "node")
    w_counts = counter.get_GDVs()
    for i in range(15):
        print(i, np.sum(orca_counts[:, i] - w_counts[:, i]))

    orca_counts = run_orca(G, "edge")
    w_counts = counter.get_edge_GDVs()

    for i in range(12):
        print(i, np.sum(orca_counts[:, i] - w_counts[:, i]))


if __name__ == "__main__":
    main()
