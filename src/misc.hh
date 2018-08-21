// misc.hh - headers of the file misc.cc 

#include <cstdlib>
#include <cstdio>
#include<cstring>
#include<fstream>

namespace phybio{

enum {
	periodic  = 0,
	Neumann   = 1,
	mirror    = 2,
	Dirichlet = 3
};

// check boundary conditions and adjusts the coordinate x accordingly
// function adapted from https://github.com/mesoscale/mmsp/
void check_boundary(int& x, int x0, int x1, int b0, int b1);

}