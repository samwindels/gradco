/* include python, should be done before standard c librarys */
#define PY_SSIZE_T_CLEAN
/* #define Py_LIMITED_API 3 */
#include <Python.h>


#include <iostream>
// uncomment to disable assert()
// #define NDEBUG
#include <cassert>


#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

/* #include <boost/python.hpp> */

#include "directed_graph.hh"




/* offsets array to enable fast indexing from row col format to flat array */
/* int *offsets; */

/* int **adj; /1* adjacency as a list of list *1/ */
/* int **adj_mono; /1* monotonically increasing adjacency list of list, only points to nodes with higher index *1/ */ 
/* int *deg; /1* node degrees *1/ */
/* int *deg_mono; /1* number of neighbours witht a higher index *1/ */

/* void init_adjacency(PyArrayObject *A, int n){ */

/* 	/1* list of list representation of our network. Symmetric, i.e., no ordering assumed *1/ */

/* 	int degree; */
/* 	int* buffer = (int*)calloc(n, sizeof(int)); */
/* 	int i,j,d; */

/* 	for(i=0; i<n; ++i){ */
		
/* 		degree = 0; */

/* 		/1* count no. neighbours + keep track of them *1/ */
/* 		for(j=0; j<n; ++j){ */
/* 			if (i==j) continue; */
/* 			if (*(int*)PyArray_GETPTR2(A, i, j)){ */
/* 			       buffer[degree] = j; */
/* 			       degree++; */	
				
/* 			} */
/* 		} */	    
/* 		/1* store degree *1/ */
/* 		deg[i] = degree; */
		
/* 		/1* copy neighbours list from buffer*/ 
/* 		int* neighbours_i = (int*)calloc(degree, sizeof(int)); */
/* 		for(d=0; d<degree; d++){ */
/* 			neighbours_i[d] = buffer[d]; */
/* 		} */
/* 		adj[i] = neighbours_i; */
/* 	} */	    
/* } */

/* void init_monotonic_adjacency(PyArrayObject *A, int n, int **adj_mono, int *deg_mono){ */

/* 	/1* Linked list representation of our network. We assume an ordering: for a given *1/ */
/* 	/1* node, we consider as its neighbours only those nodes that have a higher index. *1/ */
/* 	/1* i.e., we only consider the upper triangle of the adjacency matrix. This avoids *1/ */
/* 	/1* overcountingi counting G2 and G8. *1/ */


/* 	int degree; */
/* 	int* buffer = (int*)calloc(n, sizeof(int)); */
/* 	int i,j,d; */

/* 	for(i=0; i<n; ++i){ */
		
/* 		degree = 0; */

/* 		/1* count no. neighbours + keep track of them *1/ */ 
/* 		for(j=i+1; j<n; ++j){ */
/* 			if (*(int*)PyArray_GETPTR2(A, i, j)){ */
/* 			       buffer[degree] = j; */
/* 			       degree++; */	
				
/* 			} */
/* 		} */	    
/* 		/1* store degree *1/ */
/* 		deg_mono[i] = degree; */
		
/* 		/1* copy neighbours list from buffer*/ 
/* 		int* neighbours_i = (int*)calloc(degree, sizeof(int)); */
/* 		for(d=0; d<degree; d++){ */
/* 			neighbours_i[d] = buffer[d]; */
/* 		} */
/* 		adj_mono[i] = neighbours_i; */
/* 	} */	    
/* } */



static PyObject *gradco_count(PyObject *self, PyObject *args) {
	
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
	/* return NULL; */

	/* return rows; */

	/* init offsets array. */
	/* enables fast indexing from row col format to flat array */
	/* offsets = malloc((n-1) * sizeof(*offsets)); /1* Memory allocation *1/ */
	/* if (!offsets) { */  
    	   /* printf( "memory allocation 'degrees' failed\n" ); */
    	   /* exit(-1); */
	/* } */
	/* int incumbent = -n; */
	/* for(int i=0; i<(n-1); i++){ */
	/* 	offsets[i] = incumbent + n-i -1; */ 
	/* 	incumbent = offsets[i]; */
	/* } */

	/* /1* init monotonic adjacency linked list representation *1/ */
	/* /1* memory allocation *1/ */
	/* deg_mono = malloc(n * sizeof(*deg_mono)); /1* Memory allocation *1/ */
	/* if (!deg_mono) { */  
    	   /* printf( "memory allocation 'deg_mono' failed\n" ); */
    	   /* exit(-1); */
	/* } */
	/* adj_mono = malloc( sizeof(adj_mono) * n); /1* Memory allocation *1/ */
    	/* if( !adj_mono ) */
    	/* { */
    	   /* printf( "memory allocation 'adj_mono' failed\n" ); */
    	   /* exit(-1); */
    	/* } */
	/* init_monotonic_adjacency(A, n, adj_mono, deg_mono); */
	
	/* /1* init adjacency linked list representation *1/ */
	/* deg = malloc(n * sizeof(*deg)); /1* Memory allocation *1/ */
	/* if (!deg) { */  
    	   /* printf( "memory allocation 'deg' failed\n" ); */
    	   /* exit(-1); */
	/* } */
	/* adj= malloc( sizeof(adj) * n); /1* Memory allocation *1/ */
    	/* if( !adj) */
    	/* { */
    	   /* printf( "memory allocation 'adj' failed\n" ); */
    	   /* exit(-1); */
    	/* } */
	/* init_adjacency(A, n); */
	
	/* run counter depending on graphlet*/
	/* printf( "hoot \n" ); */
	/* switch(graphlet) { */
	/*    /1* case 1: *1/ */
	/* 	/1* return count_G1(A, n); *1/ */
	/*    case 2: */
	/*    	return count_G2(A, n); */
	/*    case 3: */
	/*    	return count_G3(A, n); */
	/*    /1* case 4: *1/ */
	/* 	/1* return count_G4(A, n); *1/ */
	/*    /1* case 5: *1/ */
	/* 	/1* return count_G5(A, n); *1/ */
	/*    case 7: */
	/* 	return count_G7(A, n); */
	/*    /1* case 8  : *1/ */
	/*    /1* 	return count_G8(A, n); *1/ */
	/*    case 1212: */
	/* 	return count_A12_12(A, n); */
	/*    default : */ 
    	   	/* printf( "choose a graphlet in range [1,8] \n" ); */
    	   	/* exit(-1); */
	/* } */

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

