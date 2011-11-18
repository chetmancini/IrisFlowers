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


#######################################
############## IMPORTS  ###############
import math


'''
Perceptron
'''
class Perceptron:
	'''
	Constructor.
	Takes a training set and a test set
	'''
	def __init__(self, trainingset, testset):
		self.numFeatures = len(trainingset[0].features)
		self.trainingset = trainingset
		self.testset = testset

	


'''
build a hyperplane
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
normalize
'''
def normalize(dataList):
	for i in range(30):
		currentList = []
		for node in dataList:
			currentList.append(node.features[i])
		mean, stdev = meanstdv(currentList)
		for node in dataList:
			node.features[i] = (node.features[i] - mean) / stdev

def normalizeScale(dataList):
	for i in range(30):
		currentList = []
		for node in dataList:
			currentList.append(node.features[i])
		minval = min(currentList)
		maxval = max(currentList)
		for node in dataList:
			node.features[i] = (node.features[i] - minval) / (maxval - minval)


	
def RunTests():
	pass

def Run():
	RunTests()

if __name__ == "__main__":
	Run()
