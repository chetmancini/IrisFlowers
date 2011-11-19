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


############## IMPORTS  ###############
from __future__ import division
from Iris import *
from HelperFunctions import *
import math

############## GLOBALS  ###############


############## CLASSES  ###############

'''
Perceptron
'''
class Perceptron:
	'''
	Constructor.
	Takes a training set and a test set
	'''
	def __init__(self, dataset):
		self.dataset = dataset
		self.numFeatures = len(trainingset[0].features)
		self.trainingset = None
		self.testset = None
		self.validationSet = None


'''
Build a hyperplane
'''
def buildHyperplane(rate=0.1, runs=1000):
	w = [0] * numFeatures
	for i in range(runs):
		for node in dataNodes:
			if (node.getY() * dot(w, node.features)) <= 0:
				scaleFactor = rate*node.getY()
				w = addVect(w, multVect(scaleFactor, node.features))
	return w

'''
hypothesis
'''
def hypothesis(w, xNode):
	if dot(w, xNode.features) > 0:
		return 1
	else:
		return -1



############## Run  ###############
'''
Run perceptron learning
'''
def Run():
	dataset = IrisDataset()
	perceptron = new Perceptron(dataset)

'''
Bootstrap
'''
if __name__ == "__main__":
	Run()
