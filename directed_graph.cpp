
#include "directed_graph.hh"

DirectedGraph::DirectedGraph(PyArrayObject* rows, PyArrayObject* cols){

    /* Nonzero boolean function */
    PyArray_NonzeroFunc* nonzero = PyArray_DESCR(rows)->f->nonzero;
    PyArray_GetItemFunc* getitem = PyArray_DESCR(rows)->f->getitem;

    NpyIter* iter;
    NpyIter_IterNextFunc *iternext;
    char** dataptr;
    npy_intp* strideptr,* innersizeptr;

    iter = NpyIter_New(rows, NPY_ITER_READONLY|
                             NPY_ITER_EXTERNAL_LOOP|
                             NPY_ITER_REFS_OK,
                             NPY_KEEPORDER, NPY_NO_CASTING,
                             NULL);

    iternext = NpyIter_GetIterNext(iter, NULL);
    
    /* The location of the data pointer which the iterator may update */
    dataptr = NpyIter_GetDataPtrArray(iter);
    /* The location of the stride which the iterator may update */
    strideptr = NpyIter_GetInnerStrideArray(iter);
    /* The location of the inner loop size which the iterator may update */
    innersizeptr = NpyIter_GetInnerLoopSizePtr(iter);

    int nonzero_count = 0;

    do {
        /* Get the inner loop data/stride/count values */
        char* data = *dataptr;
        npy_intp stride = *strideptr;
        npy_intp count = *innersizeptr;

        /* This is a typical inner loop for NPY_ITER_EXTERNAL_LOOP */
        while (count--) {
	
    	    /* std::cout<<"val"<< PyLong_Check(getitem(data,rows))<<std::endl; */
    	    std::cout<<"val: "<< PyLong_AsLong(getitem(data,rows))<<std::endl;
            if (nonzero(data, rows)) {
                ++nonzero_count;
            }
            data += stride;
        }

        /* Increment the iterator to the next inner loop */
    } while(iternext(iter));

    std::cout<<"counnt"<<nonzero_count<<std::endl;

    NpyIter_Deallocate(iter);


}

std::vector<int>* DirectedGraph::get_successors(int node){
	return &adj_out[node];
}

std::vector<int>* DirectedGraph::get_predecessors(int node){
	return &adj_in[node];
}
