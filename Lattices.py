#!/usr/bin/env python3
import numpy as np
import argparse
'''Atom Name'''
#Atom = 'Au'
'''Constants'''
#a =  3.7 #Lattice Constant
#NX, NY, NZ = 10,10,5 #Number of copies on each direction
#Type = 'fcc'
#vacancies = 50

#vmd gdis xmakemol xcrysden vesta

'''Cubic Lattice Cells Function'''

def Lattice(Atom,Type,a,NX,NY,NZ):
	Matrix = np.empty((0,3),object) #object to combine string and floats
	if Type == 'sc':
		Base = np.array([[0,0,0]], float)
		Base = Base*a
	elif Type == 'bcc':
		Base = np.array([[0,0,0],[0.5,0.5,0.5]], float)
		Base = Base*a
	elif Type == 'fcc':
		Base = np.array([[0,0,0],[0.0,0.5,0.5],[0.5,0.0,0.5],[0.5,0.5,0.0]], float)
		Base = Base*a
	else: raise ValueError('Not a Supported(or Valid) Lattice')

	'''Unitary Cell'''
	uc = np.array([[a,0,0],[0,a,0],[0,0,a]])

	N_atoms = 0 #count the number of atoms
	for k in range(NZ):
		for j in range(NY):
			for i in range(NX):
				s = i*uc[0] + j*uc[1] + k*uc[2]
				for l in Base:
					N_atoms +=1
					p = s+l
					Matrix = np.vstack((Matrix,p))
	AtomL = np.tile(Atom,Matrix.shape[0])[None].T #create a tanposed row with the name of the atom
	Matrix = np.hstack([AtomL,Matrix]) # add the column made above to the matrix
	return N_atoms,Matrix
#N_atoms, Matrix = Lattice(Atom,Type,a,NX,NY,NZ)

'''Save the perfect Latticce'''
#np.savetxt(Atom+'-'+Type+'-perfect.xyz',Matrix,fmt="%s %5.4f %5.4f %5.4f",header=str(N_atoms)+'\n', comments="")

'''Function that Make vacancies'''

def Vacancies_Lattice(N_atoms,Matrix,vacancies):
	for i in range(vacancies):
		k = np.random.randint(N_atoms-i) #index decreasing on each loop
		Matrix = np.delete(Matrix,k,0) #new matrix without the atom corresponding to the index
	N_atoms = N_atoms - vacancies
	return N_atoms, Matrix

#N_atoms, Matrix = Vacancies_Lattice(N_atoms,Matrix,vacancies)

'''Save the Latticce with vacancies'''

#np.savetxt(Atom+'-'+Type+'-vacancies.xyz',Matrix,fmt="%s %5.4f %5.4f %5.4f",header=str(N_atoms)+'\n', comments="")

def Main():
	parser = argparse.ArgumentParser()

	parser.add_argument("Element",help="Quimical Element",type=str)
	parser.add_argument("Type",help="Lattice Type",type=str)
	parser.add_argument("Constant",help="Lattice Constant",type=float)
	parser.add_argument("NX",help="Copies in X",type=int)
	parser.add_argument("NY",help="Copies in Y",type=int)
	parser.add_argument("NZ",help="Copies in Z",type=int)

	args = parser.parse_args()

	N_atoms, Matrix = Lattice(args.Element,args.Type,args.Constant,args.NX,args.NY,args.NZ)
	print(N_atoms)
	print(Matrix)

if __name__ == '__main__':
	Main()




