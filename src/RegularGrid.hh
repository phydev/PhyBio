#ifndef REGULARGRID_HH
#define REGULARGRID_HH


namespace phybio
{

template <int dim, typename T> class grid;


template <int dim, typename T>
class grid{
public:
	
	grid(int vector_dim, int Lmax[dim], int BCondition[dim]);

	grid(); // blank grid

	~grid(); // destructor

	

protected:

	#define dimMax 3

	T* data;
	int field_dim;
	int vector_dim[dimMax];
	int length[dimMax];
	int bc[dimMax];
	int np;



}; // class grid
} // namespace

#include "RegularGrid.cc"
#endif
