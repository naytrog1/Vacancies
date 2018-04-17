#!/usr/bin/env python3
import numpy as np
import argparse
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

'''Function that Make vacancies'''

def Vacancies_Lattice(N_atoms,Matrix,vacancies):
	for i in range(vacancies):
		k = np.random.randint(N_atoms-i) #index decreasing on each loop
		Matrix = np.delete(Matrix,k,0) #new matrix without the atom corresponding to the index
	N_atoms = N_atoms - vacancies
	return N_atoms, Matrix

def Main():
	parser = argparse.ArgumentParser(description='Script to create and output perfect and vacancies lattices to a xyz file' ,\
						epilog="If you want to create vacancies type: -v [number of vacancies]")
	'''Positional Arguments'''
	parser.add_argument("-e","--Element",metavar='',help="Quimical Element",required=True,type=str)
	parser.add_argument("-t","--Type",metavar='',help="Lattice Type",required=True,type=str)
	parser.add_argument("-a","--Constant",metavar='',help="Lattice Constant",required=True,type=float)
	parser.add_argument("-nx","--NX",metavar='',help="Copies in X",required=True,type=int)
	parser.add_argument("-ny","--NY",metavar='',help="Copies in Y",required=True,type=int)
	parser.add_argument("-nz","--NZ",metavar='',help="Copies in Z",required=True,type=int)

	'''Optional Arguments'''
	#parser.add_argument("-o","--output",help="Output the "+ \
	#					"result to a file",action="store_true")
	
	parser.add_argument("-v","--Vacancies",metavar='',help="Create the number of vacancies",type=int)

	args = parser.parse_args()

	N_atoms, Matrix = Lattice(args.Element,args.Type,args.Constant,args.NX,args.NY,args.NZ)
	
	'''Save the perfect Latticce'''

	np.savetxt(args.Element+'-'+args.Type+'-perfect.xyz',Matrix,fmt="%s %5.4f %5.4f %5.4f", \
					header=str(N_atoms)+'\n', comments="")

	'''Save the Latticce with vacancies'''

	if args.Vacancies:

		N_atoms, Matrix = Vacancies_Lattice(N_atoms,Matrix,args.Vacancies)
		np.savetxt(args.Element+'-'+args.Type+'-vacancies.xyz',Matrix,fmt="%s %5.4f %5.4f %5.4f", \
					header=str(N_atoms)+'\n', comments="")

if __name__ == '__main__':
	Main()




