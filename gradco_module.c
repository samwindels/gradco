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

int to_flat_index_undirected(i, j){
		/* return offsets[i]+j; */
	if (i<j){
		return offsets[i]+j;
	}
	else{
		/* printf("undir %d %d \n ",i, j); */
		return offsets[j]+i;
	}
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

	for(a=0; a<n; ++a){
		for(i=0; i<deg_mono[a]; i++)
		{       
			b = adj_mono[a][i];

			*(int*)	PyArray_GETPTR1(AG1, to_flat_index(a, b)) = deg[a] + deg[b] -2 -(2 * (*(int*) PyArray_GETPTR1(AG2, to_flat_index(a, b))));

			if (*(int*) PyArray_GETPTR1(AG1, to_flat_index(a, b)))
			{ 
				/* a is at orbit 2, b and c are at orbit 1 */
				/* all neighbours of a not connected to b */
				/* (if b and c connect they form G2 instead of G1)*/
				for(j=0; j<deg_mono[a]; j++){ /*mono?*/
					c = adj_mono[a][j]; /* mono?*/
					if (c>b && !*(int*) PyArray_GETPTR2(A, b, c)){
						/* c> b is because we only store the triu*/ 
						*(int*)	PyArray_GETPTR1(AG1, to_flat_index(b, c)) += 1;
					}
				}
				/* a is at orbit 1, b at orbit 2, and c at orbit 1 */
				/* all neighbours of b if not connected to a */
				/* (if a and c connect they form G2 instead of G1)*/
				for(j=0; j<deg[b]; j++){
					c = adj[b][j];
					if (c>a && !*(int*) PyArray_GETPTR2(A, a, c)){
						/* c> b is because we only store the triu*/ 
						*(int*)	PyArray_GETPTR1(AG1, to_flat_index(a, c)) += 1;
					}
				}
			}
			
		}
	}
	return AG1;
}


PyObject *count_G4(PyArrayObject *A, int n){

	/* initialise output array */
	/* returns 1d array = upper triangle adjacency matrix*/
	const npy_intp dims = (npy_intp) n * (n-1) / 2;
	PyObject *AG4 = PyArray_SimpleNew(1, &dims, NPY_INT);
	PyArray_FILLWBYTE(AG4, 0);
	
	/* graphlet G2 counts needed to apply redundancy equations */
	PyObject *AG2 = count_G2(A, n);
	
	PyObject *AG1 = count_G1(A, n);

	/* Input: A, n, degrees, neighbours, countarray, touches_G */
		
	int i, j, k;  /* Used to iterate neighbours*/
	int a, b, c, d;  /* Node indices in A*/
	int x, e, s, t;
	int orbitcount_6, orbitcount_7;

	for(a=0; a<n; ++a){
		for(i=0; i<deg_mono[a]; i++)
		{       
			b = adj_mono[a][i];

			/* a AT ORBIT 7 (i.e, centre). */
			/* check if a and b form star graphlet */ 
			
			/* t = *(int*) PyArray_GETPTR1(AG2, to_flat_index(a, b)); */
			s = 0;
			for(j=0; j<deg[a]; j++)
			{    
				c = adj[a][j];
		
				if (c != b){
					s += *(int*) PyArray_GETPTR1(AG2, to_flat_index_undirected(a, c));
					if (*(int*) PyArray_GETPTR2(A, b, c)){
						for(k=0; k<deg[c]; k++){
							d = adj[a][k];
							if (d!=c && d!= b && *(int*) PyArray_GETPTR2(A, a, d)){
								s -=2;
							}
						}
					
					}
				}

				/* if (!t){ */
				/* s += *(int*) PyArray_GETPTR1(AG2, to_flat_index_undirected(a, c)); */
				/* } */	
				/* if (*(int*) PyArray_GETPTR1(AG2, to_flat_index_undirected(a, c))&& t){ s-=1; */
				/* } */ 
				/* - 2* *(int*) PyArray_GETPTR2(A, b, c); */
				/* } */

				/* if (c > a){ */
				/* 	s += *(int*) PyArray_GETPTR1(AG2, to_flat_index(a, c)); */
				/* } */
				/* else{ */
				/* 	s += *(int*) PyArray_GETPTR1(AG2, to_flat_index(c, a)); */
				/* } */

			}	
			x = deg[a] - *(int*) PyArray_GETPTR1(AG2, to_flat_index(a, b));
			e = ((x - 1) * (x - 2))/2;
			
			orbitcount_7 = e - s/2;
				printf("a: %d", a);
				printf(", b: %d", b);
				/* printf(", c: %d", c); */

				printf("\tdeg: %d", deg[a]);
				printf(", e: %d", e);
				printf(", s: %d", s);
				printf(", t: %d", t);
				printf("orbitcount_2: %d", *(int*) PyArray_GETPTR1(AG2, to_flat_index(a, b)));
				printf("orbitcount_7: %d  \n", orbitcount_7);
			if (orbitcount_7>0)
			{
				*(int*)	PyArray_GETPTR1(AG4, to_flat_index(a, b)) += orbitcount_7;
				
				/* if form star, add counts to neighbours of a that not connect to b */
				{ 
					for(j=0; j<deg[a]; j++)
					{    
						c = adj[a][j];
						if (c>b && !*(int*) PyArray_GETPTR2(A, b, c)){
							e = (deg[a]-2);
							s = *(int*)PyArray_GETPTR1(AG2, to_flat_index(a, b)) + *(int*)PyArray_GETPTR1(AG2, to_flat_index_undirected(a, c));

							/* if (*(int*)PyArray_GETPTR1(AG2, to_flat_index(a, b)) &&  *(int*)PyArray_GETPTR1(AG2, to_flat_index_undirected(a, c))){ */

							/*  s -= *(int*)PyArray_GETPTR1(AG1, to_flat_index_undirected(b, c))>0; */
							/* } */

							*(int*)	PyArray_GETPTR1(AG4, to_flat_index(b, c)) += e - s ;

						}
						
					}	
				}
			}
			
			/* a AT ORBIT 6 (i.e, perifery), b at centre. */
			s = 0;
			for(j=0; j<deg[b]; j++)
			{    
				c = adj[b][j];

				if (c > b){
					s += *(int*) PyArray_GETPTR1(AG2, to_flat_index(b, c));
				}
				else{
					s += *(int*) PyArray_GETPTR1(AG2, to_flat_index(c, b));
				}
			}	
			t = *(int*) PyArray_GETPTR1(AG2, to_flat_index(a, b));

			x = deg[b] - *(int*) PyArray_GETPTR1(AG2, to_flat_index(a, b));
			e = ((x - 1) * (x - 2))/2;
			/* e = ((deg[b] - 1) * (deg[b] - 2))/2; */
			orbitcount_6 = e -s/2 + t;
			
			/* if form star, add counts to neighbours of b that not connect to a */
			if (orbitcount_6>0)
			{ 
			/* printf("a: %d", a); */
			/* printf("b: %d", b); */
			/* printf("c: %d", c); */
			/* printf("deg: %d", deg[a]); */

			/* printf("e: %d", e); */
			/* printf("s: %d", s); */
			/* printf("t: %d", t); */
			/* printf("orbitcount_6: %d", orbitcount_6); */
				
				printf("should not be hit\n");
				*(int*)	PyArray_GETPTR1(AG4, to_flat_index(a, b)) += orbitcount_6;
				
				for(j=0; j<deg[b]; j++)
				{    
					c = adj[b][j];

					if (c>a && !*(int*) PyArray_GETPTR2(A, a, c)){
						/* c> a is because we only store the triu*/ 
						/* *(int*)	PyArray_GETPTR1(AG4, to_flat_index(a, c)) += 1; */
							*(int*)	PyArray_GETPTR1(AG4, to_flat_index(a, c)) += (deg[b] -2) - *(int*)PyArray_GETPTR1(AG2, to_flat_index(a, b)) - *(int*)PyArray_GETPTR1(AG2, to_flat_index_undirected(b, c));
					}
					
				}	
			}


			
		}
	}
	return AG4;
}


PyObject *count_G3(PyArrayObject *A, int n){

	/* initialise output array */
	/* returns 1d array = upper triangle adjacency matrix*/
	const npy_intp dims = (npy_intp) n * (n-1) / 2;
	PyObject *AG3 = PyArray_SimpleNew(1, &dims, NPY_INT);
	PyArray_FILLWBYTE(AG3, 0);
	
	/* graphlet G1 and G2 counts needed to apply redundancy equations */
	PyObject *AG1 = count_G1(A, n);
	PyObject *AG8 = count_G8(A, n);
	
	/* Input: A, n, degrees, neighbours, countarray, touches_G */
		
	int i, j;  /* Used to iterate neighbours*/
	int a, b, c;  /* Node indices in A*/

	int p_bc;
	int orbit_8;

	/* used to check if sugraph of A touches graphlet G */
	/* a is on orbit 4 */
	/* int ab_bc = 5;  /1* litle endian *1/ */
	/* int ab_bc_ac; */
	/* a is on orbit 5 */
        /* int ab_ac = 3; */	
	/* int ab_ac_bc; */

	/* a is on orbit 4 */
	for(a=0; a<n; ++a){
		printf("a %d", a);
		for(i=0; i<deg[a]; i++)
		{       
			b = adj[a][i];		
			for(j=0; j<deg[b]; j++){

				c = adj[b][j];
				if (a==c) continue;
				if (*(int*)PyArray_GETPTR2(A, a, c)) continue;  /* a and c are connected, so not on G1*/ 

				/* G(x,y,z) ~ G1 == a is on orbit 4, b is on orbit 5*/
				p_bc = *(int*)PyArray_GETPTR1(AG1, to_flat_index_undirected(b, c));

				printf("p_bc %d", p_bc);

				if (p_bc > 0) {
					/* number of times a and c form G1 without b -> a, b, c form a square  */
					orbit_8 = (*(int*)(PyArray_GETPTR1(AG1, to_flat_index(a, c))))-1;
					printf("orbit_8 %d", orbit_8);
					/* subtract the times the t is also connected to b (no square but a four node clique) */
					/* double_orbit_8 -= */ 
					if (orbit_8){
						int count = p_bc - (2*orbit_8);
						if (count>0){
							/* *(int*)	PyArray_GETPTR1(AG3, to_flat_index(a, c)) += count; */
							*(int*)	PyArray_GETPTR1(AG3, to_flat_index_undirected(a, b)) += count;
							/* *(int*)	PyArray_GETPTR1(AG3, to_flat_index_undirected(a, c)) += count; */
							/* *(int*)	PyArray_GETPTR1(AG3, to_flat_index_undirected(b, c)) += count; */
						}

					}
					
				}
			}
		}
	}
	return AG3;
}


PyObject *count_G7(PyArrayObject *A, int n){

	/* initialise output array */
	/* returns 1d array = upper triangle adjacency matrix*/
	const npy_intp dims = (npy_intp) n * (n-1) / 2;
	PyObject *AG7 = PyArray_SimpleNew(1, &dims, NPY_FLOAT);
	PyArray_FILLWBYTE(AG7, 0);
	
	/* graphlet G2 and G8 counts needed to apply redundancy equations */
	PyObject *AG2 = count_G2(A, n);
	PyObject *AG8 = count_G8(A, n);
	
	/* Input: A, n, degrees, neighbours, countarray, touches_G */
		
	int i, j;  /* Used to iterate neighbours*/
	int a, b, c;  /* Node indices in A*/

	/* used to check if sugraph of A touches graphlet G */
	/* a is on orbit 1 */
	/* int ab_bc = 5;  /1* litle endian *1/ */
	/* int ab_bc_ac; */
	/* /1* a is on orbit 2 *1/ */
        /* int ab_ac = 3; */	
	/* int ab_ac_bc; */

	float o12_o14;
	float count_ab;
	float count_ac;
	float count_bc;

	/* todo: continues kunnen vermeden worden. monotonic incresing bij oorbit 1, een increasing en decreasing bij orbit 2 */
	/* ORBIT 12 */	
	for(a=0; a<n; ++a){
		for(i=0; i<deg[a]; i++)
		{       
			b = adj[a][i];		
			for(j=0; j<deg_mono[b]; j++){

				c = adj_mono[b][j];
				if (a==c) continue;
				if (!(*(int*)PyArray_GETPTR2(A, a, c))) continue;  /* a and c are not connected so not on G2*/ 
				
				o12_o14 = (float) *(int*)PyArray_GETPTR1(AG2, to_flat_index_undirected(b, c)) - 1;
				count_ab = o12_o14 - (float) (*(int*)PyArray_GETPTR1(AG8, to_flat_index_undirected(a, b))*3);
				count_ac = o12_o14 - (float) (*(int*)PyArray_GETPTR1(AG8, to_flat_index_undirected(a, c))*3);

				count_bc = o12_o14/2;
				/* printf("a%d ",a); */
				/* printf("b%d ",b); */
				/* printf("c%d\n",c); */
				/* printf("count_ab %d\n\n",count_ab); */
				/* printf("o12_o14%d ",o12_o14); */
				/* printf("count_ac %f\n\n",count_ac); */

				if (count_ab > 0){
					*(float*)	PyArray_GETPTR1(AG7, to_flat_index_undirected(a, b)) += count_ab;
				}
				if (count_ac > 0){
				*(float*)	PyArray_GETPTR1(AG7, to_flat_index_undirected(a, c)) += count_ac;
				}
				if (count_bc > 0 && b<c){
					*(float*)	PyArray_GETPTR1(AG7, to_flat_index_undirected(b, c)) += count_bc;
				}
			}
		}
	}

	/* ORBIT 9 and 12*/

	float o13_o14;
	for(a=0; a<n; ++a){
		for(i=0; i<deg[a]; i++)
		{       
			b = adj[a][i];		
			for(j=0; j<deg_mono[b]; j++){

				c = adj_mono[b][j];
				if (a==c) continue;
	 			if (!(*(int*)PyArray_GETPTR2(A, a, c))) continue;  /* a and c are not connected so not on G2*/ 

				o13_o14 = (float) *(int*)PyArray_GETPTR1(AG2, to_flat_index_undirected(a, b)) - 1.0;
				o13_o14 += (float) *(int*)PyArray_GETPTR1(AG2, to_flat_index_undirected(a, c)) - 1.0;
				o13_o14 /= 2.0;

				if (o13_o14){
					*(float*) PyArray_GETPTR1(AG7, to_flat_index_undirected(b, c)) += o13_o14;
				}
			}
		}
	}

/* 	float o9_o12; */
/* 	/1* float count_ac; *1/ */
/* 	for(b=0; b<n; ++b){ */
/* 		for(i=0; i<deg[b]; i++) */
/* 		{ */       
/* 			a = adj[b][i]; */		
/* 			for(j=0; j<deg[b]; j++){ */

/* 				c = adj[b][j]; */
/* 				if (a==c) continue; */
				
/* 	 			/1* a and c are connected so not on G1*/ 
/* 				if ((*(int*)PyArray_GETPTR2(A, a, c))) continue; */    

/* 				o9_o12 = ((float) *(int*)PyArray_GETPTR1(AG2, to_flat_index_undirected(b, c)))/4; */

/* 				count_ac = o9_o12; */ 
/* 				printf("a%d ",a); */
/* 				printf("b%d ",b); */
/* 				printf("c%d\n",c); */
/* 				printf("count_ac %f\n",count_ac); */


/* 				/1* *(int*)	PyArray_GETPTR1(AG7, to_flat_index_undirected(a, c)) += count_ac; *1/ */
/* 				*(float*)	PyArray_GETPTR1(AG7, to_flat_index_undirected(c, a)) += count_ac; */
/* 				/1* *(int*)	PyArray_GETPTR1(AG7, to_flat_index_undirected(b, a)) += count_ac; *1/ */
/* 				/1* *(int*)	PyArray_GETPTR1(AG7, to_flat_index_undirected(b, c)) += count_ac; *1/ */
/* 			} */
/* 		} */
/* 	} */

	return AG7;
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
	switch(graphlet) {
	   case 1:
		return count_G1(A, n);
	   case 2:
	   	return count_G2(A, n);
	   case 3:
	   	return count_G3(A, n);
	   case 4:
		return count_G4(A, n);
	   case 7:
		return count_G7(A, n);
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

