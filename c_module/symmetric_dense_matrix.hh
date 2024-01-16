#ifndef SYMMETRIC_DENSE_MATRIX_H
#define SYMMETRIC_DENSE_MATRIX_H

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

class SymmetricDenseMatrix{

	private:
		int n; // Dimension of matrix.
	
	public:
		SymmetricDenseMatrix(int n){
		};

	void increment_all_2_all(int a, int b);
		void increment_from_to(int a, int b);
		PyObject* to_numpy();


};

#endif // SYMMETRIC_DENSE_MATRIX_H
