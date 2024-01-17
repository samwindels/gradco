#ifndef DENSE_MATRIX_H
#define DENSE_MATRIX_H

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

class DenseMatrix{

	private:
		int n; // Dimension of matrix.
		/* offsets array to enable fast indexing from row col format to flat array */
		unsigned int* offsets;
		unsigned int* array;
		unsigned int len; // Length of array.
		unsigned int to_flat_index(int i, int j);

	public:
		DenseMatrix(int n);
		void increment(int a, int b);
		PyObject* to_numpy();
		int get_n();
		unsigned int get(int flat_index);
		unsigned int get(int i, int j);
	};
	
#endif // DENSE_MATRIX_H
