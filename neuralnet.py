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



import math

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



def Run():
	pass


if __name__ == "__main__":
	Run()
