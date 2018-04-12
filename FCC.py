#!/usr/bin/env python3
import numpy as np

'''Constants'''
a =  1 #Lattice Constant

'''Start Cube'''
XL = np.array([]) #X List
YL = np.array([]) #Y List
ZL = np.array([]) #Z List
copiesX = 50; copiesY = 50; copiesZ = 50 #Generate Starting Cube
'''Face Centered Cubic Lattice Cells Function'''

def FCCLattice(a,XL,YL,ZL,copiesX,copiesY,copiesZ):
	a0 = np.array([0,0,0])
	a1 = np.array([0,.5,.5])*a
	a2 = np.array([.5,0,.5])*a
	a3 = np.array([.5,.5,0])*a
	for i in range(copiesZ+1):
		for i in range(copiesY+1):
			for i in range(copiesX+1):
				XL = np.append(XL,[a0[0],a1[0],a2[0],a3[0]])
				YL = np.append(YL,[a0[1],a1[1],a2[1],a3[1]])
				ZL = np.append(ZL,[a0[2],a1[2],a2[2],a3[2]])
				a0[0] += a; a1[0] += a; a2[0] += a; a3[0] += a
			a0[1] += a; a1[1] += a; a2[1] += a; a3[1] += a
			a0[0] = 0; a1[0] = 0; a2[0] = .5*a; a3[0] = .5*a
		a0[2] += a; a1[2] += a; a2[2] += a; a3[2] += a
		a0[1] = 0; a1[1] = .5*a; a2[1] = 0; a3[1] = .5*a
	return XL,YL,ZL
XL,YL,ZL = FCCLattice(a,XL,YL,ZL,copiesX,copiesY,copiesZ)
np.savetxt('Face Centered Cubic.xyz',np.c_[XL,YL,ZL],fmt='%10.5f')