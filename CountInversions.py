#!/usr/bin/python

##Couting split inversions in an array by using Merge-Sort
##Compares performance of Merge-Sort with brute force algorithm
#Merge-Sort runs in nlogn time ,whereas brute force runs on n^2 time. 
# prashanthps <at> gmail <dot> com

import sys
import time as TT
import random as RR

def Sort_Count(A, n):

	if n == 1:
		return A, 0
	else:
		leftA = A[:(n/2)]
		rightA = A[n/2:]
		(C, x) = Sort_Count(leftA, len(leftA))
		#print 'C is ', C
		(D, y) = Sort_Count(rightA, len(rightA))
		#print 'D is ', D
		(E, z) = Merge_CountSplitInv(C, D)
		splitinversions = x+y+z
		#print 'E and n are', E, n
		return E, splitinverstions



def Merge_CountSplitInv(C, D):
	#Assumes C and D are sorted arrays
	n = len(C) + len(D)
	A = []
	splitinversions = 0
	i = 0
	j = 0
	for k in range(n):
		#print k, i, j
		if (i < len(C))&(j < len(D)):
			if C[i] < D[j]:
				A.append(C[i])
				i = i+1
			else:
				A.append(D[j])
				j = j+1
				splitinversions = splitinversions+(len(C)-i)

		elif (j == len(D))&(i < len(C)):
			A.append(C[i])
			i = i+1
		elif (i == len(C))&(j < len(D)):
			A.append(D[j])
			j = j+1
	

	return A, splitinversions 


def Brute(A):
	n = len(A)
	splits = 0
	#with open('Register.txt', 'w') as myfile:
	for i in range(n-1):
		for j in range(i+1, n):
			if A[i] > A[j]:
				splits = splits+1
				#blurb = str(i) + ',' + str(j) + '\n'
				#myfile.write(blurb)

	return splits

def main():

	argslen = len(sys.argv)

	if argslen != 2:
		print 'usage: n, where n is the number of elements in your array. '
		#print argslen
		sys.exit(1)
	else:
		n = int(sys.argv[1])

	#with open('IntegerArray.txt', 'rU') as f:
		#E = [2,3,4,5, 1]
		#Read contents of file and put each line as an element in a list
		#E = []
		#for line in f:
		#	E.append(int(line))

		#n = len(E)
		#print 'Length of input is', n
		#n = 10000
	E = RR.sample(range(n),n)
		
	#Set up timing
	s1 = TT.time()
	(A, splits) = Sort_Count(E, n)
	s2 = TT.time()
	print 'The number of split inversions by divide and conquer algo is: \t', splits, '\tTime taken:', s2-s1

	# Comment out the next 4 lines if you are not interested in time taken by the brute force algorithm
	s1 = TT.time()
	brutesplits = Brute(E)
	s2 = TT.time()
	print 'The number of split inversions by brute force method: \t\t', brutesplits, '\tTime taken:', s2-s1

	#(E, n) = Merge_CountSplitInv(C,D)
	#print E, n


if __name__ == '__main__':
  main()