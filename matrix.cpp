
#include "matrix.hh"

Matrix::Matrix(int n){
    adj.resize(n, std::unordered_set<int>());	
}


/* void Matrix::increment_from_to(int a, int b){ */
/* 	/1* // check if key `b` exists in the map or not *1/ */
/*         /1* it = adj[a].find(b); *1/ */
 
/*         /1* // key already present on the map *1/ */
/*         /1* if (it != freq.end()) { *1/ */
/*             /1* it->second++;    // increment map's value for key `b` *1/ */
/*         /1* } *1/ */
/*         /1* // key not found *1/ */
/*         /1* else { *1/ */
/*             /1* adj[a].insert(std::make_pair(b, 1)); *1/ */
/*         /1* } *1/ */
/* } */
/* void Matrix::increment_all_2_all(int a, int b, int c){ */
	
/* 	increment_from_to(a, b); */
/* 	increment_from_to(a, c); */
	
/* 	increment_from_to(b, a); */
/* 	increment_from_to(b, c); */
	
/* 	increment_from_to(c, a); */
/* 	increment_from_to(c, b); */
/* } */
void Matrix::increment_all_2_all(int a, int b, int c, int d){

	/* increment_from_to(a, b); */
	/* increment_from_to(a, c); */
	/* increment_from_to(a, d); */
	
	/* increment_from_to(b, a); */
	/* increment_from_to(b, c); */
	/* increment_from_to(b, d); */
	
	/* increment_from_to(c, a); */
	/* increment_from_to(c, b); */
	/* increment_from_to(c, d); */

}
