
#include "directed_graph.hh"

DirectedGraph::DirectedGraph(PyArrayObject* rows, PyArrayObject* cols){

    NpyIter* iter;
    NpyIter_IterNextFunc *iternext;
    char** dataptr;
    npy_intp* strideptr,* innersizeptr;

    /* std::cout << "check a: " << **rows << std::endl; */
    int d = PyArray_NDIM(rows);

    std::cout << "check a: "<< d<< std::endl;
    iter = NpyIter_New(rows, NPY_ITER_READONLY, NPY_KEEPORDER, NPY_NO_CASTING, NULL);
    
    std::cout << "check a: "<< d<< std::endl;
    /* iter = NpyIter_New(cols, NPY_ITER_READONLY| */
                             /* NPY_ITER_EXTERNAL_LOOP| */
                             /* NPY_ITER_REFS_OK, */
                             /* NPY_KEEPORDER, NPY_NO_CASTING, */
                             /* NULL); */
    /* if (iter == NULL) { */
    /*     return NULL; */
    /* } */

    /* iternext = NpyIter_GetIterNext(iter, NULL); */
    /* /1* if (iternext == NULL) { *1/ */
    /* /1*     NpyIter_Deallocate(iter); *1/ */
    /* /1*     return NULL; *1/ */
    /* /1* } *1/ */
    /* /1* The location of the data pointer which the iterator may update *1/ */
    /* dataptr = NpyIter_GetDataPtrArray(iter); */
    /* /1* The location of the stride which the iterator may update *1/ */
    /* strideptr = NpyIter_GetInnerStrideArray(iter); */
    /* /1* The location of the inner loop size which the iterator may update *1/ */
    /* innersizeptr = NpyIter_GetInnerLoopSizePtr(iter); */

    /* do { */
    /*     /1* Get the inner loop data/stride/count values *1/ */
    /*     char* data = *dataptr; */
    /*     npy_intp stride = *strideptr; */
    /*     npy_intp count = *innersizeptr; */

    /*     /1* This is a typical inner loop for NPY_ITER_EXTERNAL_LOOP *1/ */
    /*     while (count--) { */
	    /* std::cout << **dataptr << std::endl; */
    /*         /1* if (nonzero(data, self)) { *1/ */
    /*         /1*     ++nonzero_count; *1/ */
    /*         /1* } *1/ */
    /*         data += stride; */
    /*     } */

    /*     /1* Increment the iterator to the next inner loop *1/ */
    /* } while(iternext(iter)); */

    /* NpyIter_Deallocate(iter); */


}
