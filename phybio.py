#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 00:26:02 2018

@author: moreira
"""
import vtk
from scipy import array, zeros, floor, sqrt, copy
import sys


class grid3d(object):

    
    def __init__(self,lx,ly,lz):  
        self.a = zeros((lx,ly,lz))
        self.dim = 3
        self.dr = 1.0
        self.L0 = array((0,0,0))  # indexes - 0 -> x; 1 -> y; 2 -> z;
        self.L1 = array((lx,ly,lz))
        self.B0 = array(('periodic','periodic','periodic')) # lower bound boundary conditions
        self.B1 = array(('periodic','periodic','periodic')) # upper bound boundary conditions
        self.nodes = self.L1[0]*self.L1[1]*self.L1[2]

    def __getitem__(self,index): # __getitem__ only accepts one argument
                                 # we can pass the others as a tuple                            
        if(type(index)==int):
            s = self.position(index) # index = (x + Nx* (y + Ny* z))
            s[0] = check_boundary(s[0], phi.L0[0], phi.L1[0], phi.B0[0], phi.B1[0])
            s[1] = check_boundary(s[1], phi.L0[1], phi.L1[1], phi.B0[1], phi.B1[1])
            s[2] = check_boundary(s[2], phi.L0[2], phi.L1[2], phi.B0[2], phi.B1[2])
            return self.a[s[0],s[1],s[2]]
        else:
            i,j,k = index
            i = check_boundary(i, phi.L0[0], phi.L1[0], phi.B0[0], phi.B1[0])
            j = check_boundary(j, phi.L0[1], phi.L1[1], phi.B0[1], phi.B1[1])
            k = check_boundary(k, phi.L0[2], phi.L1[2], phi.B0[2], phi.B1[2])
            
            return self.a[i][j][k]

    def __setitem__(self,index,value):
        if(type(index)==int):
            s = self.position(index)
            self.a[s[0],s[1],s[2]] = value
        else:
            i,j,k = index
            self.a[i,j,k] = value
    
    def __call__(self,index):
        return self.a.item(index)

    def __index__(self):
        return
    
    def position(self,index):
        if(index<self.nodes):
            k = floor(index/(self.L1[0]*self.L1[1]))      
            j = floor((index - k*self.L1[0]*self.L1[1])/self.L1[0])
            i = index - self.L1[0]*j - k*self.L1[0]*self.L1[1]
            return array((int(i),int(j),int(k)))
        else:
            sys.exit("Error: Index out of bound!")
            
    def output(self,filename):
        file = open(filename, 'w+')
        file.write("<?xml version=\"1.0\"?>\n") 
        file.write("<VTKFile type=\"ImageData\" version=\"0.1\" byte_order=\"LittleEndian\">\n")
        file.write("  <ImageData WholeExtent=\""+str(self.L0[0])+" "+str(self.L1[0])+" "+str(self.L0[1])+" "+str(self.L1[1])+" "+str(self.L0[2])+" "+str(self.L1[2])+"\"   Origin=\"0 0 0\" Spacing=\"1 1 1\">\n")
        file.write("    <Piece Extent=\""+str(self.L0[0])+" "+str(self.L1[0])+" "+str(self.L0[1])+" "+str(self.L1[1])+" "+str(self.L0[2])+" "+str(self.L1[2])+"\">\n")
        file.write("      <CellData> \n")
        file.write("        <DataArray Name=\"scalar_data\" type=\"Float64\" format=\"ascii\">\n")
        for i in range(0,self.nodes):
            file.write(str(phi(i))+' '.rstrip('\n'))
        file.write("\n")
        file.write("         </DataArray> \n")    
        file.write("      </CellData> \n")
        file.write("    </Piece> \n")
        file.write("</ImageData> \n")
        file.write("</VTKFile> \n")
        file.close()
        return

    def __add__(self, other):
        return self.a + other.a
    
    def __mul__(self,right):
        return self.a*right
    
def laplacian(phi,index):
    s = phi.position(index)
    y = phi[index]
    lapl = 0.0
    
    for i in range(0,phi.dim):
       
        s[i] += 1
        yh = phi[s[0],s[1],s[2]]
        s[i] -= 2
        yl = phi[s[0],s[1],s[2]]
        s[i] +=1         
        weight = 1.0/(phi.dr*phi.dr)
        lapl += (yh + yl - 2.0*y) * weight

    return lapl
    


def check_boundary(x, x0, x1, b0, b1):
    if(x<x0):
        if (b0 == 'Neumann' or b0 == 'Dirichlet'): 
            x = x0
        elif (b0 == 'periodic'):
            x = x1 - (x0 - x)
        elif (b0 == 'mirror'):
            x = 2 * x0 - x
    elif(x>=x1):
        if (b1 == 'Neumann' or b1 == 'Dirichlet'):
            x = (x1 - 1)
        elif (b1 == 'periodic'):
            x = x0 + (x - x1)
    return x




L = [20,20,20]
phi = grid3d(L[0],L[1],L[2])
phit = grid3d(L[0],L[1],L[2])
phit.a = copy(phi.a)

for i in range(0,phi.nodes):
    s = phi.position(i)
    if(sqrt( (s[0]-L[0]/2)**2 + (s[1]-L[1]/2)**2 + (s[2]-L[2]/2)**2   )  <4.0):
        phi[i] = 1.0



nstep = 0
tstep = 0
dt = 0.005
nprint = 0
while(nstep<=tstep):
    
    for i in range(0,phi.nodes):
        phit[i] = phi[i] + dt*( laplacian(phi,i) + phi[i]*(1.0-phi[i])*(0.5 - phi[i] ) )
        
    phi.a = copy(phit.a)
    nstep+=1
    nprint+=1
    print(nstep)
    if(nprint>=100):
        nprint=0
        
        phi.output('out'+str(nstep)+'.vti')
    
