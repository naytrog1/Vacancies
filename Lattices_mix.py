#!/usr/bin/env python3
import numpy as np
import argparse
#vmd gdis xmakemol xcrysden vesta vasp. Programs to vizualize.

'''Cubic Lattice Cells Function'''

def Lattice(Atom,Base,a,NX,NY,NZ):
	Matrix = np.empty((0,3),object) #Empty matrix array, data type object to combine string and floats.

	Base = np.array(Base, float)
	Base = Base * a

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

def Vacancies_Lattice(N_atoms,Matrix,Pvacancies):

	r = (N_atoms*Pvacancies)*.01 #Percentage of atoms to remove

	r = int(r) 	#Integer below, closest to percentage

	for i in range(r):
		k = np.random.randint(N_atoms-i) #index decreasing on each loop
		Matrix = np.delete(Matrix,k,0) #new matrix without the atom corresponding to the index
	N_atoms = N_atoms - r
	return N_atoms, Matrix

def Main():
	parser = argparse.ArgumentParser(description='Script to create and output perfect and vacancies lattices to a xyz file',\
				epilog="If you want to create vacancies, type: -v [Percentage of vacancies], dtype = float")
	
	'''Required Arguments'''

	#parser.add_argument("-e","--Element",metavar='',help="Quimical Element",required=True,type=str)
	#parser.add_argument("-b","--Base",metavar='',help="Element Base",required=True,type=list)
	parser.add_argument("-eb",metavar='',help='Quimical Element and Base of it',required=True,action='append',nargs='+',dest='Bases')
	parser.add_argument("-a","--Constant",metavar='',help="Lattice Constant",required=True,type=float)
	parser.add_argument("-nx","--NX",metavar='',help="Copies in X",required=True,type=int)
	parser.add_argument("-ny","--NY",metavar='',help="Copies in Y",required=True,type=int)
	parser.add_argument("-nz","--NZ",metavar='',help="Copies in Z",required=True,type=int)
	parser.add_argument("-o","--Outputs",metavar='',help="Number of Outputs",required=True,type=int)

	'''Optional Arguments'''
	
	parser.add_argument("-v","--Pvacancies",metavar='',help="Create the percentage of vacancies",type=float)

	'''working'''
	
	args = parser.parse_args()
	a = np.array(args.Bases,dtype=object)
	first = a[0,0] 	#first element on command line
	dict = {first:[]}
	for i in a:
		p = i[0]
		q = i[1:]; q = list(map(float,q))
		if p in dict:
			dict[p].append(q)
		if p not in dict:
			dict[p] = [q]
	g = dict.keys() #Quimical Elements are the keys in the dictionary

	for j in g:
		Base = dict[str(j)]
		Element = j
		print(Element,Base)

		for i in range(args.Outputs):
			print(i)

			N_atoms, Matrix = Lattice(Element,Base,args.Constant,args.NX,args.NY,args.NZ)
			
			'''Save the perfect Latticce'''

			#np.savetxt(args.Element+'-'+args.Type+'-perfect-output_'+str(i+1)+'.xyz',Matrix,fmt="%s %5.4f %5.4f %5.4f", \
			#				header=str(N_atoms)+'\n', comments="")

			'''Save the Latticce with vacancies'''

			if args.Pvacancies:

				N_atoms, Matrix = Vacancies_Lattice(N_atoms,Matrix,args.Pvacancies)
				np.savetxt(str(Element)+'-vacancies-output_'+str(i+1)+'.xyz',Matrix,fmt="%s %5.4f %5.4f %5.4f", \
							header=str(N_atoms)+'\n', comments="")

if __name__ == '__main__':
	Main()




