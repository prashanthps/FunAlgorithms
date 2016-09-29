#!/usr/bin/python

##Counting comparisons in QuickSort
## In place swaps used for better memory utilization
## Three different ways to choose a Pivot
# prashanthps <at> gmail <dot> com

import sys
import random as RR

def QuickSort(A, n, opt):

	if n==1:
		return A, 0
	else:
		comparisons = 0
		
		(A, p) = ChoosePivot(A,opt)

		#print "\nA is \n", A
		#p = A[0]
		#print "\n p is \n", p

		##code to partition A around p .. compute partitioned sub arrays for recursive calls
		l = 0
		r = len(A)-1
		i = l+1
		for j in range(l+1,r+1):
			if A[j] < p:
				A[i], A[j] = A[j], A[i]
				i = i+1
		
		A[l], A[i-1] = A[i-1], A[l]
		
		lsub1 = 0
		rsub1 = i-1
		lsub2 = i
		rsub2 = len(A)
		#print lsub1, rsub1, lsub2, rsub2

		comparisons = comparisons + (n - 1)
		x = 0
		y = 0
		if (rsub1) > 0:
			(C, x) = QuickSort(A[lsub1:rsub1], len(A[lsub1:rsub1]), opt)
		#	print 'x is ', x
		if (rsub2-lsub2) > 0:
			(D, y) = QuickSort(A[lsub2:rsub2], len(A[lsub2:rsub2]), opt)
		#	print 'y is', y
		comparisons = comparisons + x + y

	return A, comparisons


def median(a,b,c):
	#Return median of a, b, c
	if (a<b):
		if (b<c):
			return b
		elif (a<c):
			return c
		else:
			return a
	else:
		if (b>c):
			return b
		elif (a<c):
			return a
		else:
			return c




def ChoosePivot(A,opt):
	if opt == 1:
		return A, A[0]
	elif opt == 2:
		#After choosing pivot, swap it with the first element of the array, and proceed as with option 1
		p = A[-1]
		A[0], A[-1] = A[-1], A[0]
		return A, p

	else:
		#First determine if length of array is odd or even in order to choose the middle element correctly
		if (len(A)%2)==0:
			a = A[0]
			b = A[(len(A)/2)-1]
			c = A[-1]
			p = median(a,b,c)
			#After choosing pivot, swap it with the first element of the array, and proceed as with option 1
			if p == b:
				A[0], A[(len(A)/2)-1] = A[(len(A)/2)-1], A[0]
			elif p == c:
				A[0], A[-1] = A[-1], A[0]

			return A, p

		else:
			a = A[0]
			b = A[len(A)/2]
			c = A[-1]
			p = median(a,b,c)
			#After choosing pivot, swap it with the first element of the array, and proceed as with option 1
			if p == b:
				A[0], A[(len(A)/2)] = A[(len(A)/2)], A[0]
			elif p == c:
				A[0], A[-1] = A[-1], A[0]

			return A, p





def main():

	argslen = len(sys.argv)

	if argslen != 3:
		print 'usage: n, opt ;where n is the number of elements in your array and opt is either 1 or 2 or 3 for choosing your Pivot. '
		print 'opt=1 for choosing Pivot as the first element in the array'
		print 'opt=2 for choosing Pivot as the last element of the array'
		print 'opt=3 for choosing Pivot as the median between the First, Middle and Last elements of the array'
		print 'opt=4 for running the code for all three cases above'
		#print argslen
		sys.exit(1)
	else:
		n = int(sys.argv[1])
		opt = int(sys.argv[2])
		E = RR.sample(range(n),n)

	#Uncomment the following lines in case your random numbers in a file called QuickSort.txt and you want to pass that as an Input.
	#with open('QuickSort.txt', 'rU') as f:
		#E = [2,3,4,5, 1]
		#Read contents of file and put each line as an element in a list
	#	E = []
	#	for line in f:
	#		E.append(int(line))

	#	n = len(E)
	#	print 'Length of input is', n
	
	if opt != 4:
		(A, comparisons) = QuickSort(E, len(E), opt)
		print '\nThe number of comparisons in QuickSort algo is: \t', comparisons, '\t\n'
	else:
		(A, comparisons1) = QuickSort(E, len(E), 1)
		(B, comparisons2) = QuickSort(E, len(E), 2)
		(C, comparisons3) = QuickSort(E, len(E), 3)
		print '\nThe number of comparisons in QuickSort algo by choosing the first element of the array as Pivot, is: \t\t\t', comparisons1, '\n'
		print '\nThe number of comparisons in QuickSort algo by choosing the last element of the array as Pivot, is: \t\t\t', comparisons2, '\n'
		print '\nThe number of comparisons in QuickSort algo by choosing the median of First, Middle and Last elements of the array as Pivot, is:', comparisons3, '\n'


if __name__ == '__main__':
  main()
