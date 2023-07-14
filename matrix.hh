/* #define PY_SSIZE_T_CLEAN */
/* #include <Python.h> */

#include <iostream>
#include <vector>
#include <unordered_map>
/* #include <utility> */


class Matrix {

    private:
	int n;
	std::vector<std::unordered_map<int, int> > adj;
	/* void increment_from_to(int a, int b); */

	std::unordered_map<char, int>::iterator it;
	
    public:
	Matrix(int n){};
	/* void increment_all_2_all(int a, int b, int c); */
	void increment_all_2_all(int a, int b, int c, int d);

};


