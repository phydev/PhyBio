
#include <cstdlib>
#include <cstdio>
#include "RegularGrid.hh"


namespace phybio{

// initializes a NULL grid object 
template<int dim,typename T>
grid<dim,T>::grid(){

//	length =  new int [dim];
//	bc = new int [dim];

	
	for (int i=0; i<dim; i++){
		length[i] = 0;
		bc[i] = 0;
	}

	data = NULL;
}

template<int dim,typename T>
grid<dim,T>::grid(int vector_dim, int Lmax[dim], int BCondition[dim]){

	// boundary conditions options:
	// periodic  = 0 (default); Neumann   = 1; mirror    = 2; Dirichlet = 3
	field_dim = vector_dim;


	np = 1;

	for (int i=0; i<dim; i++){
		length[i] = Lmax[i];
		bc[i] = BCondition[dim];
		np = np*Lmax[i];
	}
	
	data = new T [np];

	for (int i=0;i<np;++i){ data[i] = 0;}

}

// destructor
template<int dim,typename T>
grid<dim,T>::~grid(){
	
	double *aux;
	if (data) {
		aux = data; 
		delete [] aux; 
		data = NULL;
	}
}



} // namespace