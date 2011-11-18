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


'''
Iris object
'''
class Iris:

	class2name = {
		0:'unknown',
		1:'setosa',
		2:'versicolor',
		3:'viginica'
	}

	'''
	Constructor
	'''
	def __init__(self, inputStr=None):
		items = inputStr.split(',')
		self.features = []
		for i in range(3):
			self.features.append(float(items[i]))
		self.features.append(1)
		self.realClass = items[4]
		self.foundClass = 0

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
Iris Dataset
'''
class IrisDataset:

	trainingSet = []
	testSet = []
	validationSet = []

	'''
	Constructor
	'''
	def __init__(self):
		pass

	'''
	Read File
	'''
	def readFile(self):
		filename = "dataset.csv"
		with open(dataset, 'r') as f:
			for line in f:
				iris = Iris(line)
				self.irises.append(iris)

