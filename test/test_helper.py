import gradco
import numpy as np
import networkx as nx
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import inspect

DEBUG = True


def matches_count_windels(triu, graphlet, expected_counts):
    A = squareform(triu)
    n = A.shape[0] 
    triu_counts = gradco.count(A, n, graphlet)
    outcome = np.array_equal(triu_counts, expected_counts)

    if DEBUG and outcome is False:
        AG = squareform(triu_counts)
        AG_expected = squareform(expected_counts)
        diff = AG - AG_expected 
        print(f"\n failed test_G{graphlet}: {inspect.stack()[1][3]}")
        print(f"\n{A=}")
        print(f"\n{AG=}")
        print(f"\n{AG_expected=}")

        # labels = [f"{i} C={counts[i]} EC={expected_counts[i]}" for i in range(n) ]  

        # diff = counts - expected_counts
        # colors = [] 
        # for i in range(n):
        #     if diff[i] == 0:
        #         colors.append('g')
        #     else:
        #         colors.append('r')

        # labels = dict(zip(range(n), labels))
        G = nx.from_numpy_matrix(A)
        nx.draw(G)
        plt.draw()
        plt.show()
    return outcome


def outputs_expected_count_orca(triu, graphlet, expected_counts):
    A = squareform(triu)
    n = A.shape[0] 
    triu_counts = gradco.count(A, n, graphlet)
    AG = squareform(triu_counts)
    counts = np.sum(AG, axis=0)
    outcome = np.array_equal(counts, expected_counts)

    if DEBUG and outcome is False:
        print(f"\n failed test_G{graphlet}: {inspect.stack()[1][3]}")
        print(f"\n{A=}")
        print(f"\n{AG=}")
        print(f"\n{counts=}")
        print(f"\n{expected_counts=}")

        labels = [f"{i} C={counts[i]} EC={expected_counts[i]}" for i in range(n) ]  

        diff = counts - expected_counts
        colors = [] 
        for i in range(n):
            if diff[i] == 0:
                colors.append('g')
            else:
                colors.append('r')

        labels = dict(zip(range(n), labels))
        G = nx.from_numpy_matrix(A)
        nx.draw(G, labels=labels, node_color=colors)
        plt.draw()
        plt.show()
    return outcome
