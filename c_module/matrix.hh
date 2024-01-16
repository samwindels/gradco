#ifndef MATRIX_H
#define MATRIX_H


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
	
	virtual void increment_all_2_all(int a, int b) = 0;
	virtual void increment_all_2_all(int a, int b, int c) = 0;
	virtual void increment_all_2_all(int a, int b, int c, int d) = 0;
	virtual void increment_from_to(int a, int b) = 0;

	virtual int get(int a, int b) = 0;
	
	virtual void subtract_matrix_multiple(const Matrix& m, int scalar) = 0;
	virtual void add_scalar(int a, int b, int v) = 0;
	
	virtual PyObject* to_numpy() = 0;
	virtual PyObject* to_numpy_and_divide(int numerator) = 0;

	int get_n() const{
		return this->n;
	}


};

#endif // MATRIX_H
