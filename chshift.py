#!/usr/bin/env python
import sys
import numpy as np
inp=open(sys.argv[1],'r')
ref=open(sys.argv[2],'r')
atom=sys.argv[3]
lstref=list()
print("ref")
for line in ref:
	if 'Isotropic' in line:
		sp=line.split()
		if sp[1]==atom:
			print(line.replace('\n',''))	
			lstref.append(float(sp[4]))
print('isotropic values of reference')
print(lstref)
isoref=np.mean(np.asarray(lstref))
print('mean isotropic value of reference is ' + str(isoref)+'\n')
print('file')
for line in inp:
	if 'Isotropic'in line:
		sp=line.split()
		if sp[1]==atom:
			print(line.replace('\n',''))
			isoat=float(sp[4])
			print('chemical shift is ' + str(isoref-isoat)+'\n')
