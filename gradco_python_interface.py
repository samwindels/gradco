import argparse
import numpy as np
import uuid
import networkx as nx
import subprocess
import os
from scipy.spatial.distance import squareform
from scipy.linalg import eigh
import pandas as pd
import gradco_c_routines as gradco
from itertools import combinations
import gradco

def get_gdv(G):
    
    try:
        unique_id = uuid.uuid1()
        edgelist_file ='G_{}.txt'.format(unique_id)
        gdv_file ='G_gdv_{}.txt'.format(unique_id)
        H=nx.convert_node_labels_to_integers(G) #node ordering is same as G.nodes()
        H.remove_edges_from(nx.selfloop_edges(H)) 
   
        with open(edgelist_file,'w') as o_stream:
            o_stream.write("{} {}\n".format(H.number_of_nodes(), H.number_of_edges()))
            for line in nx.generate_edgelist(H,data=False):
               o_stream.write("{}\n".format(line))
               print(line)
        
        command = ['./orca', 'node', str(4), edgelist_file, gdv_file]
        # print(" ".join(command))
        # subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(command)
        return np.loadtxt(gdv_file)
    
    finally:
        os.remove(gdv_file)
        os.remove(edgelist_file)


adj2index = {

            'A1_1': 0,
            'A1_2': 1,
            'A3_3': 2,
            'A4_4': 3,
            'A4_5': 4,
            'A4_5_bis': 5,
            'A5_5': 6,
            'A6_6': 7,
            'A6_7': 8,
            'A8_8': 9,
            'A8_8_bis': 10,
            'A9_10': 11,
            'A9_11': 12,
            'A10_10': 13,
            'A10_11': 14,
            'A12_12': 15,
            'A12_13': 16,
            'A13_13': 17,
            'A14_14': 18
        }

def compute_graphlet_adjacency_1(As_sparse, n, order):

        A = format_gradco_output(As_sparse, 'A1_2', n, order)
        A += A.transpose()  # A2_1
        A += format_gradco_output(As_sparse, 'A1_1', n, order)
        return A

def compute_graphlet_adjacency_2(As_sparse, n, order):

        A = format_gradco_output(As_sparse, 'A3_3', n, order)
        return A

def compute_graphlet_adjacency_3(As_sparse, n, order):
        
        A = format_gradco_output(As_sparse, 'A4_5', n, order)
        A += format_gradco_output(As_sparse, 'A4_5_bis', n, order)
        A += A.transpose()  # A5_4 and 5_4_bis
        A += format_gradco_output(As_sparse, 'A5_5', n, order)
        A += format_gradco_output(As_sparse, 'A4_4', n, order)
        return A

def compute_graphlet_adjacency_4(As_sparse, n, order):

        A = format_gradco_output(As_sparse, 'A6_7', n, order)
        A += A.transpose()  # A7_6
        A += format_gradco_output(As_sparse, 'A6_6', n, order)
        return A

def compute_graphlet_adjacency_5(As_sparse, n, order):

        A = format_gradco_output(As_sparse, 'A8_8', n, order)
        A += format_gradco_output(As_sparse, 'A8_8_bis', n, order)
        return A

def compute_graphlet_adjacency_6(As_sparse, n, order):

        A = format_gradco_output(As_sparse, 'A9_10', n, order)
        A += format_gradco_output(As_sparse, 'A9_11', n, order)
        A += format_gradco_output(As_sparse, 'A10_11', n, order)
        A += A.transpose()
        A += format_gradco_output(As_sparse, 'A10_10', n, order)
        return A

def compute_graphlet_adjacency_7(As_sparse, n, order):

        A = format_gradco_output(As_sparse, 'A12_13', n, order)
        A += A.transpose()
        A += format_gradco_output(As_sparse, 'A12_12', n, order)
        A += format_gradco_output(As_sparse, 'A13_13', n, order)
        return A

def compute_graphlet_adjacency_8(As_sparse, n, order):

        A = format_gradco_output(As_sparse, 'A14_14', n, order)
        return A

def format_gradco_output(As_sparse, adj_type, n, order):
    global adj2index
    A = np.zeros((n, n))
    if A.shape[1] >0:
        A_sparse = As_sparse[adj2index[adj_type]]
        A[A_sparse[0,:], A_sparse[1,:]] = A_sparse[2,:]
        reverse_order = np.argsort(order)
        A = A[reverse_order, :]
        A = A[:, reverse_order]
    return A

def format_gradco_input(G):
    A = nx.to_numpy_array(G, dtype=int)
    A = A+A.transpose()
    A[A>0]=1

    rowsum = np.sum(A, axis=1)
    order = np.argsort(rowsum)

    A = A[order, :]
    A = A[:, order]
    
    n = A.shape[0]
    rows, cols = np.nonzero(A)
    return rows, cols, n, order

def count(G, adj_type):

    rows, cols, n, order = format_gradco_input(G)
    if len(rows) == 0:
        return np.zeros((n, n))
    As_sparse = gradco.count(rows, cols, n)

    match adj_type:
        case 'A1_1':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A1_2':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A2_1':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A3_3':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A4_4':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A4_5':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A4_5_bis':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A5_5':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A6_7':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A6_6':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A8_8':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A9_10':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A9_11':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A10_10':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A10_11':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A12_12':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A12_13':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A13_13':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 'A14_14':
            return format_gradco_output(As_sparse, adj_type, n, order)
        case 1:
            return compute_graphlet_adjacency_1(As_sparse, n, order)
        case 2:
            return compute_graphlet_adjacency_2(As_sparse, n, order)
        case 3:
            return compute_graphlet_adjacency_3(As_sparse, n, order)
        case 4:
            return compute_graphlet_adjacency_4(As_sparse, n, order)
        case 5:
            return compute_graphlet_adjacency_5(As_sparse, n, order)
        case 6:
            return compute_graphlet_adjacency_6(As_sparse, n, order)
        case 7:
            return compute_graphlet_adjacency_7(As_sparse, n, order)
        case 8:
            return compute_graphlet_adjacency_8(As_sparse, n, order)
        case _:
            ValueError('invalid adjacency type')

def normalize_symmetric(A):
    """
        Divide each entry of an adjacency matrix by square root of the
        rowsum and colsum. Implementation assumes M is symmetric.
    """
    D_array=np.sum(A, axis=1)
    D_array=np.power(D_array,0.5) + np.finfo(float).eps
    A = A / D_array[:,None]
    A = A / D_array[None,:]
    return A

def power_iteration(matrix, num_iterations, convergence_threshold=1e-6):
    # Generate a random initial guess for the dominant eigenvector
    n = matrix.shape[0]
    # eigen_vector = np.random.rand(n)
    eigen_vector = np.ones(n)

    for iteration in range(num_iterations):
        # Compute the matrix-vector product
        matrix_times_vector = np.dot(matrix, eigen_vector)

        # Normalize the result to prevent divergence
        eigen_vector = matrix_times_vector / np.linalg.norm(matrix_times_vector)

        # Compute the eigenvalue estimate
        eigen_value = np.dot(np.dot(eigen_vector, matrix), eigen_vector)

        # Check for convergence
        if iteration > 0:
            eigen_value_change = abs(eigen_value - prev_eigen_value)
            if eigen_value_change < convergence_threshold:
                print(f"Poweriteration converged after {iteration} iterations.")
                break

        prev_eigen_value = eigen_value

    return eigen_value, eigen_vector

def compute_eigencentrality(A):

    # check matrix is square
    assert A.shape[0] == A.shape[1]
    A = normalize_symmetric(A)
    n = A.shape[0]
    
    # get the dominant eigen vector with scipy
    # _, eigenvector = eigh(A, subset_by_index=(n-1,n-1))  
    
    # get the dominant eigen vector with numpy
    # _, eigenvectors = np.linalg.eig(A)
    # eigenvector = eigenvectors[:, n-1]
    
    # get the dominant eigen vector via power iteration
    _, eigenvector = power_iteration(A, 300, 1e-6)

    # eigenvector could be rotated, make sure it is non-negative
    if np.sum(eigenvector<=0.0) == n:
        eigenvector = -eigenvector 
    # check centralities are non-negative
    assert np.sum(eigenvector<0.0) == 0
    return eigenvector

def compute_graphlet_eigencentralities(G):

    if G.number_of_edges() == 0:
        raise ValueError("Graph can't be empty")

    eigencentralities = []
    A = nx.to_numpy_array(G, dtype=int)
    # making sure the matrix is undirected
    A = A+A.transpose()
    A[A>0]=1

    # standard symmetrically normalized eigencentrality (e.g., graphlet G0)
    print(0)
    eigencentralities.append(compute_eigencentrality(A))

    # compute orbit adjacencies
    rows, cols, n, order = format_gradco_input(G)
    As_sparse = gradco.count(rows, cols, n)  

    # graphlet eigencentralities 
    print(1)
    A = compute_graphlet_adjacency_1(As_sparse, n, order)
    eigencentralities.append(compute_eigencentrality(A))
    
    print(2)
    A = compute_graphlet_adjacency_2(As_sparse, n, order)
    eigencentralities.append(compute_eigencentrality(A))
    
    print(3)
    A = compute_graphlet_adjacency_3(As_sparse, n, order)
    eigencentralities.append(compute_eigencentrality(A))
    
    print(4)
    A = compute_graphlet_adjacency_4(As_sparse, n, order)
    eigencentralities.append(compute_eigencentrality(A))
    
    print(5)
    A = compute_graphlet_adjacency_5(As_sparse, n, order)
    eigencentralities.append(compute_eigencentrality(A))
            
    print(6)
    A = compute_graphlet_adjacency_6(As_sparse, n, order)
    eigencentralities.append(compute_eigencentrality(A))
    
    print(7)
    A = compute_graphlet_adjacency_7(As_sparse, n, order)
    eigencentralities.append(compute_eigencentrality(A))
            
    print(8)
    A = compute_graphlet_adjacency_8(As_sparse, n, order)
    eigencentralities.append(compute_eigencentrality(A))

    return eigencentralities


def main():

   
    G = nx.scale_free_graph(5000)
    A = nx.to_numpy_array(G, dtype=int)
    

    counter = gradco.Counter(A)
    counter.count()
    for A in counter.generate_graphlet_adjacencies():
        print(A)

    counter.get_graphlet_adjacency(1)
    counter.get_graphlet_adjacency(2)
    counter.get_graphlet_adjacency(3)
    counter.get_graphlet_adjacency(4)
    counter.get_graphlet_adjacency(5)
    counter.get_graphlet_adjacency(6)
    counter.get_graphlet_adjacency(7)
    counter.get_graphlet_adjacency(8)


if __name__ == "__main__":
    main()
