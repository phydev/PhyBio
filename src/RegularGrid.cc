#include "RegularGrid.hh"
#include <cstdlib>
#include <cstdio>

grid2D::grid2D(){
	
	length[0] = 0;
	length[1] = 0;
	periodic[0] = false;
	periodic[1] = false;
	data = NULL;
}

grid2D::grid2D(int Lx,int Ly){
	
	length[0] = Lx;
	length[1] = Ly;
	periodic[0] = false;
	periodic[1] = false;
	data = new double [Lx*Ly];
	for (int i=0;i<Lx*Ly;++i) data[i] = 0;
}

grid2D::grid2D(int L){
	
	length[0] = L;
	length[1] = L;
	periodic[0] = false;
	periodic[1] = false;
	data = new double [L*L];
	for (int i=0;i<L*L;++i) data[i] = 0;
}

grid2D::~grid2D(){
	
	double *aux;
	if (data) {aux = data; delete [] aux; data = NULL;}
}

void grid2D::resize(int newLx, int newLy){
	
	double* aux = data;
	data = new double [newLx*newLy];
	length[0] = newLx;
	length[1] = newLy;
	for (int i=0;i<newLx*newLy;++i) data[i] = 0;
	
	delete [] aux;
}

void grid2D::setPeriodic(int dimRef, bool isPeriodic){
	
	if (dimRef < 1){printf("Dimension error. Aborted.\n");return;}
	
	if (dimRef > 2){printf("Dimension error. Aborted.\n");return;}
	
	periodic[dimRef-1] = isPeriodic;
}

void grid2D::setPeriodic(char dimRefChar, bool isPeriodic){
	
	if (dimRefChar == 'x' || dimRefChar == 'X')
		{setPeriodic(1,isPeriodic); return;}
	if (dimRefChar == 'y' || dimRefChar == 'Y')
		{setPeriodic(2,isPeriodic); return;}
	
	printf("Use 'x' or 'y'. Aborted.\n");
}

void grid2D::setPeriodic(bool isPeriodicX, bool isPeriodicY){
	
	periodic[0] = isPeriodicX;
	periodic[1] = isPeriodicY;
}

grid2D& grid2D::operator=(const grid2D& other){
	
	length[0] = other.length[0];
	length[1] = other.length[1];
	
	periodic[0] = other.periodic[0];
	periodic[1] = other.periodic[1];
	
	double* aux = data;
	data = other.data;
	delete [] aux;
	
	return  *this;
}

double& grid2D::operator()(int i, int j){
	
	return data[i*length[1] + j];
}

const double& grid2D::operator()(int i, int j){
	
	return data[i*length[1] + j];
}
