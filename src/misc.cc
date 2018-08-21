// misc.cc - miscelaneous of recurrent routines used in the main code

#include "misc.hh"
#include <cstdlib>
#include <cstdio>
#include<cstring>
#include<fstream>


namespace phybio{

// check boundary conditions in a given direction for the coordenate point x
void check_boundary(int& x, int x1, int b0, int b1)
{
	// note: we are assuming that (X0,Y0,Z0) = vec(0), so the user must set the grid with origin on (0,0,0)
	if (x < 0) { // lower bound
		if (b0 == Neumann or b0 == Dirichlet) x = 0;
		else if (b0 == periodic) x = x1 + x;
		else if (b0 == mirror) x =  - x;
	} 
	else if (x >= x1) { // upper bound
		if (b1 == Neumann or b1 == Dirichlet) x = (x1 - 1);
		else if (b1 == periodic) x = x - x1;
		else if (b1 == mirror) x = 2 * (x1 - 1) - x;
	}
}
}