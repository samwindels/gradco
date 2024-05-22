import gradco as gradco
import numpy as np
import networkx as nx
from scipy.sparse import csr_array


def main():

    n = 1000
    m = 10
    G = nx.barabasi_albert_graph(n, m, seed=42)
    A = nx.to_scipy_sparse_array(G)

    # create our counter object
    counter = gradco.Counter(A)

    # count the orbit adjacency matrices
    counter.count()

    # iterate over the orbit adjacencies
    for hop, o1, o2, A in counter.generate_orbit_adjacencies():
        print("O:", hop, o1, o2)

    # iterate the graphlet adjacencies
    for graphlet, A in enumerate(counter.generate_graphlet_adjacencies()):
        print("GA:", graphlet)

    # get the graphlet degree vectors
    GDV = counter.get_GDVs()

    # get the edge graphlet degree vectors
    eGDV = counter.get_edge_GDVs()

    # get the edge orbit adjacency matrices
    for e, A in enumerate(counter.generate_edge_orbit_adjacencies()):
        print("EA:", e)


if __name__ == "__main__":
    main()
