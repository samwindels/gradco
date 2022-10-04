    
import gradco
import ctypes
import numpy as np
import networkx as nx
from scipy.spatial.distance import squareform
import uuid
import subprocess
import os
from scipy.spatial.distance import squareform
import pandas as pd


def contains_graphlet(A, graphlet):
    n = A.shape[0]
    triu = gradco.count(A, n, graphlet)
    AG = squareform(triu)
    print(A)
    print(AG)
    return np.array_equal(np.ones((n)), triu)

def test_graphlet_4():

    graphlet = 4

    A = squareform([0, 0, 0, 0, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 0, 0, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 0, 0, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 0, 0, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 1, 0, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 1, 0, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 1, 0, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 1, 0, 0, 0])
    assert contains_graphlet(A, graphlet)

    A = squareform([0, 0, 0, 1, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 0, 1, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 0, 1, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 0, 1, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 1, 1, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 1, 1, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 1, 1, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 1, 1, 0, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 0, 0, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 0, 0, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 0, 0, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 0, 0, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 1, 0, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 1, 0, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 1, 0, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 1, 0, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 0, 1, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 0, 1, 1, 0])
    assert contains_graphlet(A, graphlet)

    A = squareform([0, 1, 0, 1, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 0, 1, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 1, 1, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 1, 1, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 1, 1, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 1, 1, 1, 0])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 0, 0, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 0, 0, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 0, 0, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 0, 0, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 1, 0, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 1, 0, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 1, 0, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 1, 0, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 0, 1, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 0, 1, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 0, 1, 0, 1])
    assert contains_graphlet(A, graphlet)

    A = squareform([1, 1, 0, 1, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 1, 1, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 1, 1, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 1, 1, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 1, 1, 0, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 0, 0, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 0, 0, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 0, 0, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 0, 0, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 1, 0, 1, 1])
    assert contains_graphlet(A, graphlet)

    A = squareform([1, 0, 1, 0, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 1, 0, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 1, 0, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 0, 1, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 0, 1, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 0, 1, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 0, 1, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 0, 1, 1, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 0, 1, 1, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([0, 1, 1, 1, 1, 1])
    assert not contains_graphlet(A, graphlet)

    A = squareform([1, 1, 1, 1, 1, 1])
    assert not contains_graphlet(A, graphlet)

