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
	Matrix A3_3 = Matrix(n);    // 3-node triangle
	
	Matrix A1_1 = Matrix(n);    // 3-node path, outside orbits
	Matrix A1_2 = Matrix(n);    // 3-node path, outside and midle orbits

	int b, c, d;

	for (int a = 0; a < n; ++a){
		for (int i=0; i<G.adj_out[a].size(); i++)
		{
			b = G.adj_out[a][i];
			for (int j=i+1; j<G.adj_out[a].size(); j++){
				// in-out wedge
				c = G.adj_out[a][j];
				if (G.has_out_edge(b, c)){

					A3_3.increment_all_2_all(a, b, c, d);
					for (int k=j+1; k<G.adj_out[a].size(); k++){
						d = G.adj_out[a][k];
						if (G.has_out_edge(b, d) && G.has_out_edge(c, d)){
							A14_14.increment_all_2_all(a, b, c, d);
						}
					}
				}else{
					// increment A1_1
					// increment A1_2
				}
			}
		}
	}	

	
	// 
	/* Py_DECREF(rows); */
	/* Py_DECREF(cols); */

	// Finish the Python Interpreter
	/* Py_Finalize(); */
	PyObject* A14_14_numpy = A14_14.to_numpy_arrays();
	/* Py_INCREF(A14_14_numpy); */
	return	A14_14_numpy;
	
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

