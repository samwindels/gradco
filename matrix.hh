#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <iostream>
#include <vector>
#include <unordered_set>


class Matrix {

    private:
	int n;
	std::vector<std::unordered_set<int> > adj;
	
    public:
	Matrix(int n){};
	void addCount(int i, int j, int count);

};


