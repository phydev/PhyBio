#ifndef REGULARGRID_HH
#define REGULARGRID_HH

// I'm pretty sure an N dimensional grid can easily
// be achieved by a recursive template. But for us
// this should be much more straight-forward. And
// SWIG won't give us a headache...

class grid2D{
private:
	
	int length [2];
	bool periodic [2];
	double* data;
public:
	
	grid2D();
	grid2D(int,int);
	grid2D(int);
	~grid2D();
	void resize(int,int);
	void setPeriodic(int,bool);
	void setPeriodic(char,bool);
	void setPeriodic(bool,bool);
	
	grid2D& operator=(const grid2D&);
	double& operator()(int,int);
	const double& operator()(int,int);
};

#endif
