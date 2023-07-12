

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <unordered_set>
#include <vector>
#include <iostream>

#include <numpy/arrayobject.h>
#include <numpy/ndarrayobject.h>



class DirectedGraph
    {
    public:
	DirectedGraph(PyArrayObject*, PyArrayObject*);

    private:
	std::vector<std::unordered_set<int> > adj_out; 
	std::vector<std::unordered_set<int> > adj_in;  
	
    };
