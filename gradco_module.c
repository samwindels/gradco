/* include python, should be done before standard c librarys */
#define PY_SSIZE_T_CLEAN
#include <Python.h>
/* #define PY_ARRAY_UNIQUE_SYMBOL cool_ARRAY_API */
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>



/* offsets array to enable fast indexing from row col format to flat array */
int *offsets;

int **adj; /* adjacency as a list of list */
int **adj_mono; /* monotonically increasing adjacency list of list, only points to nodes with higher index */ 
int *deg; /* node degrees */
int *deg_mono; /* number of neighbours witht a higher index */

void init_adjacency(PyArrayObject *A, int n){

	/* list of list representation of our network. Symmetric, i.e., no ordering assumed */

	int degree;
	int* buffer = (int*)calloc(n, sizeof(int));
	int i,j,d;

	for(i=0; i<n; ++i){
		
		degree = 0;

		/* count no. neighbours + keep track of them */
		for(j=0; j<n; ++j){
			if (i==j) continue;
			if (*(int*)PyArray_GETPTR2(A, i, j)){
			       buffer[degree] = j;
			       degree++;	
				
			}
		}	    
		/* store degree */
		deg[i] = degree;
		
		/* copy neighbours list from buffer*/
		int* neighbours_i = (int*)calloc(degree, sizeof(int));
		for(d=0; d<degree; d++){
			neighbours_i[d] = buffer[d];
		}
		adj[i] = neighbours_i;
	}	    
}

void init_monotonic_adjacency(PyArrayObject *A, int n, int **adj_mono, int *deg_mono){

	/* Linked list representation of our network. We assume an ordering: for a given */
	/* node, we consider as its neighbours only those nodes that have a higher index. */
	/* i.e., we only consider the upper triangle of the adjacency matrix. This avoids */
	/* overcountingi counting G2 and G8. */


	int degree;
	int* buffer = (int*)calloc(n, sizeof(int));
	int i,j,d;

	for(i=0; i<n; ++i){
		
		degree = 0;

		/* count no. neighbours + keep track of them */ 
		for(j=i+1; j<n; ++j){
			if (*(int*)PyArray_GETPTR2(A, i, j)){
			       buffer[degree] = j;
			       degree++;	
				
			}
		}	    
		/* store degree */
		deg_mono[i] = degree;
		
		/* copy neighbours list from buffer*/
		int* neighbours_i = (int*)calloc(degree, sizeof(int));
		for(d=0; d<degree; d++){
			neighbours_i[d] = buffer[d];
		}
		adj_mono[i] = neighbours_i;
	}	    
}



static PyObject *gradco_count(PyObject *self, PyObject *args) {
	
	/* set stdio buffer to zero to always show printf. TODO: remove this line */	
	setvbuf(stdout, NULL, _IONBF, 0);

	/* parse input from python */
	int n;
	int graphlet;
	PyArrayObject *A = NULL;
	if (!PyArg_ParseTuple(args, "O!ii", &PyArray_Type, &A, &n, &graphlet))
		return NULL;

	/* init offsets array. */
	/* enables fast indexing from row col format to flat array */
	offsets = malloc((n-1) * sizeof(*offsets)); /* Memory allocation */
	if (!offsets) {  
    	   printf( "memory allocation 'degrees' failed\n" );
    	   exit(-1);
	}
	int incumbent = -n;
	for(int i=0; i<(n-1); i++){
		offsets[i] = incumbent + n-i -1; 
		incumbent = offsets[i];
	}

	/* init monotonic adjacency linked list representation */
	/* memory allocation */
	deg_mono = malloc(n * sizeof(*deg_mono)); /* Memory allocation */
	if (!deg_mono) {  
    	   printf( "memory allocation 'deg_mono' failed\n" );
    	   exit(-1);
	}
	adj_mono = malloc( sizeof(adj_mono) * n); /* Memory allocation */
    	if( !adj_mono )
    	{
    	   printf( "memory allocation 'adj_mono' failed\n" );
    	   exit(-1);
    	}
	init_monotonic_adjacency(A, n, adj_mono, deg_mono);
	
	/* init adjacency linked list representation */
	deg = malloc(n * sizeof(*deg)); /* Memory allocation */
	if (!deg) {  
    	   printf( "memory allocation 'deg' failed\n" );
    	   exit(-1);
	}
	adj= malloc( sizeof(adj) * n); /* Memory allocation */
    	if( !adj)
    	{
    	   printf( "memory allocation 'adj' failed\n" );
    	   exit(-1);
    	}
	init_adjacency(A, n);
	
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

