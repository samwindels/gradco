

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <unordered_set>
#include <vector>
#include <iostream>

// For explanation on NO_IMPORT_ARRAT and PY_ARRAY_UNIQUE_SYMBOL, see: 
// 	https://numpy.org/doc/1.13/reference/c-api.array.html: miscelaneous, importing the api
// 	https://github.com/numpy/numpy/issues/9309
#define NO_IMPORT_ARRAY
#define PY_ARRAY_UNIQUE_SYMBOL my_ARRAY_API
#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>



class DirectedGraph
    {
    public:
	DirectedGraph(int n, PyArrayObject* rows, PyArrayObject* cols);

	std::vector<int>* get_successors(int node);
	std::vector<int>* get_predecessors(int node);
	bool has_edge(int a, int b);

    private:
	std::vector<std::vector<int> > adj_out; 
	std::vector<std::vector<int> > adj_in;  
	std::unordered_set<int> E;

	/* std::vector<std::unordered_set<int> > adj_out_set; */ 
	/* std::vector<std::unordered_set<int> > adj_in_set; */  
	
    };
