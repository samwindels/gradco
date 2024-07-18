=========================================
GRaphlet-orbit ADjacency COunter (GRADCO)
=========================================

.. image:: https://badge.fury.io/py/gradco.svg
    :target: http://badge.fury.io/py/gradco
.. image:: https://img.shields.io/pypi/dm/gradco.svg?label=PyPI%20downloads)
    :target: https://pypistats.org/packages/gradco
.. image:: https://img.shields.io/badge/DOI-10.48550/arXiv.2405.14194-blue
    :target: https://doi.org/10.48550/arXiv.2405.14194

------------
Introduction
------------

This is our alpha-version of GRADCO, our general purpose counter that can
output graphlet degree vectors (GDVs), edge graphlet degree vectors, graphlet
adjacency matrices, edge orbit adjacency matrices and node orbit adjacency
matrices. GRADCO is part of our submission 'Graphlets correct for the
topological information missed by random walks' (`DOI:10.48550/arXiv.2405.14194
<https://doi.org/10.48550/arXiv.2405.14194>`_), in which we formally define the
topological information that is implicitly captured by random walks in terms of
orbit adjacencies (i.e., the co-occurence of nodes on symmetric positions
within graphlets). We mathematically prove random walks miss various orbit
adjacencies and illustrate that these orbit adjacencies have real-world value
in a multiclass label prediction setting. If you use GRADCO, please cite our
paper.

-----------------
Quick start guide
-----------------

We are working on improving the documentation. For now, we provide the example
code below to illustrate how to use our counter, GRADCO.

.. code-block:: python

    import gradco as gradco
    import networkx as nx
    from scipy.sparse import csr_array
    
    
    def main():
    
        # generate a random graph
        n = 1000
        m = 10
        G = nx.barabasi_albert_graph(n, m, seed=42)
        A = nx.to_scipy_sparse_array(G)
    
        # create GRADCO counter object
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

-------
Roadmap
-------

We forsee the following steps to take GRADCO from alpha to full release:

    - set up a GitHub workflow to automatically compile and test the code
    - set up a GitHub workflow to automatically deploy the code to PyPI
    - add windows to the precompiled wheels
    - add a bug report template
    - add docs
    - upgrade to numpy 2.0

In the future, we plan to add the following features:

    - speed up the counter
    - reduce the memory footprint
    - add larger graphlets

The best way to support our project is to cite our paper. 

