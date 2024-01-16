#ifndef SPARSE_MATRIX_H
#define SPARSE_MATRIX_H

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>
#include "unordered_dense.h"

#include <iostream>
#include <vector>
#include "symmetric_dense_matrix.hh" 
#include "dense_matrix.hh" 


class SparseMatrix{

    private:
	int n; // Dimension of matrix.
	int z_entries;  // Track no. zero entries in "adj".
	int n_entries;  // Track no. entries in "adj".
	
	ankerl::unordered_dense::map<int, int>::iterator it;
	void subtract_scalar(int a, int b, int v);

    public:
	SparseMatrix(int n){
    		adj.resize(n, ankerl::unordered_dense::map<int, int>());	
		this->n = n;
		n_entries = 0;
	}
	
	void increment_all_2_all(int a, int b);
	void increment_all_2_all(int a, int b, int c);
	void increment_all_2_all(int a, int b, int c, int d);
	
	void increment_from_to(int a, int b); 
	int get(int a, int b);
	int get_n();
	
	void subtract_matrix_multiple(SparseMatrix& m, int scalar);
	void subtract_matrix(SymmetricDenseMatrix& m);
	void subtract_matrix(DenseMatrix& m);
	void add_scalar(int a, int b, int v);
	PyObject* to_numpy();
	PyObject* to_numpy_and_divide(int numerator);
	
	std::vector<ankerl::unordered_dense::map<int, int> > adj;


};

#endif // SPARSE_MATRIX_H
