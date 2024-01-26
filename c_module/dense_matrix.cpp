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



void DenseMatrix::subtract_matrix(DenseMatrix& m){
	unsigned int val = 0;
	for (unsigned int row=0; row<m.get_n(); row++)
	{
		for (unsigned int col=0; col<m.get_n(); col++) {
			val = m.get(row, col);
			if (val != 0){
				subtract_scalar(row, col, val);
			}
		}
	}
}


void DenseMatrix::subtract_matrix(SymmetricDenseMatrix& m){

	unsigned int val = 0;
	for (unsigned int row=0; row<m.get_n(); row++)
	{
		for (unsigned int col=row+1; col<m.get_n(); col++) {
			val = m.get(row, col);
			if (val != 0){
				subtract_scalar(row, col, val);
				subtract_scalar(col, row, val);
			}
		}
	}
}

void DenseMatrix::subtract_matrix_multiple(DenseMatrix& m, int scalar){
	unsigned int val = 0;
	for (unsigned int row=0; row<m.get_n(); row++)
	{
		for (unsigned int col=0; col<m.get_n(); col++) {
			val = m.get(row, col);
			if (val != 0){
				subtract_scalar(row, col, val * scalar);
			}
		}
	}
}
void DenseMatrix::subtract_matrix_multiple(SymmetricDenseMatrix& m, int scalar){
	unsigned int val = 0;
	for (unsigned int row=0; row<m.get_n(); row++)
	{
		for (unsigned int col=row+1; col<m.get_n(); col++) {
			val = m.get(row, col);
			if (val != 0){
				val = val * scalar;
				subtract_scalar(row, col, val);
				subtract_scalar(col, row, val);
			}
		}
	}
}


int DenseMatrix::get_n(){
	return this->n;
}

unsigned int DenseMatrix::get(int i, int j){
	return this->array[to_flat_index(i,j)];
}

unsigned int DenseMatrix::get(int flat_i){
	return this->array[flat_i];
}

void DenseMatrix::increment(int i, int j){
	this->array[to_flat_index(i,j)]++;
}


void DenseMatrix::add_scalar(int i, int j, int scalar){
	this->array[to_flat_index(i,j)]+=scalar;
}

void DenseMatrix::subtract_scalar(int i, int j, int scalar){
	this->array[to_flat_index(i,j)]-=scalar;
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

PyObject* DenseMatrix::to_numpy_and_divide(int scalar){

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
				val = val / scalar;
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

