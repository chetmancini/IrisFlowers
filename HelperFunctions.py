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
Calculate mean and stddev of a set
'''
def meanstdv(x):
    from math import sqrt
    n, mean, std = len(x), 0, 0
    for a in x:
		mean = mean + a
    mean = mean / float(n)
    for a in x:
		std = std + (a - mean)**2
    std = sqrt(std / float(n-1))
    return mean, std



'''
dot product of two vectors
'''
def dot(vect1, vect2):
	toReturn = 0
	if len(vect1) != len(vect2):
		print 'unmatched vectors'
	for i in range(len(vect1)):
		toReturn += vect1[i] * vect2[i]
	return toReturn

'''
multiply a vector by a scalar
'''
def multVect(scalar, vect):
	return [x * scalar for x in vect]


'''
add two vectors together --> vector
'''
def addVect(vect1, vect2):
	toReturn = []
	for i in range(len(vect1)):
		toReturn.append(vect1[i] + vect2[i])
	return toReturn


'''
Precision and Recall
'''
def precision(truePositive, falsePositive):
	if truePositive + falsePositive == 0:
		return 0
	else:
		return truePositive / (truePositive + falsePositive)

def recall(truePositive, falseNegative):
	if truePositive + falseNegative == 0:
		return 0
	else:
		return truePositive / (truePositive + falseNegative)

def accuracy(truePositive, trueNegative, falsePositive, falseNegative):
	if (falsePositive + falseNegative + trueNegative + truePositive) == 0:
		print 'accuracy 0'
		return 0
	else:
		return 100*(truePositive + trueNegative) / (falsePositive + falseNegative + trueNegative + truePositive)
'''
Helper function for f-measure
'''
def fMeasure(precision, recall):
	if precision + recall == 0:
		return 0
	else:
		return 2 * precision * recall / (precision + recall)