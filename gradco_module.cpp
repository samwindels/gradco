/* include python, should be done before standard c librarys */
#define PY_SSIZE_T_CLEAN
/* #define Py_LIMITED_API 3 */
#include <Python.h>

#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

// uncomment to disable assert()
// #define NDEBUG
#include <cassert>

#include <iostream>

#include "directed_graph.hh"
#include "matrix.hh"


static PyObject *gradco_count(PyObject *self, PyObject *args) {


	/* parse input from python */
	int n;
	int graphlet;
	PyArrayObject* rows = NULL;
	PyArrayObject* cols = NULL;
	
	if (!PyArg_ParseTuple(args, "O!O!ii", &PyArray_Type, &rows, &PyArray_Type, &cols, &n, &graphlet))
		return NULL;

	// SANITY CHECKS NUMPY ARRAYS
	// arrays are one dimensional
	assert(PyArray_NDIM(rows)==1);
	assert(PyArray_NDIM(cols)==1);
	
	// arrays are equal length
	assert(PyArray_SIZE(rows)==PyArray_SIZE(cols));

	/* std::cout<<"contiguous"<<PyArray_IS_C_CONTIGUOUS(rows)<<std::endl; */

	DirectedGraph G = DirectedGraph(n, rows, cols);



	// BRUTE FORCE
	Matrix A1_1     = Matrix(n);  // 3-node path, outside orbits
	Matrix A1_2     = Matrix(n);  // 3-node path, outside and middle orbits
	Matrix A3_3     = Matrix(n);  // 3-node triangle
	Matrix A4_4     = Matrix(n);  // 4-node path, outside orbits
	Matrix A4_5     = Matrix(n);  // 4-node path, outside orbit and neighbour
	Matrix A4_5_bis = Matrix(n);  // 4-node path, outside orbit and two hops away 
	Matrix A5_5     = Matrix(n);  // 4-node path, inside orbits 
	Matrix A6_6     = Matrix(n);  // 4-node star, outside orbits 
	Matrix A6_7     = Matrix(n);  // 4-node star, outsite to centre orbits 
	Matrix A8_8     = Matrix(n);  // 4-node cycle, neighbouring nodes 
	Matrix A8_8_bis = Matrix(n);  // 4-node cycle, nodes two hops away 
	Matrix A9_10    = Matrix(n);  // 4-node paw,  
	Matrix A9_11    = Matrix(n);  // 4-node paw,
	Matrix A10_10   = Matrix(n);  // 4-node paw,
	Matrix A10_11   = Matrix(n);  // 4-node paw,
	Matrix A12_12   = Matrix(n);  // 4-node cycle with chord,
	Matrix A12_13   = Matrix(n);  // 4-node cycle with chord,
	Matrix A13_13   = Matrix(n);  // 4-node cycle with chord,
	Matrix A14_14   = Matrix(n);  // 4-node clique
	

	int b, c, d;

	std::cout<<"BRUTE FORCE"<<std::endl;
	std::cout<<"in-out wedges"<<std::endl;
	for (int a = 0; a < n; a++){
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=i+1; j<G.adj_out[a].size(); j++){
				// in-out wedge
				// b <- a -> c, with b < c
				c = G.adj_out[a][j];
				if (G.has_out_edge(b, c)){
					// triangle
					A3_3.increment_all_2_all(a, b, c);
					for (int k=j+1; k<G.adj_out[a].size(); k++){
						d = G.adj_out[a][k];
						if (G.has_out_edge(b, d) && G.has_out_edge(c, d)){
							A14_14.increment_all_2_all(a, b, c, d);
						}
					}
				}else{
					// 3-node path
					/* std::cout<<"in-out"<<a<<' '<<b<<' '<<' '<<c<<std::endl; */
					A1_1.increment_all_2_all(b, c);
					A1_2.increment_from_to(b, a);
					A1_2.increment_from_to(c, a);

					for (int k=0; k<G.adj_in[c].size(); k++){
						// predecessors of c
						d = G.adj_in[c][k];
						if(!G.has_edge(a, d) && !G.has_edge(b, d)){
							// b <- a -> c <- d, with b < c
							/* std::cout<<"G3 6, d<a : "<<a<<' '<<b<<' '<<c<<' '<<d<<std::endl; */
							A4_4.increment_all_2_all(b, d);
							A4_5.increment_from_to(b, a);
							A4_5.increment_from_to(d, c);
							A4_5_bis.increment_from_to(b, c);
							A4_5_bis.increment_from_to(d, a);
							A5_5.increment_all_2_all(a, c);
						}
					}
					
					for (int k=0; k<G.adj_in[b].size(); k++){
						// predecessors of b
						d = G.adj_in[b][k];
						if (d!=a && !G.has_edge(a, d) && !G.has_edge(c,d)){
							// d -> b <- a -> c, with b < c
							/* std::cout<<"G3 3, a<d<b : "<<a<<' '<<b<<' '<<' '<<c<<' '<<d<<std::endl; */
							A4_4.increment_all_2_all(c, d);
							A4_5.increment_from_to(d, b);
							A4_5.increment_from_to(c, a);
							A4_5_bis.increment_from_to(d, a);
							A4_5_bis.increment_from_to(c, b);
							A5_5.increment_all_2_all(b, a);
						}
					}
				}
			}
		}
	}	
	std::cout<<"out-out wedges"<<std::endl;
	for (int a = 0; a < n; a++){
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=0; j<G.adj_out[b].size(); j++){
				c = G.adj_out[b][j];
				// out-out wedge
				// a -> b -> c
				if (! G.has_out_edge(a, c)){
					// 3-node path
					/* std::cout<<"out-out"<<a<<' '<<b<<' '<<' '<<c<<std::endl; */
					A1_1.increment_all_2_all(a, c);
					A1_2.increment_from_to(a, b);
					A1_2.increment_from_to(c, b);

					for (int k=0; k<G.adj_out[c].size(); k++){
						// sucessors of c
						d = G.adj_out[c][k];
						if (!G.has_out_edge(a, d) && !G.has_out_edge(b, d)){
							// a -> b -> c -> d
							A4_4.increment_all_2_all(a, d);
							A4_5.increment_from_to(a, b);
							A4_5.increment_from_to(d, c);
							A4_5_bis.increment_from_to(a, c);
							A4_5_bis.increment_from_to(d, b);
							A5_5.increment_all_2_all(b, c);
						}
					}

					for (int k=0; k<G.adj_in[c].size(); k++){
						// predecessors of c
						d = G.adj_in[c][k];
						if(d!= b && d != a && !G.has_edge(a, d) && !G.has_edge(b, d)){
							/* std::cout<<"G3 2 & 4: "<<a<<' '<<b<<' '<<c<<' '<<d<<std::endl; */
							// a -> b -> c <- d
							A4_4.increment_all_2_all(a, d);
							A4_5.increment_from_to(a, b);
							A4_5.increment_from_to(d, c);
							A4_5_bis.increment_from_to(a, c);
							A4_5_bis.increment_from_to(d, b);
							A5_5.increment_all_2_all(b, c);
						}
					}
					for (int k=0; k<G.adj_out[a].size(); k++){
						// successor of a
						d = G.adj_out[a][k];
						if (d!= b && !G.has_edge(b, d) && !G.has_edge(c, d))
						{	// d <- a -> b -> c
							// c <- b <- a -> d 
							/* std::cout<<"G3 5b, 7a: "<<a<<' '<<b<<' '<<' '<<c<<' '<<d<<std::endl; */
							A4_4.increment_all_2_all(d, c);
							A4_5.increment_from_to(d, a);
							A4_5.increment_from_to(c, b);
							A4_5_bis.increment_from_to(d, b);
							A4_5_bis.increment_from_to(c, a);
							A5_5.increment_all_2_all(a, b);
						}
					}
				}
			}
		}
	}
	std::cout<<"out-in wedges"<<std::endl;
	for (int a = 0; a < n; a++){
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=G.adj_in[b].size()-1; j>-1; j--){
				// in-out wedge
				// a -> b <- c
				c = G.adj_in[b][j];
				if (c <= a){ break; }
				if (! G.has_out_edge(a, c)){
					/* std::cout<<"out-in "<<a<<' '<<b<<' '<<c<<' '<<d<<std::endl; */
					A1_1.increment_all_2_all(a, c);
					A1_2.increment_from_to(a, b);
					A1_2.increment_from_to(c, b);
				}
			}
		}
	}

	//INFERED  
	
	int A3_3_ab, A3_3_ac, A3_3_bc; 
	int A1_2_ab, A1_2_ba, A1_2_ac, A1_2_ca, A1_2_bc, A1_2_cb;
	int A1_2_min1_ab, A1_2_min1_ba, A1_2_min1_ac, A1_2_min1_ca, A1_2_min1_bc, A1_2_min1_cb;

	A10_10.add_matrix_multiple(A14_14, 2);

	std::cout<<"APPLYING REDUNDANCIES"<<std::endl;
	std::cout<<"IN-OUT WEDGES"<<std::endl;
	int a;
	for (int b = 0; b < n; b++){
		if (G.adj_out[b].size() >= 2){
			for (int i=0; i<G.adj_out[b].size(); i++){
				a = G.adj_out[b][i];
				for (int j=i+1; j<G.adj_out[b].size(); j++){
					// in-out wedge
					// a <- b -> c
					c = G.adj_out[b][j];
					if (G.has_out_edge(a, c)){
						
						A3_3_ab = A3_3.get(a,b) - 1;
						A3_3_ac = A3_3.get(a,c) - 1;
						A3_3_bc = A3_3.get(b,c) - 1;

						A1_2_ab = A1_2.get(a, b);
						A1_2_bc = A1_2.get(b, c);
						A1_2_ac = A1_2.get(a, c);
						A1_2_cb = A1_2.get(c, b);
						A1_2_ca = A1_2.get(c, a);
						A1_2_ba = A1_2.get(b, a);

						A12_13.add_scalar(a, b, A3_3_bc);
						A12_13.add_scalar(a, c, A3_3_bc);
						A12_13.add_scalar(b, a, A3_3_ac);
						A12_13.add_scalar(b, c, A3_3_ac);
						A12_13.add_scalar(c, a, A3_3_ab);
						A12_13.add_scalar(c, b, A3_3_ab);

						A10_10.add_scalar(a, b, A1_2_bc - A3_3_ab);
						A10_10.add_scalar(b, a, A1_2_ac - A3_3_ab);
						A10_10.add_scalar(a, c, A1_2_cb - A3_3_ac);
						A10_10.add_scalar(c, a, A1_2_ab - A3_3_ac);
						A10_10.add_scalar(b, c, A1_2_ca - A3_3_bc);
						A10_10.add_scalar(c, b, A1_2_ba - A3_3_bc);
						
						A13_13.add_scalar(a, b, A3_3_ab);
						A13_13.add_scalar(a, c, A3_3_ac);
						A13_13.add_scalar(b, a, A3_3_ab);
						A13_13.add_scalar(b, c, A3_3_bc);
						A13_13.add_scalar(c, a, A3_3_ac);
						A13_13.add_scalar(c, b, A3_3_bc);
						
						A10_11.add_scalar(a, b, A1_2_ab); 
						A10_11.add_scalar(b, a, A1_2_ba); 
						A10_11.add_scalar(a, c, A1_2_ac); 
						A10_11.add_scalar(c, a, A1_2_ca); 
						A10_11.add_scalar(b, c,	A1_2_bc); 
						A10_11.add_scalar(c, b, A1_2_cb); 

					}else{
						/* // three node path */
						A3_3_ab = A3_3.get(a, b);
						A3_3_bc = A3_3.get(b, c);
						A9_11.add_scalar(a, b, A3_3_bc);
						A9_11.add_scalar(c, b, A3_3_ab);

						A6_7.add_scalar(a, b, A1_2.get(a, b) -1);
						A6_7.add_scalar(c, b, A1_2.get(c, b) -1);

					}
				}
			}
		}
	}	
	std::cout<<"OUT-OUT WEDGES"<<std::endl;
	for (int a = 0; a < n; a++){
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=0; j<G.adj_out[b].size(); j++){
				// in-out wedge
				// a -> b -> c
				c = G.adj_out[b][j];
				if (! G.has_out_edge(a, c)){
					A3_3_ab = A3_3.get(a, b);
					A3_3_bc = A3_3.get(b, c);
					A9_11.add_scalar(a, b, A3_3_bc);
					A9_11.add_scalar(c, b, A3_3_ab);
					A6_7.add_scalar(a, b, A1_2.get(a, b) -1);
					A6_7.add_scalar(c, b, A1_2.get(c, b) -1);
				}
			}
		}
	}
	std::cout<<"OUT-IN WEDGES"<<std::endl;
	for (int a = 0; a < n; a++){
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=G.adj_in[b].size()-1; j>-1; j--){
				// in-out wedge
				// a -> b <- c
				c = G.adj_in[b][j];
				if (c <= a){ break; }
				if (! G.has_out_edge(a, c)){
					A3_3_ab = A3_3.get(a, b);
					A3_3_bc = A3_3.get(b, c);
					A9_11.add_scalar(a, b, A3_3_bc);
					A9_11.add_scalar(c, b, A3_3_ab);
					A6_7.add_scalar(a, b, A1_2.get(a, b) -1);
					A6_7.add_scalar(c, b, A1_2.get(c, b) -1);
				}
			}
		}
	}

	// ordering matters !!!
	A12_13.subtract_matrix_multiple(A14_14, 2);
	A13_13.subtract_matrix_multiple(A14_14, 2);
	A10_11.subtract_matrix_multiple(A12_13, 1);
	
	A9_11.subtract_matrix_multiple(A12_13, 1);
	A6_7.subtract_matrix_multiple(A9_11, 1);  // 9_11 is already times 2
	

	//FORMAT RESULTS
	std::cout<<"Translating c arrays to numpy arrays"<<std::endl;
	PyObject* A1_1_numpy     = A1_1.to_numpy();
	PyObject* A1_2_numpy     = A1_2.to_numpy();
	PyObject* A3_3_numpy     = A3_3.to_numpy();
	PyObject* A4_4_numpy     = A4_4.to_numpy();
	PyObject* A4_5_numpy     = A4_5.to_numpy();
	PyObject* A4_5_bis_numpy = A4_5_bis.to_numpy();
	PyObject* A5_5_numpy     = A5_5.to_numpy();
	PyObject* A6_6_numpy     = A6_6.to_numpy();
	PyObject* A6_7_numpy     = A6_7.division_to_numpy(2);   
	PyObject* A8_8_numpy     = A8_8.to_numpy();
	PyObject* A8_8_bis_numpy = A8_8_bis.to_numpy();
	PyObject* A9_10_numpy    = A9_10.to_numpy();
	// correcting only here to avoid iterating over the matrix twice (correction + to_numpy)
	PyObject* A9_11_numpy    = A9_11.division_to_numpy(2);
	PyObject* A10_10_numpy   = A10_10.to_numpy();
	PyObject* A10_11_numpy   = A10_10.to_numpy();
	PyObject* A12_12_numpy   = A12_12.to_numpy();
	PyObject* A12_13_numpy   = A12_13.to_numpy();
	// correcting only here to avoid iterating over the matrix twice (correction + to_numpy)
	PyObject* A13_13_numpy   = A13_13.division_to_numpy(2);  
	PyObject* A14_14_numpy   = A14_14.to_numpy();

	
	PyObject* tuple = Py_BuildValue("(OOOOOOOOOOOOOOOOOOO)", 
					A1_1_numpy,     // 0 Brute force
					A1_2_numpy,     // 1 Brute force
					A3_3_numpy,     // 2 Brute force
					A4_4_numpy,     // 3 Brute force
					A4_5_numpy,     // 4 Brute force
					A4_5_bis_numpy, // 5 -> TODO update to infer 
					A5_5_numpy,     // 6 -> TODO update to infer    
					A6_6_numpy,     // 7 
					A6_7_numpy,     // 8 Inf. (1-hop)
					A8_8_numpy,     // 9
					A8_8_bis_numpy, // 10
					A9_10_numpy,    // 11
					A9_11_numpy,    // 12 Inf. (1-hop)
					A10_10_numpy,   // 13 Inf. (1-hop)
					A10_11_numpy,   // 14 Inf. (1-hop)
					A12_12_numpy,   // 15 Inf. (1-hop)
					A12_13_numpy,   // 16 Inf. (1-hop)
					A13_13_numpy,   // 17 Inf. (1-hop)
					A14_14_numpy);  // 18 Brute force
	
	//  Py_BuildValue increases reference count, need to deref
	for (int i=0; i<18; i++){
		Py_DECREF(PyTuple_GetItem(tuple,i));
	}
	
	return tuple;
	
}


/* Lists the methods available */
static PyMethodDef GradcoMethods[] = {
   /* {name function in python, name function internal, vargs, description} */
    {"count", gradco_count, METH_VARARGS, "counts graphlet adjacency"},
    {NULL, NULL, 0, NULL}  /* Sentinel */
};


/* Describes the module */
static struct PyModuleDef gradco_module = {
    PyModuleDef_HEAD_INIT,
    "gradco",
    "graphlet adjacency counter",
    -1,
    GradcoMethods
};

/* Called at import */
PyMODINIT_FUNC PyInit_gradco(void) {
    import_array();
    return PyModule_Create(&gradco_module);
}

