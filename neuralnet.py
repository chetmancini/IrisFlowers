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
