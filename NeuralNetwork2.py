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
import random

############# Globals #################
alpha = 0.1
DEBUG_FLG = False
KFOLDS = 5

#######################################

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
Represents a single iris datapoint for training and comparison.
Constructor takes a features vector and true class value.
'''
class Example:

	'''
	Constructor
	'''
	def __init__(self, features, outputClass):
		self.inputX = features
		self.outputY = [0]*3
		self.outputY[outputClass-1] = 1
		self.realClass = outputClass


'''
Main Neural Network class
'''
class Network:

	'''
	Constructor
	Nodes [# INPUT, # HIDDEN, # OUTPUT]
	'''
	def __init__(self, nodeCounts):
		self.nodes = []
		for i in range(3):
			initVect = [1.0]*nodeCounts[i]
			self.nodes.append(initVect)

		# Input vectors to nodes (serve as variables for computing values)
		self.hiddenInputs = [0.0] * nodeCounts[1]
		self.outputInputs = [0.0] * nodeCounts[2]

		# Create weights
		self.inputWeights = zeroMatrix(len(self.nodes[0]), len(self.nodes[1]))
		self.outputWeights = zeroMatrix(len(self.nodes[1]), len(self.nodes[2]))

		# Init weights
		for i in range(len(self.inputWeights)):
			for j in range(len(self.inputWeights[i])):
				self.inputWeights[i][j] = random.uniform(-0.2, 0.2)

		for i in range(len(self.outputWeights)):
			for j in range(len(self.outputWeights[i])):
				self.outputWeights[i][j] = random.uniform(-0.2, 0.2)

		# Activation functions
		self.activationfunction = activation
		self.activationderivative = dActivation

	# the number of layers (3)
	def numLayers(self):
		return len(self.nodes)
	
	# Layer counts
	def numInput(self):
		return len(self.nodes[0])
	def numHidden(self):
		return len(self.nodes[1])
	def numOutput(self):
		return len(self.nodes[2])

	'''
	Back propogation algorithm
	'''
	def backPropLearn(self, examples, iterationLimit=100):
		delta = copy.deepcopy(self.nodes)
		iterations = 0

		while True:
			for example in examples:
				# Assign inputs
				for i in range(len(example.inputX)):
					self.nodes[0][i] = example.inputX[i]
				# Propogate to Hidden Layer
				for j in range(self.numHidden()):
					self.hiddenInputs[j] = 0.0
					for i in range(self.numInput()):
						self.hiddenInputs[j] += self.inputWeights[i][j] * self.nodes[0][i]
					self.nodes[1][j] = self.activationfunction(self.hiddenInputs[j])

				# Propogate to Output Layer
				for j in range(self.numOutput()):
					self.outputInputs[j] = 0.0
					for i in range(self.numHidden()):
						self.outputInputs[j] += self.outputWeights[i][j] * self.nodes[1][i]
					self.nodes[2][j] = self.activationfunction(self.outputInputs[j])


				for j in range(self.numOutput()):
					delta[2][j] = self.activationderivative(self.outputInputs[j]) * (example.outputY[j] - self.nodes[2][j])

				#propgate back through hidden
				for i in range(self.numHidden()):
					summation = 0.0
					for j in range(self.numOutput()):
						summation += self.outputWeights[i][j] * delta[2][j]
					delta[1][i] = self.activationderivative(self.hiddenInputs[i]) * summation

				#propgate back through input
				for i in range(self.numInput()):
					summation = 0.0
					for j in range(self.numHidden()):
						summation += self.inputWeights[i][j] * delta[1][j]
					delta[0][i] = self.activationderivative(example.inputX[i]) * summation

				# Update weights.
				for i in range(self.numInput()):
					for j in range(self.numHidden()):
						self.inputWeights[i][j] += alpha * self.nodes[0][i] * delta[1][j]
						if DEBUG_FLG:
							print 'node 0,',i, ':', self.nodes[0][i], 'delta:',delta[1][j]
				for i in range(self.numHidden()):
					for j in range(self.numOutput()):
						self.outputWeights[i][j] += alpha * self.nodes[1][i] * delta[2][j]
						if DEBUG_FLG:
							print 'node 1,',i, ':', self.nodes[1][i], 'delta:',delta[2][j]

			iterations += 1

			# Just stop after a hundred iterations
			if iterations > iterationLimit:
				break

	'''
	Find a value for a given datapoint.
	'''
	def findValue(self, example):
		for i in range(len(example.inputX)):
			self.nodes[0][i] = example.inputX[i]

		# Propogate to Hidden Layer
		for j in range(self.numHidden()):
			self.hiddenInputs[j] = 0.0
			for i in range(self.numInput()):
				self.hiddenInputs[j] += self.inputWeights[i][j] * self.nodes[0][i]
			self.nodes[1][j] = self.activationfunction(self.hiddenInputs[j])

		# Propogate to Output Layer
		for j in range(self.numOutput()):
			self.outputInputs[j] = 0.0
			for i in range(self.numHidden()):
				self.outputInputs[j] += self.outputWeights[i][j] * self.nodes[1][i]
			self.nodes[2][j] = self.activationfunction(self.outputInputs[j])
		
		if DEBUG_FLG:
			print 'result',self.nodes[2], 'real class:', example.realClass
		return self.nodes[2].index(max(self.nodes[2]))+1
	
	'''
	For debugging
	'''
	def printWeights(self):
		print '******* Input weights ***********'
		print self.inputWeights
		print '******* Output weights **********'
		print self.outputWeights

	'''
	Run tests to find error rate on a given validation set
	'''
	def test(self, validationset):
		total = len(validationset)
		correct = 0
		for example in validationset:
			result = self.findValue(example)
			if result == example.realClass:
				correct += 1
		return (total-correct)/total

		
'''
For the sake of code reuse, use the Iris datatype from the perceptrons project
this converts the objects into an 'Element' for easier use with the network.
'''
def irises2examples(irislist):
	examples = []
	for iris in irislist:
		features = iris.features[:4]
		example = Example(features, iris.realClass)
		examples.append(example)
	return examples

'''
Run network
'''
def Run():
	dataset = IrisDataset()

	for loops in range(1, 1001, 100):
		for i in range(1, 71, 2):
			tErrorSum = 0
			vErrorSum = 0
			for j in range(5):
				irisTrainingSet, irisValidationSet = dataset.partition(j, KFOLDS)

				trainingset = irises2examples(irisTrainingSet)
				validationset = irises2examples(irisValidationSet)

				network = Network([4, i, 3])

				network.backPropLearn(trainingset, loops)
				tError = network.test(trainingset)
				vError = network.test(validationset)

				tErrorSum += tError
				vErrorSum += vError

			tErrorAvg = tErrorSum / 5
			vErrorAvg = vErrorSum / 5

			print 'Hidden,',i,',Avg Training Error,',tErrorAvg,',Avg Validation Error,',vErrorAvg,',loops,',loops



'''
Bootstrap
'''
if __name__ == "__main__":
	Run()