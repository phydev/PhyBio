#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

    This file is part of Phybio.

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

from scipy import array, zeros, floor
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
            s[0] = check_boundary(s[0], self.L0[0], self.L1[0], self.B0[0], self.B1[0])
            s[1] = check_boundary(s[1], self.L0[1], self.L1[1], self.B0[1], self.B1[1])
            s[2] = check_boundary(s[2], self.L0[2], self.L1[2], self.B0[2], self.B1[2])
            return self.a[s[0],s[1],s[2]]
        else:
            i,j,k = index
            i = check_boundary(i, self.L0[0], self.L1[0], self.B0[0], self.B1[0])
            j = check_boundary(j, self.L0[1], self.L1[1], self.B0[1], self.B1[1])
            k = check_boundary(k, self.L0[2], self.L1[2], self.B0[2], self.B1[2])
            
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
            file.write(str(self(i))+' '.rstrip('\n'))
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
    laplacian_value = 0.0
    
    for i in range(0,phi.dim):
       
        s[i] += 1
        yh = phi[s[0],s[1],s[2]]
        s[i] -= 2
        yl = phi[s[0],s[1],s[2]]
        s[i] +=1         
        weight = 1.0/(phi.dr*phi.dr)
        laplacian_value += (yh + yl - 2.0*y) * weight

    return lapl



def gradient(phi,index):
    gradient_value = array((0.0,0.0,0.0))
    s = phi.position(index)
    

    for i in range(0,phi.dim):
        s[i] += 1
        yh = phi[s[0],s[1],s[2]]
        s[i] -= 2
        yl = phi[s[0],s[1],s[2]]
        s[i] += 1

        weight = 1.0 / (2.0 * phi.dr);
        gradient_value[i] = weight * (yh - yl);
        
    return gradient_value


def divergence(u):
    divergence_value = 0.0
    
    return divergence_value

def shortcuts():
    # defining functions shortcuts
    global lapl  # the laplacian function can be called as lapl() or laplacian()
    global grad  # the gradient function can be called as grad() or gradient()
    global div  # the divergence function can be called as div() or divergence()
    lapl = laplacian
    grad = gradient
    div = divergence 
    return
    
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

