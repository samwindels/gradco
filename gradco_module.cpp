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
	Matrix A14_14 = Matrix(n);  // 4-node clique
	Matrix A3_3   = Matrix(n);  // 3-node triangle
	
	Matrix A1_1   = Matrix(n);  // 3-node path, outside orbits
	Matrix A1_2   = Matrix(n);  // 3-node path, outside and midle orbits

	int b, c, d;

	std::cout<<"BRUTE FORCE"<<std::endl;
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

						A3_3.increment_all_2_all(a, b, c);
						for (int k=j+1; k<G.adj_out[a].size(); k++){
							d = G.adj_out[a][k];
							if (G.has_out_edge(b, d) && G.has_out_edge(c, d)){
								A14_14.increment_all_2_all(a, b, c, d);
							}
						}
					}else{
						std::cout<<"in-out"<<a<<' '<<b<<' '<<' '<<c<<std::endl;
						A1_1.increment_all_2_all(b, c);
						A1_2.increment_from_to(b, a);
						A1_2.increment_from_to(c, a);
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
					std::cout<<"out-out"<<a<<' '<<b<<' '<<' '<<c<<std::endl;
					A1_1.increment_all_2_all(a, c);
					A1_2.increment_from_to(a, b);
					A1_2.increment_from_to(c, b);
				}
			}
		}
	}
	std::cout<<"OUT-IN WEDGES"<<std::endl;
	for (int a = 0; a < n; a++){
		for (int i=0; i<G.adj_out[a].size(); i++){
			b = G.adj_out[a][i];
			for (int j=0; j<G.adj_in[b].size(); j++){
				// in-out wedge
				// a -> b <- c
				c = G.adj_in[b][j];
				if (c > a){
					if (! G.has_out_edge(a, c)){
						std::cout<<"out-in"<<a<<' '<<b<<' '<<' '<<c<<std::endl;
						A1_1.increment_all_2_all(a, c);
						A1_2.increment_from_to(a, b);
						A1_2.increment_from_to(c, b);
					}
				}
			}
		}
	}

	// 
	/* Py_DECREF(rows); */
	/* Py_DECREF(cols); */
	/* Py_INCREF(A14_14_numpy); */

	// Finish the Python Interpreter
	/* Py_Finalize(); */
	std::cout<<"translating to numpy"<<std::endl;
	/* return A14_14.to_numpy_arrays(); */
	/* return A3_3.to_numpy_arrays(); */
	/* return A1_1.to_numpy_arrays(); */
	return A1_2.to_numpy_arrays();
	
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

