/* #define PY_SSIZE_T_CLEAN */
/* #include <Python.h> */

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>
#include "unordered_dense.h"

#include <iostream>
#include <vector>


class Matrix {

    protected:
	int n_entries;  // Track no. entries in "adj".
	const int n;  // Dimension of matrix.
	
    public:
	Matrix(int n) : n_entries(0), n(n) {};
	
	virtual void increment_all_2_all(int a, int b);
	virtual void increment_all_2_all(int a, int b, int c);
	virtual void increment_all_2_all(int a, int b, int c, int d);
	virtual void increment_from_to(int a, int b);

	virtual int get(int a, int b);
	
	virtual void subtract_matrix_multiple(const Matrix& m, int scalar);
	virtual void add_scalar(int a, int b, int v);
	
	virtual PyObject* to_numpy();
	virtual PyObject* to_numpy_and_divide(int numerator);

	int get_n() const{
		return this->n;
	}


};


