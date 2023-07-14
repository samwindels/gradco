
#include "directed_graph.hh"

DirectedGraph::DirectedGraph(int n, PyArrayObject* rows, PyArrayObject* cols) : n(n) {

	// INITIALISE THE ADJACENY LISTS and ADJACENCY SETS
	adj_in.resize(n, std::vector<int>());	
	adj_out.resize(n, std::vector<int>());	
	
	adj_out_set.resize(n, std::unordered_set<int>());	

	// FOR LOOP OVER THE ROWS/COLS TO FILL ADJACENCY LISTS
	// Array iterator
    	NpyIter* iter_rows = NpyIter_New(rows, NPY_ITER_READONLY|
    	                      		 NPY_ITER_EXTERNAL_LOOP|
    	                        	 NPY_ITER_REFS_OK,
    	                        	 NPY_KEEPORDER, NPY_NO_CASTING,
    	                        	 NULL);
    	
    	NpyIter* iter_cols = NpyIter_New(cols, NPY_ITER_READONLY|
    	                        	 NPY_ITER_EXTERNAL_LOOP|
    	                        	 NPY_ITER_REFS_OK,
    	                        	 NPY_KEEPORDER, NPY_NO_CASTING,
    	                        	 NULL);
    	
	// The location of the data pointer which the iterator may update 
    	char **dataptr_rows = NpyIter_GetDataPtrArray(iter_rows);
    	char **dataptr_cols = NpyIter_GetDataPtrArray(iter_cols);
    	
	// The location of the stride which the iterator may update
    	npy_intp *strideptr_rows = NpyIter_GetInnerStrideArray(iter_rows);
    	npy_intp *strideptr_cols = NpyIter_GetInnerStrideArray(iter_cols);
    	
	// The location of the inner loop size which the iterator may update
    	npy_intp *innersizeptr_rows = NpyIter_GetInnerLoopSizePtr(iter_rows);
    	npy_intp *innersizeptr_cols = NpyIter_GetInnerLoopSizePtr(iter_cols);

	// METHOD POINTERS
    	PyArray_GetItemFunc* getitem_rows = PyArray_DESCR(rows)->f->getitem;
    	PyArray_GetItemFunc* getitem_cols = PyArray_DESCR(cols)->f->getitem;
	
	// FOR LOOP 
	// initialise for loop
    	NpyIter_IterNextFunc *iternext_rows, *iternext_cols;
    	iternext_rows = NpyIter_GetIterNext(iter_rows, NULL);
    	iternext_cols = NpyIter_GetIterNext(iter_cols, NULL);
	
	// where to store pointer values
    	char *data_rows, *data_cols;
	npy_intp stride_rows, stride_cols;
	
	// track for loop progress	
	npy_intp count_rows, count_cols;
    
	// values in the two arrays (finally)
	int row, col;

	do {
    	    /* Get the inner loop data/stride/count values */
    	    data_rows = *dataptr_rows;
    	    data_cols = *dataptr_cols;
    	    
    	    stride_rows = *strideptr_rows;
    	    stride_cols = *strideptr_cols;
    	    
    	    count_rows = *innersizeptr_rows;
    	    count_cols = *innersizeptr_cols;

    	    /* This is a typical inner loop for NPY_ITER_EXTERNAL_LOOP */
    	    while (count_rows-- and count_cols--) {
    	    
    	    	row = PyLong_AsLong(getitem_rows(data_rows, rows));
    	    	col = PyLong_AsLong(getitem_cols(data_cols, cols));
    	    	if (row != col && col){
			adj_out[row].push_back(col);
			adj_in[col].push_back(row);
			
			adj_out_set[row].insert(col);
    	    	}
		data_rows += stride_rows;
    	        data_cols += stride_cols;
    	    }

    	    /* Increment the iterator to the next inner loop */
    	} while(iternext_rows(iter_rows) && iternext_cols(iter_cols));

    	NpyIter_Deallocate(iter_rows);
    	NpyIter_Deallocate(iter_cols);

}

std::vector<int>* DirectedGraph::get_successors(int node){
	return &adj_out[node];
}

std::vector<int>* DirectedGraph::get_predecessors(int node){
	return &adj_in[node];
}

bool DirectedGraph::has_out_edge(int a, int b){
	return adj_out_set[a].find(b) != adj_out_set[a].end();
}

bool DirectedGraph::has_in_edge(int a, int b){
	return adj_out_set[b].find(a) != adj_out_set[b].end();
}

int DirectedGraph::get_n(){
	return n;
}

