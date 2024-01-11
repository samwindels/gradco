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

    private:
	int n_entries;  // Track no. entries in "adj".
	int z_entries;  // Track no. zero entries in "adj".

    public:
	std::vector<ankerl::unordered_dense::map<int, int> > adj;
	Matrix(int n);
	Matrix(const Matrix& m);
	void increment_all_2_all(int a, int b);
	void increment_all_2_all(int a, int b, int c);
	void increment_all_2_all(int a, int b, int c, int d);
	void increment_from_to(int a, int b);

	int get(int a, int b);
	
	PyObject* to_numpy();
	PyObject* division_to_numpy(int scalar);
	
	ankerl::unordered_dense::map<int, int>::iterator it;
	void add_scalar(int a, int b, int v);
	void subtract_scalar(int a, int b, int v);
	void subtract_matrix_multiple(const Matrix& m, int scalar);


};


