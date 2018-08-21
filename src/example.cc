//#include "example.hh"
#include<iostream>
#include "RegularGrid.hh"

using namespace phybio;



// Code here
int main(int argc, char* argv[]) {
	
	int dim = atoi(argv[1]);

	int L[2];
	int bc[2];

	L[0] = 10;
	L[1] = 10;
	bc[0] = 0;
	bc[1] = 0;

	grid<2,double> f(2,L,bc);


}