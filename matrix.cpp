
#include "matrix.hh"

Matrix::Matrix(int n){
	n_entries=0;
    	adj.resize(n, std::unordered_map<int, int>());	
}


void Matrix::increment_from_to(int a, int b){
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

void Matrix::increment_all_2_all(int a, int b){

	increment_from_to(a, b);
	increment_from_to(b, a);
}

void Matrix::increment_all_2_all(int a, int b, int c){

	increment_from_to(a, b);
	increment_from_to(a, c);
	
	increment_from_to(b, a);
	increment_from_to(b, c);
	
	increment_from_to(c, a);
	increment_from_to(c, b);
}
void Matrix::increment_all_2_all(int a, int b, int c, int d){

	increment_from_to(a, b);
	increment_from_to(a, c);
	increment_from_to(a, d);
	
	increment_from_to(b, a);
	increment_from_to(b, c);
	increment_from_to(b, d);
	
	increment_from_to(c, a);
	increment_from_to(c, b);
	increment_from_to(c, d);
	
	increment_from_to(d, a);
	increment_from_to(d, b);
	increment_from_to(d, c);

}

PyObject* Matrix::to_numpy(){

	// contigues c, interpretted "3 rows, n_entries collumns"-array
	int* array = new int[3*n_entries];
	const npy_intp dims[2] = {3, n_entries};
	
	int i=0, j=n_entries, k=2*n_entries;

	int row = 0;
	for (auto & col_map : adj) {
		for (auto& [col, data]: col_map){
			
			array[i] = row;
			array[j] = col;
			array[k] = data;

			i++;
			j++;
			k++;
		}
		row++;
	}

	return PyArray_SimpleNewFromData(2, dims, NPY_INT, array);

}
int Matrix::get(int a, int b){

        it = adj[a].find(b);
 
        // key found
        if (it != adj[a].end()) {
            	return it->second;
        }
        // key not found
        else {
		return 0;
        }
}



