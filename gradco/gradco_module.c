/* include python, should be done before standard c librarys */
#define PY_SSIZE_T_CLEAN
#include <Python.h>
/* #define PY_ARRAY_UNIQUE_SYMBOL cool_ARRAY_API */
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

/* GLOBAL VARIABLES */

/* We check if a given 3 or 4 node graph touches a specific graphlet: */
/*     We interpret the upper triangle of the adj. m. as an array of bits. */
/*     We interpret the bitarray as defining an integer (little endian). */
/*     We map each integer repr. to the graph touching a given graphlet yes or no. */

int touches_G1[8]  = {0,0,0,1,0,1,1,0};
int touches_G2[8]  = {0,0,0,0,0,0,0,1};
int touches_G3[64] = {0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0};
int touches_G4[64] = {0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0};
int touches_G5[64] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0};
int touches_G6[64] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0};
int touches_G7[64] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0};
int touches_G8[64] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};


/* offsets array to enable fast indexing from row col format to flat array */
int *offsets;
int to_flat_index(i, j){
		return offsets[i]+j;
	/* if (i<j){ */
	/* 	return offsets[i]+j; */
	/* } */
	/* else{ */
	/* 	printf(i, j); */
	/* 	return offsets[j]+i; */
	/* } */
}

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

PyObject *count_G8(PyArrayObject *A, int n){
	/* count graphlet adjacency for four node graphlet G8 (orbit 14)*/

	/* initialise output array */
	/* we return a 1d arra = upper triangle adjacency matrix*/
	/* this to save memory as the matrix is symmetric*/
	const npy_intp dims = (npy_intp) n * (n-1) / 2;
	PyObject *AG = PyArray_SimpleNew(1, &dims, NPY_INT);
	PyArray_FILLWBYTE(AG, 0);

	/* Input: A, n, degrees, neighbours, countarray */
		
	int i, j, k;  /* Used to iterate neighbours*/
	int a, b, c, d;  /* Node indices in A*/

	/* used to check if sugraph of A touches graphlet G */
	int ab_bc_cd = 1+8+32;  /* litle endian */ 
	int ab_bc_cd_ac;
	int ab_bc_cd_ac_ad_bd;

	for(a=0; a<n; ++a){
		for(i=0; i<deg_mono[a]; i++)
		{       
			b = adj_mono[a][i];		

			for(j=0; j<deg_mono[b]; j++){
				c = adj_mono[b][j];
				ab_bc_cd_ac = ab_bc_cd + (*(int*)PyArray_GETPTR2(A, a, c)!=0)*2;

				for(k=0; k<deg_mono[c]; k++){
					d = adj_mono[c][k];

					/* interpret upper triangle adjacency as an int */				
					ab_bc_cd_ac_ad_bd = ab_bc_cd_ac + (*(int*)PyArray_GETPTR2(A, a, d)!=0)*4 + (*(int*)PyArray_GETPTR2(A, b, d)!=0)*16;
					
					if (touches_G8[ab_bc_cd_ac_ad_bd]){
					  	
						*(int*)	PyArray_GETPTR1(AG, to_flat_index(a, b)) += 1;
					  	*(int*)	PyArray_GETPTR1(AG, to_flat_index(a, c)) += 1;
					  	*(int*)	PyArray_GETPTR1(AG, to_flat_index(a, d)) += 1;
					  	*(int*)	PyArray_GETPTR1(AG, to_flat_index(b, c)) += 1;
					  	*(int*)	PyArray_GETPTR1(AG, to_flat_index(b, d)) += 1;
					  	*(int*)	PyArray_GETPTR1(AG, to_flat_index(c, d)) += 1;
					}

				}
			}
		}
	}
	return AG;
}

PyObject *count_G2(PyArrayObject *A, int n){
	/* count graphlet adjacency for three node grahplet G2 (orbit 3)*/

	/* initialise output array */
	/* returns 1d array = upper triangle adjacency matrix*/
	const npy_intp dims = (npy_intp) n * (n-1) / 2;
	PyObject *AG = PyArray_SimpleNew(1, &dims, NPY_INT);
	PyArray_FILLWBYTE(AG, 0);


	/* Input: A, n*/
		
	int i, j;  /* Used to iterate neighbours*/
	int a, b, c;  /* Node indices in A*/

	/* used to check if sugraph of A touches graphlet G */
	int ab_bc = 5;  /* litle endian */ 
	int ab_bc_ac;

	for(a=0; a<n; ++a){
		for(i=0; i<deg_mono[a]; i++)
		{       
			/* printf("degree %d", degrees[a]); */
			b = adj_mono[a][i];		
			for(j=0; j<deg_mono[b]; j++){
				c = adj_mono[b][j];
				ab_bc_ac = ab_bc + (*(int*)PyArray_GETPTR2(A, a, c)!=0)*2;
				/* printf("ab_bc_ac %d", ab_bc_ac); */

				if (touches_G2[ab_bc_ac]){
					  	
					*(int*)	PyArray_GETPTR1(AG, to_flat_index(a, b)) += 1;
					*(int*)	PyArray_GETPTR1(AG, to_flat_index(a, c)) += 1;
					*(int*)	PyArray_GETPTR1(AG, to_flat_index(b, c)) += 1;
				}

			}
		}
	}
	return AG;
}


PyObject *count_G1(PyArrayObject *A, int n){

	/* initialise output array */
	/* returns 1d array = upper triangle adjacency matrix*/
	const npy_intp dims = (npy_intp) n * (n-1) / 2;
	PyObject *AG1 = PyArray_SimpleNew(1, &dims, NPY_INT);
	PyArray_FILLWBYTE(AG1, 0);
	
	/* graphlet G2 counts needed to apply redundancy equations */
	PyObject *AG2 = count_G2(A, n);

	
	/* Input: A, n, degrees, neighbours, countarray, touches_G */
		
	int i, j;  /* Used to iterate neighbours*/
	int a, b, c;  /* Node indices in A*/

	/* used to check if sugraph of A touches graphlet G */
	/* a is on orbit 1 */
	int ab_bc = 5;  /* litle endian */
	int ab_bc_ac;
	/* a is on orbit 2 */
        int ab_ac = 3;	
	int ab_ac_bc;

	for(a=0; a<n; ++a){
		for(i=0; i<deg_mono[a]; i++)
		{       
			b = adj_mono[a][i];
		}
	}
	return AG1;
}

/* PyObject *count_G1(PyArrayObject *A, int n){*/

/* 	/* initialise output array */*/
/* 	/* returns 1d array = upper triangle adjacency matrix*/*/
/* 	const npy_intp dims = (npy_intp) n * (n-1) / 2;*/
/* 	PyObject *AG1 = PyArray_SimpleNew(1, &dims, NPY_INT);*/
/* 	PyArray_FILLWBYTE(AG1, 0);*/
	
/* 	/* graphlet G2 counts needed to apply redundancy equations */*/
/* 	/* PyObject *AG2 = count_G2(A, n); */*/

	
/* 	/* Input: A, n, degrees, neighbours, countarray, touches_G */*/
		
/* 	int i, j;  /* Used to iterate neighbours*/*/
/* 	int a, b, c;  /* Node indices in A*/*/

/* 	/* used to check if sugraph of A touches graphlet G */*/
/* 	/* a is on orbit 1 */*/
/* 	int ab_bc = 5;  /* litle endian */*/
/* 	int ab_bc_ac;*/
/* 	/* a is on orbit 2 */*/
/*         int ab_ac = 3;*/	
/* 	int ab_ac_bc;*/

/* 	/* todo: continues kunnen vermeden worden. monotonic incresing bij oorbit 1, een increasing en decreasing bij orbit 2 */*/
/* 	for(a=0; a<n; ++a){*/
/* 		for(i=0; i<deg[a]; i++)*/
/* 		{*/       
/* 			/* printf("degree %d", degrees[a]); */*/
/* 			b = adj[a][i];*/		
/* 			/* a is on orbit 1: the 3-node path outer */*/
/* 			for(j=0; j<deg[b]; j++){*/

/* 				c = adj[b][j];*/
/* 				if (a==c) continue;*/
/* 				ab_bc_ac = ab_bc + (*(int*)PyArray_GETPTR2(A, a, c)!=0)*2;*/
/* 				/* printf("ab_bc_ac %d", ab_bc_ac); */*/

/* 				if (touches_G1[ab_bc_ac]){*/
/* 					/* printf("hit orbit 1"); */*/	  	
/* 					*(int*)	PyArray_GETPTR1(AG1, offsets[a]+b) += 1;*/
/* 					*(int*)	PyArray_GETPTR1(AG1, offsets[a]+c) += 1;*/
/* 					if (b < c){*/
/* 						*(int*)	PyArray_GETPTR1(AG1, offsets[b]+c) += 1;*/
/* 					}*/
/* 					else{*/
/* 						*(int*)	PyArray_GETPTR1(AG1, offsets[c]+b) += 1;*/
/* 					}*/
/* 				}*/

/* 			}*/
/* 			/* a is on orbit 2: the 3-node path middle */*/
/* 			for(j=0; j<deg[a]; j++){*/
/* 				c = adj[a][j];*/
/* 				if (b==c) continue;*/

/* 				ab_ac_bc = ab_ac + (*(int*)PyArray_GETPTR2(A, b, c)!=0)*4;*/
/* 				/* printf("ab_bc_ac %d", ab_bc_ac); */*/
/* 				if (touches_G1[ab_bc_ac]){*/
					  	
/* 					*(int*)	PyArray_GETPTR1(AG1, offsets[a]+b) += 1;*/
/* 					*(int*)	PyArray_GETPTR1(AG1, offsets[a]+c) += 1;*/
/* 					if (b < c){*/
/* 						*(int*)	PyArray_GETPTR1(AG1, offsets[b]+c) += 1;*/
/* 					}*/
/* 					else{*/
/* 						*(int*)	PyArray_GETPTR1(AG1, offsets[c]+b) += 1;*/
/* 					}*/
/* 				}*/

/* 			}*/
/* 		}*/
/* 	}*/
/* 	return AG1;*/
/* }*/

PyObject *count_G7(PyArrayObject *A, int n){

	/* initialise output array */
	/* returns 1d array = upper triangle adjacency matrix*/
	const npy_intp dims = (npy_intp) n * (n-1) / 2;
	PyObject *AG7 = PyArray_SimpleNew(1, &dims, NPY_INT);
	PyArray_FILLWBYTE(AG7, 0);
	
	/* graphlet G2 and G8 counts needed to apply redundancy equations */
	PyObject *AG2 = count_G2(A, n);
	PyObject *AG8 = count_G8(A, n);
	
	/* Input: A, n, degrees, neighbours, countarray, touches_G */
		
	int i, j;  /* Used to iterate neighbours*/
	int a, b, c;  /* Node indices in A*/

	/* used to check if sugraph of A touches graphlet G */
	/* a is on orbit 1 */
	int ab_bc = 5;  /* litle endian */
	int ab_bc_ac;
	/* a is on orbit 2 */
        int ab_ac = 3;	
	int ab_ac_bc;

	/* todo: continues kunnen vermeden worden. monotonic incresing bij oorbit 1, een increasing en decreasing bij orbit 2 */
	for(a=0; a<n; ++a){
		for(i=0; i<deg[a]; i++)
		{       
			b = adj[a][i];		
			/* int eb = to_flat_index(a, b); */
			/* a is on orbit 1: the 3-node path outer */
			for(j=0; j<deg[b]; j++){

				c = adj[b][j];
				if (a==c) continue;
				/* ec = to_flat_index(a, c) */
				ab_bc_ac = ab_bc + (*(int*)PyArray_GETPTR2(A, a, c)!=0)*2;

				if (touches_G1[ab_bc_ac]){
					/* three node path */ 
					/* printf("hit orbit 1"); */	  	
					/* *(int*)	PyArray_GETPTR1(AG1, offsets[a]+b) += 1; */
					/* *(int*)	PyArray_GETPTR1(AG1, offsets[a]+c) += 1; */
					/* *(int*)	PyArray_GETPTR1(AG1, offsets[b]+c) += 1; */
				}
				else{

				   /* three node path */ 
				}


			}
			/* a is on orbit 2: the 3-node path middle */
			for(j=0; j<deg[a]; j++){
				c = adj[a][j];
				if (b==c) continue;

				ab_ac_bc = ab_ac + (*(int*)PyArray_GETPTR2(A, b, c)!=0)*4;
				if (touches_G1[ab_bc_ac]){
					  	
					/* *(int*)	PyArray_GETPTR1(AG1, offsets[a]+b) += 1; */
					/* *(int*)	PyArray_GETPTR1(AG1, offsets[a]+c) += 1; */
					/* *(int*)	PyArray_GETPTR1(AG1, offsets[b]+c) += 1; */
				}

			}
		}
	}
	return AG7;
}


static PyObject *gradco_count(PyObject *self, PyObject *args) {

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
	switch(graphlet) {
	   case 1:
		return count_G1(A, n);
	   case 2 :
	   	return count_G2(A, n);
	   /* case 7: */
		/* return count_G7(A, n); */
	   case 8  :
	   	return count_G8(A, n);
	   default : 
    	   	printf( "choose a graphlet in range [1,8] \n" );
    	   	exit(-1);
	}

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

