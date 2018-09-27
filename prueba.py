#!/usr/bin/env python3
import numpy as np
import argparse


def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-p',metavar='',help='solo prueba',action='append',nargs='+',dest='collection')#,type=string)
	args = parser.parse_args()
	a = np.array(args.collection,dtype=object)
	first = a[0,0]
	dict = {first:[]}
	for i in a:
		p = i[0]
		q = i[1:]; q = list(map(float,q))
		if p in dict:
			dict[p].append(q)
		if p not in dict:
			dict[p] = [q]
	g = dict.keys()
	for i in g:
		base = dict[str(i)]
		print(i,base)
if __name__ == '__main__':
	Main()
