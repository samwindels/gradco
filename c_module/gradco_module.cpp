/* include python, should be done before standard c librarys */
#define PY_SSIZE_T_CLEAN
/* #define Py_LIMITED_API 3 */
#include <Python.h>

#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

// #define NDEBUG  // uncomment to disable assert()
#include <cassert>
#include <iostream>
#include <chrono>

#include "directed_graph.hh"
#include "sparse_matrix.hh"
#include "symmetric_dense_matrix.hh"
#include "dense_matrix.hh"

void __print_execution_time(std::chrono::system_clock::time_point start_time,
			    std::chrono::system_clock::time_point end_time){

    // Calculate the duration
    std::chrono::seconds duration = std::chrono::duration_cast<std::chrono::seconds>(end_time - start_time);

    // Extract minutes and remaining seconds
    std::chrono::minutes minutes = std::chrono::duration_cast<std::chrono::minutes>(duration);
    std::chrono::seconds remaining_seconds = duration - minutes;

    // Output the duration in minutes and seconds
    /* std::cout << "Execution Time: " << minutes.count() << " minutes and " */
    /*           << remaining_seconds.count() << " seconds" << std::endl; */
}

// SINGLE-HOP EQUATIONS, path-based
// depending on the type of wedge (in-out, out-out, out-in) the positon of nodes a, b, c, d is different
// wedge: l - m - r 
// l = left
// m = middle
// r = right

void  __update_A6_7_A9_11(DenseMatrix& A, int l, int m, int r, DenseMatrix& A1_2){
	A.add_scalar(l, m, A1_2.get(l, m) -1);
	A.add_scalar(r, m, A1_2.get(r, m) -1);
}

void __update_A8_8_A12_13(SymmetricDenseMatrix& A, int l, int m, int r, SymmetricDenseMatrix& A1_1){
	int A1_1_lr = A1_1.get(l, r)-1;

	// A is symmetric	
	if (l<m){
		A.add_scalar(l, m, A1_1_lr);
	}
	if(r<m){
		A.add_scalar(r, m, A1_1_lr);
	}
}

void __update_A8_8_A5_5(SymmetricDenseMatrix& A, int l, int m, int r, DenseMatrix& A1_2){
	
	if (l<m){A.add_scalar(l, m, A1_2.get(m, l));}
	if (r<m){A.add_scalar(r, m, A1_2.get(m, r));}
}

void __update_A4_5_A8_8(DenseMatrix& A, int l, int m, int r, DenseMatrix& A1_2){
	A.add_scalar(l, m, A1_2.get(m, r));
	A.add_scalar(r, m, A1_2.get(m, l));
}

void __update_A9_11_A12_13(DenseMatrix& A, int l, int m, int r, SymmetricDenseMatrix& A3_3){
	A.add_scalar(l, m, A3_3.get(m, r));
	A.add_scalar(r, m, A3_3.get(l, m));
}

void __update_A13_13_A14_14(SymmetricDenseMatrix& A, int l, int m, int r, SymmetricDenseMatrix& A3_3){
	int A3_3_lm = A3_3.get(l,m) - 1;
	int A3_3_lr = A3_3.get(l,r) - 1;
	int A3_3_mr = A3_3.get(m,r) - 1;
	A.add_scalar(l, m, A3_3_lm);
	/* A.add_scalar(m, l, A3_3_lm); */
	A.add_scalar(l, r, A3_3_lr);
	/* A.add_scalar(r, l, A3_3_lr); */
	A.add_scalar(m, r, A3_3_mr);
	/* A.add_scalar(r, m, A3_3_mr); */
} 

// SINGLE-HOP EQUATIONS, triangle-based
void __update_A12_13_A14_14(DenseMatrix& A, int l, int m, int r, SymmetricDenseMatrix& A3_3){
	int A3_3_lm = A3_3.get(l,m) - 1;
	int A3_3_lr = A3_3.get(l,r) - 1;
	int A3_3_mr = A3_3.get(m,r) - 1;
	A.add_scalar(l, m, A3_3_mr);
	A.add_scalar(l, r, A3_3_mr);
	A.add_scalar(m, l, A3_3_lr);
	A.add_scalar(m, r, A3_3_lr);
	A.add_scalar(r, l, A3_3_lm);
	A.add_scalar(r, m, A3_3_lm);
}

void __update_A10_10_A12_13(SymmetricDenseMatrix& A, int l, int m, int r, DenseMatrix& A1_2){
	// commented out because A is symmetric
	if (l<m){
		A.add_scalar(l, m, A1_2.get(l, r));
	}
	else{
		A.add_scalar(m, l, A1_2.get(m, r));
	}
	if (l<r){
		A.add_scalar(l, r, A1_2.get(l, m));
	}
	else{
		A.add_scalar(r, l, A1_2.get(r, m));
	}
	if (m<r){
		A.add_scalar(m, r, A1_2.get(m, l));
	}
	else{
		A.add_scalar(r, m, A1_2.get(r, l));
	}
	
		
	/* A.add_scalar(l, m, A1_2.get(l, r)); */
	/* A.add_scalar(m, l, A1_2.get(m, r)); */
	/* A.add_scalar(l, r, A1_2.get(l, m)); */
	/* A.add_scalar(r, l, A1_2.get(r, m)); */
	/* A.add_scalar(m, r, A1_2.get(m, l)); */
	/* A.add_scalar(r, m, A1_2.get(r, l)); */
}

void __update_A10_11_A12_13(DenseMatrix& A, int l, int m, int r, DenseMatrix& A1_2){
	A.add_scalar(l, m, A1_2.get(l, m)); 
	A.add_scalar(l, r, A1_2.get(l, r)); 
	A.add_scalar(m, l, A1_2.get(m, l)); 
	A.add_scalar(m, r, A1_2.get(m, r)); 
	A.add_scalar(r, l, A1_2.get(r, l)); 
	A.add_scalar(r, m, A1_2.get(r, m)); 
}


// DOUBLE-HOP EQUATIONS
// depending on the type of wedge (in-out, out-out, out-in) the positon of nodes a, b, c, d is different
// wedge: l - m - r 
// l = left
// m = middle
// r = right
void __update_A6_6_A9_10(SymmetricDenseMatrix& A, int l, int m, int r, DenseMatrix& A1_2){
	A.add_scalar(l, r, A1_2.get(l, m) -1);
	// commented out because A is symmetric
	/* A.add_scalar(r, l, A1_2.get(r, m) -1); */
}

void __update_A9_10_A12_12(DenseMatrix& A, int l, int m, int r, SymmetricDenseMatrix& A3_3){
	A.add_scalar(l, r, A3_3.get(m, r));
	A.add_scalar(r, l, A3_3.get(l, m));
}


void __update_A8_8bis_A4_5bis(DenseMatrix& A, int l, int m, int r, DenseMatrix& A1_2){

	A.add_scalar(l, r, A1_2.get(m, r));
	A.add_scalar(r, l, A1_2.get(m, l));
}

void __update_A12_12_A8_8bis(SymmetricDenseMatrix& A, int l, int m, int r, SymmetricDenseMatrix& A1_1){
	int A1_1_lr = A1_1.get(l, r)-1;
	A.add_scalar(l, r, A1_1_lr);
	// commented out because A is symmetric
	/* A.add_scalar(r, l, A1_1_lr); */
}


void __count_four_node_path_based(DirectedGraph& G, 
				  int n, 
				  SymmetricDenseMatrix& A1_1, 
				  DenseMatrix& A1_2, 
				  SymmetricDenseMatrix& A3_3, 
				  SymmetricDenseMatrix& A4_4, 
				  DenseMatrix& A4_5_bis, 
				  SymmetricDenseMatrix& A5_5){
	int a, b, c, d;
	/* std::cout<<"BRUTE FORCE FOUR NODE PATHS"<<std::endl; */
	std::chrono::system_clock::time_point init_time = std::chrono::system_clock::now();
	std::chrono::system_clock::time_point start_time = init_time;
	// brute force old	
	for (a = 0; a < n; a++){
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=i+1; j<G.adj_out[a].size(); j++){
				// in-out wedge
				// b <- a -> c, with b < c
				c = G.adj_out[a][j];
				if (G.has_out_edge(b, c)){
					// triangle
					A3_3.increment(a, b);
					A3_3.increment(a, c);
					A3_3.increment(b, c);
				}else{
					// 3-node path
					A1_1.increment(b, c);
					A1_2.increment(b, a);
					A1_2.increment(c, a);

					for (int k=0; k<G.adj_in[c].size(); k++){
						// predecessors of c
						d = G.adj_in[c][k];
						if(!G.has_edge(b, d) && !G.has_edge(a, d)){
							// b <- a -> c <- d, with a < c
							A4_4.increment(b, d);
							A4_5_bis.increment(b,c);
							A4_5_bis.increment(d,a);
							A5_5.increment(a, c);
						}
					}
					
					for (int k=0; k<G.adj_in[b].size(); k++){
						// predecessors of b
						d = G.adj_in[b][k];
						if (d!=c && !G.has_edge(a, d) && !G.has_edge(c,d)){
							// d -> b <- a -> c, with b < c
							A4_4.increment(c, d);
							A4_5_bis.increment(d,a);
							A4_5_bis.increment(c,b);
							A5_5.increment(a, b);
						}
					}
				}
			}
		}
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=0; j<G.adj_out[b].size(); j++){
				c = G.adj_out[b][j];
				// out-out wedge
				// a -> b -> c
				if (! G.has_out_edge(a, c)){
					// 3-node path
					A1_1.increment(a, c);
					A1_2.increment(a, b);
					A1_2.increment(c, b);

					for (int k=0; k<G.adj_out[c].size(); k++){
						// sucessors of c
						d = G.adj_out[c][k];
						if (!G.has_out_edge(a, d) && !G.has_out_edge(b, d)){
							// a -> b -> c -> d
							/* A4_4.increment_all_2_all(a, d); */
							A4_4.increment(a, d);
							A4_5_bis.increment(a,c);
							A4_5_bis.increment(d,b);
							A5_5.increment(b, c);
						}
					}

					for (int k=0; k<G.adj_in[c].size(); k++){
						// predecessors of c
						d = G.adj_in[c][k];
						if(d!= b && d != a && !G.has_edge(a, d) && !G.has_edge(b, d)){
							// a -> b -> c <- d
							A4_4.increment(a, d);
							A4_5_bis.increment(a,c);
							A4_5_bis.increment(d,b);
							A5_5.increment(b, c);
						}
					}
					for (int k=0; k<G.adj_out[a].size(); k++){
						// successor of a
						d = G.adj_out[a][k];
						if (d!= b && !G.has_edge(b, d) && !G.has_edge(c, d))
						{	// d <- a -> b -> c
							// c <- b <- a -> d 
							A4_4.increment(d, c);
							A4_5_bis.increment(d,b);
							A4_5_bis.increment(c,a);
							A5_5.increment(a, b);
						}
					}
				}
			}
		}
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=G.adj_in[b].size()-1; j>-1; j--){
				// out-in wedge
				// a -> b <- c
				c = G.adj_in[b][j];
				if (c <= a){ break; }
				if (! G.has_out_edge(a, c)){
					A1_1.increment(a, c);
					A1_2.increment(a, b);
					A1_2.increment(c, b);

				}
			}
		}
	}
    	std::chrono::system_clock::time_point end_time = std::chrono::system_clock::now();
	__print_execution_time(start_time, end_time);
}

static PyObject *gradco_c_count(PyObject *self, PyObject *args) {


	/* parse input from python */
	int n;
	PyArrayObject* rows = NULL;
	PyArrayObject* cols = NULL;
	
	if (!PyArg_ParseTuple(args, "O!O!i", &PyArray_Type, &rows, &PyArray_Type, &cols, &n))
		return NULL;

	// SANITY CHECKS NUMPY ARRAYS
	// arrays are one dimensional
	assert(PyArray_NDIM(rows)==1);
	assert(PyArray_NDIM(cols)==1);
	
	// arrays are equal length
	assert(PyArray_SIZE(rows)==PyArray_SIZE(cols));

	/* std::cout<<"contiguous"<<PyArray_IS_C_CONTIGUOUS(rows)<<std::endl; */

	/* std::cout<<"BUILDING DIGRAPH"<<std::endl; */
	DirectedGraph G = DirectedGraph(n, rows, cols);
	std::chrono::system_clock::time_point init_time = std::chrono::system_clock::now();
	std::chrono::system_clock::time_point start_time = init_time;
	
	// INITIALIZE MATRICES
	SymmetricDenseMatrix A1_1   = SymmetricDenseMatrix(n);  // 3-node path, outside orbits
	DenseMatrix A1_2     	    = DenseMatrix(n);  // 3-node path, outside and middle orbits
	SymmetricDenseMatrix A3_3   = SymmetricDenseMatrix(n);  // 3-node triangle, inside orbits
	SymmetricDenseMatrix A12_12 = SymmetricDenseMatrix(n);  // 4-node cycle with chord, double hop orbits 
	SymmetricDenseMatrix A14_14 = SymmetricDenseMatrix(n);  // 4-node clique 

	int a, b, c, d;
	bool bc_connected;

	/* std::cout<<"BRUTE FORCE"<<std::endl; */
	for (a = 0; a < n; a++){
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=i+1; j<G.adj_out[a].size(); j++){
				// in-out wedge
				// b <- a -> c, with b < c
				c = G.adj_out[a][j];
				if (G.has_out_edge(b, c)){
					// triangle 
					A3_3.increment(a, b);
					A3_3.increment(a, c);
					A3_3.increment(b, c);
					bc_connected = true;
				}
				else { 
					// 3-node path
					// b <- a -> c, with b < c
					A1_1.increment(b, c);
					A1_2.increment(b, a);
					A1_2.increment(c, a);
					bc_connected = false; 
				}
			
				// case where 'a' might be on orbit 13	
				for (int k=j+1; k<G.adj_out[a].size(); k++){
					d = G.adj_out[a][k];
					if (bc_connected){
						if (G.has_out_edge(b, d)){
							if (G.has_out_edge(c, d)){
								// 4-node clique
								A14_14.increment(a, b);
								A14_14.increment(a, c);
								A14_14.increment(a, d);
								A14_14.increment(b, c);
								A14_14.increment(b, d);
								A14_14.increment(c, d);
							}
							else {
								// 4-node cycle with chord
								// G7 isomorphism 0
								A12_12.increment(c, d);
							}
						} else if (G.has_out_edge(c, d)){
							// 4-node cycle with chord
							// G7 isomorphism 1
							A12_12.increment(b, d);
						}
					} else if (G.has_out_edge(b, d) && G.has_out_edge(c, d)){
						// 4-node cycle with chord
						// G7 isomorphism 2
						A12_12.increment(b, c);
					}
				}
				// case where 'a' might be on orbit 12	
				if (bc_connected){
					for (int k=0; k<G.adj_out[b].size(); k++){
						d = G.adj_out[b][k];
						if ((!G.has_out_edge(a, d) && (G.has_out_edge(c, d) or G.has_out_edge(d,c)))){
						// 4-node cycle with chord
						// G7 isomorphism 3 and 4
							A12_12.increment(a, d);
						}
					}
					for (int k=G.adj_in[b].size()-1; k>-1; k--){
						d = G.adj_in[b][k];
						if (d <=a) {break;}
						if (G.has_out_edge(d, c) && ! G.has_out_edge(a, d)){
							// 4-node cycle with chord
							// G7 isomorphism 5
							A12_12.increment(a, d);
						}
					}
				}
			}
			for (int j=0; j<G.adj_out[b].size(); j++){
				c = G.adj_out[b][j];
				// out-out wedge
				// a -> b -> c
				if (! G.has_out_edge(a, c)){
					// 3-node path
					A1_1.increment(a, c);
					A1_2.increment(a, b);
					A1_2.increment(c, b);
				}
			}
		}
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=G.adj_in[b].size()-1; j>-1; j--){
				// out-in wedge
				// a -> b <- c
				c = G.adj_in[b][j];
				if (c <= a){ break; }
				if (! G.has_out_edge(a, c)){
					A1_1.increment(a, c);
					A1_2.increment(a, b);
					A1_2.increment(c, b);

				}
			}
		}
	}

    	std::chrono::system_clock::time_point end_time = std::chrono::system_clock::now();
	__print_execution_time(start_time, end_time);
	start_time = end_time;
	
	/* std::cout<<"COMPUTING REDUNDANCY MATRICES"<<std::endl; */
	// INITIALIZE REDUNDANCY MATRICES
	/* SparseMatrix A4_5     = SparseMatrix(n);  // 4-node path, outside orbit and neighbour */
	DenseMatrix A4_5     = DenseMatrix(n);  // 4-node path, outside orbit and neighbour
	DenseMatrix A4_5_bis  = DenseMatrix(n);  // 4-node path, outside orbit and node two hops away 
	SymmetricDenseMatrix A5_5 = SymmetricDenseMatrix(n);  // 4-node path, both inside orbits 
	SymmetricDenseMatrix A6_6 = SymmetricDenseMatrix(n);  // 4-node star, outside orbits 
	DenseMatrix A6_7     = DenseMatrix(n);  // 4-node star, outsite to centre orbits 
	SymmetricDenseMatrix A8_8 = SymmetricDenseMatrix(n);  // 4-node cycle, neighbouring nodes 
	SymmetricDenseMatrix A8_8_bis = SymmetricDenseMatrix(n);  // 4-node cycle, nodes two hops away 
	DenseMatrix A9_10    = DenseMatrix(n);  // 4-node paw, 
	DenseMatrix A9_11    = DenseMatrix(n);  // 4-node paw,
	SymmetricDenseMatrix A10_10   = SymmetricDenseMatrix(n);  // 4-node paw,
	DenseMatrix A10_11   = DenseMatrix(n);  // 4-node paw,
	DenseMatrix A12_13   = DenseMatrix(n);  // 4-node cycle with chord,
	SymmetricDenseMatrix A13_13 = SymmetricDenseMatrix(n);  // 4-node cycle with chord,
	
	for (int a = 0; a < n; a++){
		if (G.adj_out[a].size() >= 2){
			for (int i=0; i<G.adj_out[a].size(); i++){
				b = G.adj_out[a][i];
				for (int j=i+1; j<G.adj_out[a].size(); j++){
					// in-out wedge
					// b <- a -> c
					c = G.adj_out[a][j];
					if (G.has_out_edge(b, c)){
						// triangle
						__update_A12_13_A14_14(A12_13, b, a, c, A3_3);
						__update_A10_10_A12_13(A10_10, b, a, c, A1_2);
						__update_A13_13_A14_14(A13_13, b, a, c, A3_3);
						__update_A10_11_A12_13(A10_11, b, a, c, A1_2);
						/* __update_A12_13_A14_14(A14_14, b, a, c, A3_3); */

					}else{
						/* // three node path */
						__update_A4_5_A8_8(A4_5, b, a, c, A1_2);
						__update_A9_11_A12_13(A9_11, b, a, c, A3_3);
 						__update_A6_6_A9_10(A6_6, b, a, c, A1_2);
						__update_A6_7_A9_11(A6_7, b, a, c, A1_2);
						__update_A8_8_A12_13(A8_8, b, a, c, A1_1);
						__update_A8_8bis_A4_5bis(A4_5_bis, b, a, c, A1_2);
						__update_A8_8_A5_5(A5_5, b, a, c, A1_2);
						/* __update_A8_8bis_A4_5bis(A8_8_bis, b, a, c, A1_2); */
						/* __update_A12_12_A8_8bis(A12_12, b, a, c, A1_1); */
						__update_A12_12_A8_8bis(A8_8_bis, b, a, c, A1_1);
						/* __update_A8_8bis_A12_12(A8_8_bis, b, a, c, A1_2); */
						/* __update_A12_12_A8_8bis(A12_12, b, a, c, A1_1); */
						__update_A9_10_A12_12(A9_10, b, a, c, A3_3);
						/* __update_A8_8_A12_13(A12_13, b, a, c, A1_1); */
					}
				}
			}
		}
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=0; j<G.adj_out[b].size(); j++){
				// out-out wedge
				// a -> b -> c
				c = G.adj_out[b][j];
				if (! G.has_out_edge(a, c)){
					__update_A4_5_A8_8(A4_5, a, b, c, A1_2);
					__update_A9_11_A12_13(A9_11, a, b, c, A3_3);
					__update_A6_7_A9_11(A6_7, a, b, c, A1_2);
 					__update_A6_6_A9_10(A6_6, a, b, c, A1_2);
					__update_A8_8_A12_13(A8_8, a, b, c, A1_1);
					__update_A8_8_A5_5(A5_5, a, b, c, A1_2);
					/* __update_A8_8bis_A4_5bis(A8_8_bis, a, b, c, A1_2); */
					/* __update_A12_12_A8_8bis(A12_12, a, b, c, A1_1); */
					__update_A8_8bis_A4_5bis(A4_5_bis, a, b, c, A1_2);
					__update_A12_12_A8_8bis(A8_8_bis, a, b, c, A1_1);
					/* __update_A8_8bis_A12_12(A8_8_bis, a, b, c, A1_2); */
					__update_A9_10_A12_12(A9_10, a, b, c, A3_3);
					/* __update_A8_8_A12_13(A12_13, a, b, c, A1_1); */
				}
			}
		}
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=G.adj_in[b].size()-1; j>-1; j--){
				// in-out wedge
				// a -> b <- c
				c = G.adj_in[b][j];
				if (c <= a){ break; }
				if (! G.has_out_edge(a, c)){
					__update_A4_5_A8_8(A4_5, a, b, c, A1_2);
					__update_A9_11_A12_13(A9_11, a, b, c, A3_3);
					__update_A6_7_A9_11(A6_7, a, b, c, A1_2);
 					__update_A6_6_A9_10(A6_6, a, b, c, A1_2);
					__update_A8_8_A12_13(A8_8, a, b, c, A1_1);
					__update_A8_8_A5_5(A5_5, a, b, c, A1_2);
					/* __update_A8_8bis_A4_5bis(A8_8_bis, a, b, c, A1_2); */
					__update_A8_8bis_A4_5bis(A4_5_bis, a, b, c, A1_2);
					/* /1* __update_A12_12_A8_8bis(A12_12, a, b, c, A1_1); *1/ */
					__update_A12_12_A8_8bis(A8_8_bis, a, b, c, A1_1);
					/* __update_A8_8bis_A12_12(A8_8_bis, a, b, c, A1_2); */
					__update_A9_10_A12_12(A9_10, a, b, c, A3_3);
					/* __update_A8_8_A12_13(A12_13, a, b, c, A1_1); */
				}
			}
		}
	}
    	
	end_time = std::chrono::system_clock::now();
	__print_execution_time(start_time, end_time);
	start_time = end_time;

	/* std::cout<<"COMPUTING ADJACENCY MATRICES"<<std::endl; */
	/* // ordering matters !!! */  	
	// 1. dependend on brute force matrices
	A12_13.subtract_matrix_multiple(A14_14, 2);
	A13_13.subtract_matrix_multiple(A14_14, 2);
	
	A8_8_bis.subtract_matrix_multiple(A12_12, 2);
	A9_10.subtract_matrix_multiple(A12_12, 2);
	
	/* // 2. dependend on infered matrices */
	A8_8.subtract_matrix(A12_13);
	A9_11.subtract_matrix_multiple(A12_13, 1);
	A10_10.subtract_matrix_multiple(A12_13, 1);
	A10_11.subtract_matrix_multiple(A12_13, 1);
	
	A6_6.subtract_matrix_multiple(A9_10, 1);
	A4_5_bis.subtract_matrix_multiple(A8_8_bis, 1);

	/* //3. depend on infered infered matrices */
	A4_5.subtract_matrix_multiple(A8_8, 1);
	A5_5.subtract_matrix_multiple(A8_8, 1);
	A6_7.subtract_matrix_multiple(A9_11, 1);
	
    	end_time = std::chrono::system_clock::now();
	__print_execution_time(start_time, end_time);
	start_time = end_time;

	//FORMAT RESULTS
	/* std::cout<<"CONVERTING TO NUMPY ARRAYS"<<std::endl; */
	PyObject* A1_1_numpy     = A1_1.to_numpy();
	PyObject* A1_2_numpy     = A1_2.to_numpy();
	PyObject* A3_3_numpy     = A3_3.to_numpy();
	
	const npy_intp dims[2] = {3, 0};
	int* np_array_empty = new int[0];
	// empty array. actual counts computed on python side
	PyObject* A4_4_numpy     = PyArray_SimpleNewFromData(2, dims, NPY_INT, np_array_empty);  
	
	PyObject* A4_5_numpy     = A4_5.to_numpy();
	PyObject* A4_5_bis_numpy = A4_5_bis.to_numpy();
	PyObject* A5_5_numpy     = A5_5.to_numpy();
	PyObject* A6_6_numpy     = A6_6.to_numpy();
	PyObject* A6_7_numpy     = A6_7.to_numpy_and_divide(2);   
	PyObject* A8_8_numpy     = A8_8.to_numpy();
	PyObject* A8_8_bis_numpy = A8_8_bis.to_numpy_and_divide(2);
	PyObject* A9_10_numpy    = A9_10.to_numpy();
	// correcting only here to avoid iterating over the matrix twice (correction + to_numpy)
	PyObject* A9_11_numpy    = A9_11.to_numpy_and_divide(2);
	PyObject* A10_10_numpy   = A10_10.to_numpy();
	PyObject* A10_11_numpy   = A10_11.to_numpy();
	PyObject* A12_12_numpy   = A12_12.to_numpy();
	PyObject* A12_13_numpy   = A12_13.to_numpy();
	// correcting only here to avoid iterating over the matrix twice (correction + to_numpy)
	PyObject* A13_13_numpy   = A13_13.to_numpy_and_divide(2);  
	PyObject* A14_14_numpy   = A14_14.to_numpy();

	
	PyObject* tuple = Py_BuildValue("(OOOOOOOOOOOOOOOOOOO)", 
					A1_1_numpy,     // 0  Brute force
					A1_2_numpy,     // 1  Brute force
					A3_3_numpy,     // 2  Brute force
					A4_4_numpy,     // 3   no computed
					A4_5_numpy,     // 4  Inf. (1-hop) 
					A4_5_bis_numpy, // 5  Inf. (2-hop)
					A5_5_numpy,     // 6  Inf. (1-hop)
					A6_6_numpy,     // 7  Inf. (2-hop)
					A6_7_numpy,     // 8  Inf. (1-hop)
					A8_8_numpy,     // 9  Inf. (1-hop)
					A8_8_bis_numpy, // 10 Inf. (2-hop)
					A9_10_numpy,    // 11 Inf. (2-hop)
					A9_11_numpy,    // 12 Inf. (1-hop)
					A10_10_numpy,   // 13 Inf. (1-hop)
					A10_11_numpy,   // 14 Inf. (1-hop)
					A12_12_numpy,   // 15 Inf. (2-hop)
					A12_13_numpy,   // 16 Inf. (1-hop)
					A13_13_numpy,   // 17 Inf. (1-hop)
					A14_14_numpy);  // 18 Brute force
	
	//  Py_BuildValue increases reference count, need to deref
	for (int i=0; i<18; i++){
		Py_DECREF(PyTuple_GetItem(tuple,i));
	}
    	end_time = std::chrono::system_clock::now();
	__print_execution_time(start_time, end_time);
	start_time = end_time;
	/* std::cout<<"TOTAL TIME"<<std::endl; */
	__print_execution_time(init_time, end_time);

	
	return tuple;
	
}



/* Lists the methods available */
static PyMethodDef GradcoMethods[] = {
   /* {name function in python, name function internal, vargs, description} */
    {"gradco_c_count", gradco_c_count, METH_VARARGS, "counts graphlet adjacency"},
    {NULL, NULL, 0, NULL}  /* Sentinel */
};


/* Describes the module */
static struct PyModuleDef gradco_module = {
    PyModuleDef_HEAD_INIT,
    "gradco_c_routines",
    "graphlet adjacency counter",
    -1,
    GradcoMethods
};

/* Called at import */
PyMODINIT_FUNC PyInit_gradco_c_routines(void) {
    import_array();
    return PyModule_Create(&gradco_module);
}

