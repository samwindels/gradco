#ifndef SYMMETRIC_DENSE_MATRIX_H
#define SYMMETRIC_DENSE_MATRIX_H

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>
#include "dense_matrix.hh"

class DenseMatrix;
class SymmetricDenseMatrix{

	private:
		int n; // Dimension of matrix.
		/* offsets array to enable fast indexing from row col format to flat array */
		unsigned int* offsets;
		unsigned int* array;
		int len; // Length of array.

	public:
		SymmetricDenseMatrix(int n);
		void increment(int a, int b);
		PyObject* to_numpy();
		PyObject* to_numpy_and_divide(int scalar);
		unsigned int to_flat_index(int i, int j);
		int get_n();
		unsigned int get(int flat_i);
		unsigned int get(int i, int j);
		void add_scalar(int i, int j, unsigned int scalar);
		void subtract_scalar(int i, int j, unsigned int scalar);
		void subtract_matrix(DenseMatrix& m);
		void subtract_matrix(SymmetricDenseMatrix& m);
		void subtract_matrix_multiple(DenseMatrix& m, int scalar);
		void subtract_matrix_multiple(SymmetricDenseMatrix& m, int scalar);
	};
	
#endif // SYMMETRIC_DENSE_MATRIX_H
