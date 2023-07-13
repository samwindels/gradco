/* include python, should be done before standard c librarys */
#define PY_SSIZE_T_CLEAN
/* #define Py_LIMITED_API 3 */
#include <Python.h>


#include <iostream>
// uncomment to disable assert()
// #define NDEBUG
#include <cassert>

#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

/* #include <boost/python.hpp> */

#include "directed_graph.hh"

static PyObject *gradco_count(PyObject *self, PyObject *args) {


	import_array();

	
	/* parse input from python */
	int n;
	int graphlet;
	/* PyArrayObject *A = NULL; */
	/* if (!PyArg_ParseTuple(args, "O!ii", &PyArray_Type, &A, &n, &graphlet)) */
	/* 	return NULL; */
	/* PyArrayObject *rows = NULL; */
	/* PyArrayObject *cols = NULL; */
	PyArrayObject* rows = NULL;
	PyArrayObject* cols = NULL;
	if (!PyArg_ParseTuple(args, "O!O!ii", &PyArray_Type, &rows, &PyArray_Type, &cols, &n, &graphlet))
		return NULL;
	std::cout<<"contiguous"<<PyArray_IS_C_CONTIGUOUS(rows)<<std::endl;
    	std::cout<<"size"<<PyArray_SIZE(rows)<<std::endl;

    	NpyIter* iter;
    	NpyIter_IterNextFunc *iternext;
    	char** dataptr;
    	npy_intp* strideptr,* innersizeptr;


    	iter = NpyIter_New(rows, NPY_ITER_READONLY, NPY_KEEPORDER, NPY_NO_CASTING, NULL);
	/* std::cout<<"done done"<<std::endl; */
    	std::cout<<*(rows->dimensions)<<std::endl;
	Py_INCREF(rows);
	DirectedGraph(rows, cols);
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

