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
#######################################


############# Imports #################
from __future__ import division
from Iris import *
from MatrixOperations import *
from HelperFunctions import *
import math

############################################
############# Training Program #############
'''
Train
'''
def train():
	pass

'''
Load data
'''
def loaddata():
	pass

'''
Feed forward
'''
def feedForward(inputsMatrix, weightsMatrix, biasMatrix=None):
	if not biasMatrix:
		toMul = inputsMatrix
	else:
		toMul = concatenate(inputsMatrix, biasMatrix)

	net = matrix.multiply(weightsMatrix, toMul)
	output = activate(net)
	return output

'''
Eval network
'''
def evalnetwork():
	pass

'''
Back propogation
'''
def backpropagation():
	pass

'''
Output to class
'''
def outputToClass(outputMatrix):
	toReturn = []
	for row in outputMatrix:
		for i in range(len(row)):
			if row[i] == 1:
				toReturn.append(i+1)
	return toReturn


'''
Class to output
'''
def classOutput(classVector):
	toReturn = [[0 for col in range(3)] for row in range(len(classVector))]
	for i in range(len(classVector)):
		toReturn[i][classVector[i]-1] = 1
	return toReturn


'''
Activation function f(x)
Use hyperbolic tangent
'''
def activation(x):
	return (math.tanh(x) + 1)/2

'''
Derivative of activation function: f'(x)
(d/dx hyperbolic tangent)
'''
def dActivation(x):
	return (1 - (math.tanh(x)**2))/2

'''
apply activation function to a matrix
'''
def activate(matrixIn):
	toReturn = copy.deepcopy(matrixIn)
	return [[activation(col) for col in row] for row in toReturn]



#############################################
############### Application Program #########
class Application:
	def feedForward(self):
		pass

	def outputVectorToClass(self):
		pass


##############  RUN  ###############
'''
Run Neural Nets
'''
def Run():
	pass


'''
Boostrap
'''
if __name__ == "__main__":
	Run()
