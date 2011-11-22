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
from HelperFunctions import *
import math
import random
import sys
import copy

'''
Iris object
'''
class Iris:

	'''
	Dictionary of values to iris name
	'''
	class2name = {
		0:'NULL',
		1:'setosa',
		2:'versicolor',
		3:'viginica'
	}

	'''
	Constructor
	'''
	def __init__(self, inputStr=None):
		if inputStr:
			items = inputStr.split(',')
			self.features = []
			for i in range(4):
				self.features.append(float(items[i]))
			self.features.append(1)
			self.realClass = int(items[4])
		else:
			self.features = []
			self.realClass = 0
		self.foundClass = 0

	'''
	Euclidean distance between this feature vector and another.
	'''
	def distance(self, other):
		distSum = 0
		for i in range(len(self.features)):
			distSum += (self.features[i]-other.features[i])**2
		return math.sqrt(distSum)

	'''
	Getter methods
	'''
	def sepalLength(self):
		return self.vector[0]

	def sepalWidth(self):
		return self.vector[1]

	def petalLength(self):
		return self.vector[2]

	def petalWidth(self):
		return self.vector[3]

	def getClassification(self):
		return self.foundClass

	def getName(self):
		return class2name[self.foundClass]

	'''
	Get Y
	'''
	def getY(self, classifyId):
		if self.realClass == classifyId:
			return 1
		else:
			return -1

	'''
	String version of iris
	'''
	def asString(self):
		return str(self.features) + str(self.realClass)

	'''
	Clone class
	'''
	def clone(self):
		toReturn = Iris()
		toReturn.features = copy.deepcopy(self.features)
		toReturn.realClass = self.realClass
		toReturn.foundClass = self.foundClass
		return toReturn

'''
Iris Dataset
'''
class IrisDataset:

	'''
	the dataset of irises as a list
	'''
	fullset = []

	'''
	Constructor
	'''
	def __init__(self, normalize=True):
		self.readFile("dataset.csv")
		self.numFeatures = len(self.fullset[0].features)
		random.shuffle(self.fullset)
		if normalize:
			self.normalizeStdNorm()
		#self.normalizeScale()

	'''
	Read File
	'''
	def readFile(self, filename="dataset.csv"):
		with open(filename, 'r') as f:
			for line in f:
				iris = Iris(line)
				self.fullset.append(iris)

	def shuffleData(self):
		random.shuffle(self.fullset)

	'''
	normalize to a normal distribution
	'''
	def normalizeStdNorm(self):
		for i in range(self.numFeatures - 1):
			currentList = []
			for node in self.fullset:
				currentList.append(node.features[i])
			mean, stdev = meanstdv(currentList)
			for node in self.fullset:
				node.features[i] = (node.features[i] - mean) / stdev

	'''
	Normalize to a scale
	'''
	def normalizeScale(self):
		for i in range(self.numFeatures):
			currentList = []
			for node in self.fullset:
				currentList.append(node.features[i])
			minval = min(currentList)
			maxval = max(currentList)
			for node in self.fullset:
				if maxval - minval == 0:
					print maxval, minval, 0
				node.features[i] = (node.features[i] - minval) / (maxval - minval)


	'''
	Partition
	'''
	def partition(self, fold, kfolds):
		length = len(self.fullset)
		validationSet = []
		trainingSet = []
		for i in range(length):
			if i >= math.floor(fold*(length/kfolds)) and i <= math.floor((fold+1)*(length/kfolds)):
				validationSet.append(self.fullset[i].clone())
			else:
				trainingSet.append(self.fullset[i].clone())
		return trainingSet, validationSet