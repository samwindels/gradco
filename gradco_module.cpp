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
	Matrix A14_14   = Matrix(n);  // 4-node clique
	

	int b, c, d;

	std::cout<<"BRUTE FORCE"<<std::endl;
	std::cout<<"IN-OUT WEDGES"<<std::endl;
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
						}
					}
					
					for (int k=0; k<G.adj_in[b].size(); k++){
						// predecessors of b
						d = G.adj_in[b][k];
						if (d!=a && !G.has_edge(a, d) && !G.has_edge(c,d)){
							// d -> b <- a -> c, with b < c
							/* std::cout<<"G3 3, a<d<b : "<<a<<' '<<b<<' '<<' '<<c<<' '<<d<<std::endl; */
							A4_4.increment_all_2_all(c, d);
						}
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
				c = G.adj_out[b][j];
				// in-out wedge
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
						/* std::cout<<"G3 1 & 8: "<<a<<' '<<b<<' '<<' '<<c<<' '<<d<<std::endl; */
							A4_4.increment_all_2_all(a, d);
						}
					}

					for (int k=0; k<G.adj_in[c].size(); k++){
						// predecessors of c
						d = G.adj_in[c][k];
						if(d!= b && d != a && !G.has_edge(a, d) && !G.has_edge(b, d)){
							/* std::cout<<"G3 2 & 4: "<<a<<' '<<b<<' '<<c<<' '<<d<<std::endl; */
							A4_4.increment_all_2_all(a, d);
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
						}
					}
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
					/* std::cout<<"out-in "<<a<<' '<<b<<' '<<c<<' '<<d<<std::endl; */
					A1_1.increment_all_2_all(a, c);
					A1_2.increment_from_to(a, b);
					A1_2.increment_from_to(c, b);
				}
			}
		}
	}
	//INFERED  
	std::cout<<"APPLYING REDUNDANCIES"<<std::endl;
	std::cout<<"IN-OUT WEDGES"<<std::endl;
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

					}else{
						// three node path
					
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
					// TODO
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
					//TODO
				}
			}
		}
	}
	

	//FORMAT RESULTS
	std::cout<<"Translating c arrays to numpy arrays"<<std::endl;
	PyObject* A1_1_numpy     = A1_1.to_numpy();
	PyObject* A1_2_numpy     = A1_2.to_numpy();
	PyObject* A3_3_numpy     = A3_3.to_numpy();
	PyObject* A4_4_numpy     = A4_4.to_numpy();
	PyObject* A4_5_numpy     = A4_5.to_numpy();
	PyObject* A4_5_bis_numpy = A4_5_bis.to_numpy();
	PyObject* A5_5_numpy     = A5_5.to_numpy();
	PyObject* A14_14_numpy   = A14_14.to_numpy();
	
	PyObject* tuple = Py_BuildValue("(OOOO)",A1_1_numpy,
						 A1_2_numpy,
						 A3_3_numpy,
						 A4_4_numpy,
						 A4_5_numpy,
						 A4_5_bis_numpy,
						 A5_5_numpy,
						 A14_14_numpy);
	//  Py_BuildValue increases reference count
	Py_DECREF(A1_1_numpy);
	Py_DECREF(A1_2_numpy);
	Py_DECREF(A3_3_numpy);
	Py_DECREF(A4_4_numpy);
	Py_DECREF(A4_5_numpy);
	Py_DECREF(A4_5_bis_numpy);
	Py_DECREF(A5_5_numpy);
	Py_DECREF(A14_14_numpy);

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

