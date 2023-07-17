/* #define PY_SSIZE_T_CLEAN */
/* #include <Python.h> */

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>

#include <iostream>
#include <vector>
#include <unordered_map>


class Matrix {

    private:
	std::vector<std::unordered_map<int, int> > adj;
	int n_entries;  // Track no. entreis in "adj".

	
    public:
	Matrix(int n);
	void increment_all_2_all(int a, int b);
	void increment_all_2_all(int a, int b, int c);
	void increment_all_2_all(int a, int b, int c, int d);
	void increment_from_to(int a, int b);
	PyObject* to_numpy_arrays();
	
	std::unordered_map<int, int>::iterator it;


};


