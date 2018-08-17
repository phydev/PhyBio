#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

    This file is part of PhyBio.

    PhyBio is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PhyBio is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PhyBio.  If not, see <https://www.gnu.org/licenses/>.
    
@author: moreira
"""

import sys
sys.path.insert(0, '../phybio')
from phybio import *
from scipy import copy, random

# Example: Allen-Cahn Equation

L = [50,50,1]  # defining the simulation box length
phi = grid3d(L[0],L[1],L[2]) # creating the 3d grid
phit = grid3d(L[0],L[1],L[2]) # copy of the phi grid
nstep = 0 # actual time step
tstep = 100 # total number of steps
dt = 0.005  # time interval
nprint = 0 # counter to output data

phi.a = random.rand(L[0],L[1],L[2]) # filling the grid with a uniform random distribution

# main loop of integration
while(nstep<=tstep): # this loop is integrating the Allen-Cahn function in time 
    
    # this for loop goes over all the grid points and integrate each one of them
    for i in range(0,phi.nodes):
        # the Euler method is used here, it is well behaved for diffusion-like equations
        # f(t+dt) = f(t) + dt( Lapl(phi) + f(t)*(1-f(t))(0.5 -f(t) )
        phit[i] = phi[i] + dt*( laplacian(phi,i) + phi[i]*(1.0-phi[i])*(phi[i] -0.5 ) )
        
    phi.a = copy(phit.a) # updating value of phi after the integration
    nstep+=1
    nprint+=1
    if(nprint>=10):
        print(nstep)
        nprint=0
        phi.output('out'+str(nstep)+'.vti') # PhyBio has an output function that prints the grid in the VTK format