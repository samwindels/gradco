/* #define PY_SSIZE_T_CLEAN */
/* #include <Python.h> */

#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>
#include "unordered_dense.h"

#include <iostream>
#include <vector>
#include "matrix.hh"


class SparseMatrix : public Matrix{

    private:
	int z_entries;  // Track no. zero entries in "adj".
	
	ankerl::unordered_dense::map<int, int>::iterator it;
	void subtract_scalar(int a, int b, int v);

    public:
	SparseMatrix(int n): Matrix(n) {
    		adj.resize(n, ankerl::unordered_dense::map<int, int>());	
	}
	
	void increment_all_2_all(int a, int b){};
	void increment_all_2_all(int a, int b, int c){};
	void increment_all_2_all(int a, int b, int c, int d){};
	
	void increment_from_to(int a, int b){
		// check if key `b` exists in the map or not
        	it = adj[a].find(b);
        	// key found
        	if (it != adj[a].end()) {
        	    	it->second++;    // increment map's value for key `b`
        	}
        	// key not found
        	else {
        	    	adj[a].insert(std::make_pair(b, 1));
			n_entries++;
		}
        }

	int get(int a, int b){return 1;};
	
	void subtract_matrix_multiple(const Matrix& m, int scalar){};
	void add_scalar(int a, int b, int v){
		if (v==0){ return; }
        	
		it = adj[a].find(b);
 
        	// key found
        	if (it != adj[a].end()) {
        	    	it->second+=v;    
        	}
        	// key not found
        	else {
        	    	adj[a].insert(std::make_pair(b, v));
			n_entries++;
        	}
	}
	
	PyObject* to_numpy(){return NULL;};
	PyObject* to_numpy_and_divide(int numerator){return NULL;};
	
	std::vector<ankerl::unordered_dense::map<int, int> > adj;


};


