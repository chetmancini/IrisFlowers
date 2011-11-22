#######################################
######### Irises Classification #######
# Version: 0.1
#
# Author: Chet Mancini
# Email: cam479 at cornell dot edu
# Web: chetmancini.com
# Warranty: None at all
#
# CS4700, Fall 2011
# Cornell University
#
# Credits:
# Some code from: http://www.syntagmatic.net/matrix-multiplication-in-python/
#
#######################################

########### IMPORTS ###############
import copy

'''
Usage:
Matrix is a list of lists of doubles.

Vector is a list of doubles.
'''

'''
Create a zero matrix
'''
def zeroMatrix(rows, cols):
    return [[0.0 for col in range(cols)] for row in range(rows)]


'''
Transpose a matrix
'''
def transpose(matrix):
	tuples = zip(*matrix)
	toReturn = []
	for tup in tuples:
		toReturn.append(list(tup))

'''
Matrix addition
'''
def add(matrix1, matrix2):
	if len(matrix1) != len(matrix2):
		return None
	toReturn  = []
	for i in range(len(matrix1)):
		toAppend = []
		for j in range(len(matrix1[i])):
			toAppend.append(matrix1[i][j] + matrix2[i][j])
		toReturn.append(toAppend)
	return toReturn

'''
multiply a matrix by a scalar
'''
def multiplyScalar(matrix, scalar):
	return [[y * scalar for y in x] for x in matrix]

'''
multiply two matrices
'''
def multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
    	return None
    else:
        # Multiply if correct dimensions
        toReturn = zero(len(matrix1), len(matrix2[0]))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    toReturn[i][j] += matrix1[i][k] * matrix2[k][j]
        return toReturn

'''
Hadamard multiply two matrices
'''
def HadamardMultiply(matrix1, matrix2):
	toReturn = copy.deepcopy(matrix1)
	for i in range(len(matrix2)):
		for j in range(len(matrix2[i])):
			toReturn[i][j] *= matrix2[i][j]
	return toReturn


'''
Kronecker multiply two matrices (row vector and column vector)
Z[i][j] = X[0][i] * Y[j][0]
'''
def KroneckerMultiply(matrix1, matrix2):
	toReturn = []
	for i in range(len(matrix1[0])):
		toAppend = []
		for j in range(len(matrix2)):
			toAppend.append(matrix1[0][i]*matrix2[j][0])
		toReturn.append(toReturn)
	return toReturn 

'''
Concatenate two matrices horizontally.
'''
def concatenate(matrix1, matrix2):
	toReturn  = []
	for i in range(len(matrix1)):
		row = []
		for item in matrix1[i]:
			row.append(item)
		for item in matrix2[i]:
			row.append(item)
		toReturn.append(row)
	return toReturn