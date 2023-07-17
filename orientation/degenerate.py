import networkx as nx
import gradco
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random


def order_degenerate(G):
    core_numbers_map = nx.core_number(G)
    nodes = [n for n in G.nodes()]
    core_numbers = np.asarray([core_numbers_map[n] for n in nodes])
    ordering = np.argsort(core_numbers)
    ordered_nodes = [nodes[i] for i in ordering]

    H = nx.DiGraph(nodes=ordered_nodes)
    for n in ordered_nodes:
        for m in G.neighbors(n):
            if not H.has_edge(m, n):
                H.add_edge(n, m)
    return H


def order_degreebased(G):

    nodes = [n for n in G.nodes()]
    degrees = np.asarray([G.degree[n] for n in nodes])
    ordering = np.argsort(degrees)
    ordered_nodes = [nodes[i] for i in ordering]

    H = nx.DiGraph(nodes=ordered_nodes)

    H = nx.DiGraph(nodes=ordered_nodes)
    for n in ordered_nodes:
        for m in G.neighbors(n):
            if not H.has_edge(m, n):
                H.add_edge(n, m)

    return H


def order_random(G):

    nodes = [n for n in G.nodes()]
    random.shuffle(nodes)
    H = nx.DiGraph(nodes=nodes)
    H.add_edges_from(G.edges())
    return H


def read_write_network_to_degenerate(in_fp, out_fp, weighted=None):
    if weighted:
        G = nx.read_weighted_edgelist(in_fp)
    else:
        G = nx.read_edgelist(in_fp)
    H = order_degenerate(G)
    nx.write_edgelist(H, out_fp)


def compare_out_degree_naive_vs_degenerate(in_fp_1, in_fp_2):
    G = nx.read_edgelist(in_fp_1, create_using=nx.DiGraph())
    H = nx.read_edgelist(in_fp_2, create_using=nx.DiGraph())

    G_degrees_map = G.out_degree()
    G_degrees = np.asarray([G_degrees_map[n] for n in G.nodes()])
    H_degrees_map = H.out_degree()
    H_degrees = np.asarray([H_degrees_map[n] for n in H.nodes()])

    # G_degrees = G_degrees[G_degrees != 0]
    # H_degrees = H_degrees[H_degrees != 0]
    # G_degrees = np.log(G_degrees)
    # H_degrees = np.log(H_degrees)
    # G_degrees = G_degrees[G_degrees > 4]
    # H_degrees = H_degrees[H_degrees > 4]

    bins = 1000
    fig, ax = plt.subplots()
    plt.hist(G_degrees, color='lightgreen', bins=bins)
    plt.hist(H_degrees, color='red', bins=bins)
    # plt.plot(G_degrees, color='lightgreen')
    # plt.plot(H_degrees, color='red')
    plt.show()


def plot_degree_distribution(G):

    degree_frequencies = Counter([d for (_, d) in G.degree])
    degrees = sorted(degree_frequencies.keys())
    frequency = [degree_frequencies[d] for d in degrees]

    out_degree_frequencies = Counter([d for (_, d) in G.out_degree])
    out_degrees = sorted(out_degree_frequencies.keys())
    out_frequency = [out_degree_frequencies[d] for d in out_degrees]

    in_degree_frequencies = Counter([d for (_, d) in G.in_degree])
    in_degrees = sorted(in_degree_frequencies.keys())
    in_frequency = [in_degree_frequencies[d] for d in in_degrees]
    print(max(degrees), max(out_degrees), max(in_degrees))
    print(np.median(degrees), np.median(out_degrees), np.median(in_degrees))

    fig, ax = plt.subplots()
    ax = plt.gca()
    s = 10
    a = 0.7
    ax.scatter(degrees, frequency, c='blue', label='degree', s=s, alpha=a)
    ax.scatter(out_degrees, out_frequency, c='red',
               label='out-degree', s=s, alpha=a)
    ax.scatter(in_degrees, in_frequency, c='green',
               label='in-degree', s=s, alpha=a)
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.xlabel("Degree")
    plt.ylabel("No. of nodes (Frequency)")
    plt.title("Degree distribution")
    plt.legend()
    plt.show()


def main():
    # in_fp_1 = 'nets/PPI_biogrid_yeast.edgelist'
    # in_fp_2 = 'nets/PPI_yeast_degenerate.edgelist'

    in_fp_1 = 'nets/human_ppi.txt'
    G = nx.read_edgelist(in_fp_1)
    # G_digraph = order_degenerate(G)
    G_digraph = order_degreebased(G)
    # G_digraph = order_random(G)
    plot_degree_distribution(G_digraph)

    # in_fp_1 = 'nets/COEX7_human_0.01_LCM.edgelist'
    # in_fp_2 = 'nets/COEX_human_degenerate.edgelist'

    # in_fp_1 = 'nets/human_ppi.txt'
    # in_fp_2 = 'nets/PPI_human_degenerate.edgelist'
    # read_write_network_to_degenerate(in_fp_1,
    #                                  in_fp_2)
    # G = nx.read_edgelist(in_fp_1, create_using=nx.DiGraph)
    # G = nx.read_edgelist(in_fp_1, create_using=nx.DiGraph)
    # G_degree = G.out_degree()
    # print(max(G_degree))
    # A = nx.to_numpy_array(G, dtype=float)
    # n = A.shape[0]
    # triu_counts = gradco.count(A, n, 1212)

    # compare_out_degree_naive_vs_degenerate(in_fp_1, in_fp_2)


if __name__ == "__main__":
    main()
