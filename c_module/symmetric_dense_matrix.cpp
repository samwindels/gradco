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

void SymmetricDenseMatrix::add_scalar(int i, int j, int v){
	this->array[to_flat_index(i,j)] += v;
}

int SymmetricDenseMatrix::to_flat_index(int i, int j){
	if (i<j){ 
		return offsets[i]+j;
	}
	else{ 
		return offsets[j]+i; 
	}
}


