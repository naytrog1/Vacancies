#!/usr/bin/env python3
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')
'''Constantes'''
a =  1 #Lattice Constant
x0 = 0; y0 = 0; z0 = 0 #Start Point
'''Start Cube'''
XL = np.array([x0]) #X List
YL = np.array([y0]) #Y List
ZL = np.array([z0]) #Z List
copiesX = 1; copiesY = 1; copiesZ = 1 #Generate Starting Cube
'''Simple Cubic Lattice Cells Function'''
def SCLattice(XL,YL,ZL,copiesX,copiesY,copiesZ,a,x0,y0,z0):
	z = z0
	for i in range(copiesZ+1):
		y = y0
		for i in range(copiesY+1):
			for i in range(copiesX):
				x = x0 + a
				XL = np.append(XL,x)
				YL = np.append(YL,y)
				ZL = np.append(ZL,z)
				x0 = x
			x0 = 0
			y = y0 + a
			y0 = y
			XL = np.append(XL,x0)
			YL = np.append(YL,y0)
			ZL = np.append(ZL,z0)
		XL = np.delete(XL,len(XL)-1)
		YL = np.delete(YL,len(YL)-1)
		ZL = np.delete(ZL,len(ZL)-1)
		y = 0
		y0 = y
		z = z0 + a
		z0 = z
		XL = np.append(XL,x0)
		YL = np.append(YL,y0)
		ZL = np.append(ZL,z0)
	XL = np.delete(XL,len(XL)-1)
	YL = np.delete(YL,len(YL)-1)
	ZL = np.delete(ZL,len(ZL)-1)
	return XL,YL,ZL
XL,YL,ZL = SCLattice(XL,YL,ZL,copiesX,copiesY,copiesZ,a,x0,y0,z0)
'''Computes'''
copiesX += 1; copiesY += 1; copiesZ += 1 #Number of Copies on Each Direction
XL,YL,ZL = SCLattice(XL,YL,ZL,copiesX,copiesY,copiesZ,a,x0,y0,z0)
np.savetxt('Simple Cubic.xyz',np.c_[XL,YL,ZL],fmt='%10.5f')
ax.scatter(XL,YL,ZL,s=100)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()