#include "dense_matrix.hh"
#include <iostream>

DenseMatrix::DenseMatrix(int n) : n(n){
			
		/* init offsets array. */
		this-> offsets = (unsigned int*) malloc((n) * sizeof(*offsets)); /* Memory allocation */
		if (!offsets) {  
    			printf( "memory allocation 'offsets' failed\n" );
    			exit(-1);
		}
		/* int incumbent = -n; */
		/* for(int i=0; i<(n-1); i++){ */
		/* 	offsets[i] = incumbent + n -1; */ 
		/* 	incumbent = offsets[i]; */
		/* } */
		for(int i=0; i<(n); i++){
			offsets[i] = i*n;
		}
		
		this->len = this->n*n;
		this->array = (unsigned int *) malloc(this->len * sizeof(int *));
		for (int i=0; i<this->len; i++){
			this->array[i] = 0;
		}
}

int DenseMatrix::get_n(){
	return this->n;
}

unsigned int DenseMatrix::get_entry(int flat_i){
	return this->array[flat_i];
}

void DenseMatrix::increment(int i, int j){
	this->array[to_flat_index(i,j)]++;
}

unsigned int DenseMatrix::to_flat_index(int i, int j){
	return offsets[i]+j;
}


PyObject* DenseMatrix::to_numpy(){

	unsigned int n_entries = 0;
	for (int i=0; i<this->len; i++){
		if (this->array[i] != 0){
			n_entries++;
		}
	}
	n_entries = n_entries; // output matrix is symmetric, array only stores upper triu

	// contigues c, interpretted "3 rows, n_entries collumns"-array
	int* np_array = new int[3*n_entries];
	const npy_intp dims[2] = {3, n_entries};
	
	int i=0;
	int j=n_entries; 
	int k=2*n_entries;

	unsigned int val;
	unsigned int flat_i;

	for (int row=0; row < this->n; row++)
	{
		for (int col=0; col < this->n; col++)
		{
			flat_i = to_flat_index(row, col);
			val = this->array[flat_i];
			if (val != 0){
				/* std::cout << "i: " << i << " j: " << j << " k: " << k << std::endl; */
				np_array[i] = row;
				np_array[j] = col;
				np_array[k] = val;
				i++;
				j++;
				k++;
			}
		}
	
	}	
	return PyArray_SimpleNewFromData(2, dims, NPY_INT, np_array);

}


