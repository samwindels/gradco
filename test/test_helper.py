import gradco
import numpy as np
import networkx as nx
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import inspect
from gradco_python_interface import count

DEBUG = True
# DEBUG = False


def matches_count_windels(triu, graphlet, expected_counts):

    print(inspect.stack()[1].function)  # print name of the test
    A = squareform(triu)
    G = nx.from_numpy_array(A)
    # A_orbit = count(G, graphlet)
    AG = count(G, graphlet)
    # print(A)
    # print(AG)
    triu_counts = squareform(AG)
    # counts = np.sum(A_orbit, axis=1)

    # A = squareform(triu)
    # n = A.shape[0]
    # triu_counts = gradco.count(A, n, graphlet)
    # print(triu_counts)
    outcome = np.array_equal(triu_counts, expected_counts)
    if outcome:
        if np.sum(triu_counts<0)>0:
            outcome = False

    if DEBUG and outcome is False:
        print(inspect.stack()[1].function)  # print name of the test
        n = AG.shape[0]
        AG = squareform(triu_counts)
        AG_expected = squareform(expected_counts)
        diff = AG - AG_expected
        print(f"\n failed test_G{graphlet}: {inspect.stack()[1][3]}")
        print(f"\n{A=}")
        print(f"\n{AG=}")
        print(f"\n{AG_expected=}")
        print(f"\n{diff}")

        node_counts = np.sum(AG, axis=1)
        node_counts_expected = np.sum(AG_expected, axis=1)

        letters = ['a', 'b', 'c', 'd', 'e']
        labels = [
            # f"i: C={node_counts[i]} EC={node_counts_expected[i]}" for i in range(n)]
            f"{i}:" for i in range(n)]

        node_diff = node_counts - node_counts_expected
        colors = []
        for i in range(n):
            if node_diff[i] == 0:
                colors.append('g')
            else:
                colors.append('r')

        labels = dict(zip(range(n), labels))
        G = nx.from_numpy_array(A)
        pos = nx.spring_layout(G)
        edge_color = []
        for edge in G.edges():
            i, j = edge
            if AG[i, j] == AG_expected[i, j]:
                edge_color.append('g')
            else:
                edge_color.append('r')
        nx.draw(G, labels=labels, node_color=colors,
                pos=pos, edge_color=edge_color)

        edge_labels = {}
        for edge in G.edges():
            i, j = edge
            label = f"C: {AG[i,j]}, E:{AG_expected[i,j]}"
            edge_labels[edge] = label

        ax = plt.gca()
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
        plt.draw()
        plt.show()
    return outcome


def matches_orca(triu, adj_type, expected_counts):
    print(inspect.stack()[1].function)  # print name of the test
    A = squareform(triu)
    G = nx.from_numpy_array(A)
    A_orbit = count(G, adj_type)
    counts = np.sum(A_orbit, axis=1)
    outcome = np.array_equal(counts, expected_counts)
    if outcome:
        if np.sum(np.asarray(A_orbit)<0)>0:
            print('CONTAINS NEGATIVES')
            outcome = False

    if DEBUG and outcome is False:
        print(f"\n failed test_G{adj_type}: {inspect.stack()[1][3]}")
        print(f"\n{A=}")
        print(f"\n{A_orbit=}")
        print(f"\n{counts=}")
        print(f"\n{expected_counts=}")
        n = A.shape[0]

        labels = [
            f"{i} C={counts[i]} EC={expected_counts[i]}" for i in range(n)]

        diff = counts - expected_counts
        colors = []
        for i in range(n):
            if diff[i] == 0:
                colors.append('g')
            else:
                colors.append('r')

        labels = dict(zip(range(n), labels))
        G = nx.from_numpy_array(A)
        nx.draw(G, labels=labels, node_color=colors)
        plt.draw()
        plt.show()
    return outcome


# def outputs_expected_count_orca(triu, graphlet, expected_counts):
#     A = squareform(triu)
#     n = A.shape[0]
#     triu_counts = gradco.count(A, n, graphlet)
#     AG = squareform(triu_counts)
#     counts = np.sum(AG, axis=0)
#     outcome = np.array_equal(counts, expected_counts)

#     if DEBUG and outcome is False:
#         print(f"\n failed test_G{graphlet}: {inspect.stack()[1][3]}")
#         print(f"\n{A=}")
#         print(f"\n{AG=}")
#         print(f"\n{counts=}")
#         print(f"\n{expected_counts=}")

#         labels = [
#             f"{i} C={counts[i]} EC={expected_counts[i]}" for i in range(n)]

#         diff = counts - expected_counts
#         colors = []
#         for i in range(n):
#             if diff[i] == 0:
#                 colors.append('g')
#             else:
#                 colors.append('r')

#         labels = dict(zip(range(n), labels))
#         G = nx.from_numpy_array(A)
#         nx.draw(G, labels=labels, node_color=colors)
#         plt.draw()
#         plt.show()
#     return outcome
