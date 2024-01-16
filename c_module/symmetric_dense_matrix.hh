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
		unsigned int* offsets;
		unsigned int* array;
		int len; // Length of array.

		int to_flat_index(int i, int j);
	
	public:
		SymmetricDenseMatrix(int n){
			this->n = n;
			
			/* init offsets array. */
			this-> offsets = (unsigned int*) malloc((n-1) * sizeof(*offsets)); /* Memory allocation */
			if (!offsets) {  
    			   printf( "memory allocation 'offsets' failed\n" );
    			   exit(-1);
			}
			int incumbent = -n;
			for(int i=0; i<(n-1); i++){
				offsets[i] = incumbent + n-i -1; 
				incumbent = offsets[i];
			}
		
			this->len = this->n*(this->n-1)/2;
		        this->array = (unsigned int *) malloc(this->len * sizeof(int *));
			for (int i=0; i<this->len; i++){
				this->array[i] = 0;
			}
		};
	
	void add_scalar(int i, int j, int v);
	void increment_all_2_all(int a, int b);
	void increment_from_to(int a, int b);
	PyObject* to_numpy();


};

#endif // SYMMETRIC_DENSE_MATRIX_H
