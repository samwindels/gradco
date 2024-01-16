#include "symmetric_dense_matrix.hh"


SymmetricDenseMatrix::SymmetricDenseMatrix(int n) : n(n){
			
		/* init offsets array. */
		this-> offsets = (unsigned int*) malloc((n-1) * sizeof(*offsets)); /* Memory allocation */
		if (!offsets) {  
    			printf( "memory allocation 'offsets' failed\n" );
    			exit(-1);
		}
		int incumbent = -n;
		for(int i=0; i<(n-1); i++){
			offsets[i] = incumbent + n-i -1; 
			incumbent = offsets[i];
		}
		
		this->len = this->n*(this->n-1)/2;
		this->array = (unsigned int *) malloc(this->len * sizeof(int *));
		for (int i=0; i<this->len; i++){
			this->array[i] = 0;
		}
}

void SymmetricDenseMatrix::increment(int i, int j){
	this->array[to_flat_index(i,j)]++;
}

int SymmetricDenseMatrix::to_flat_index(int i, int j){
	if (i<j){ 
		return offsets[i]+j;
	}
	else{ 
		return offsets[j]+i; 
	}
}


PyObject* to_numpy(){

	n_entries = 0;
	for (int i=0; i<this->len; i++){
		if (this->array[i] != 0){
			n_entries++;
		}
	}

	// contigues c, interpretted "3 rows, n_entries collumns"-array
	int* np_array = new int[3*n_entries];
	const npy_intp dims[2] = {3, n_entries};
	
	int i=0, j=n_entries, k=2*n_entries;



	for (int row=0; row < this->len; row++)
	{
		for (int col=row+1; col < this->len; col++)
		{
			flat_i = to_flat_index(row, col);
			val = this->array[flat_i];
			if (val != 0){
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


