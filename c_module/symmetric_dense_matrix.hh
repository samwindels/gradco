#ifndef SYMMETRIC_DENSE_MATRIX_H
#define SYMMETRIC_DENSE_MATRIX_H

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

class SymmetricDenseMatrix{

	private:
		int n; // Dimension of matrix.
		/* offsets array to enable fast indexing from row col format to flat array */
		int *offsets;
		unsigned int* array;


	int to_flat_index(i, j){
		if (i<j){ 
			return offsets[i]+j;
		}
		else{ 
			return offsets[j]+i; 
		}
	}
	
	public:
		SymmetricDenseMatrix(int n){
			/* init offsets array. */
			offsets = malloc((n-1) * sizeof(*offsets)); /* Memory allocation */
			if (!offsets) {  
    			   printf( "memory allocation 'offsets' failed\n" );
    			   exit(-1);
			}
			int incumbent = -n;
			for(int i=0; i<(n-1); i++){
				offsets[i] = incumbent + n-i -1; 
				incumbent = offsets[i];
			}
			
		        array = (unsigned **)malloc(n*(n-1)/2 sizeof(int *));
		};
	
	void add_scalar(int i, j, v);
	void increment_all_2_all(int a, int b);
	void increment_from_to(int a, int b);
	PyObject* to_numpy();


};

#endif // SYMMETRIC_DENSE_MATRIX_H
