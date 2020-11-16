import numpy as np
import math

# rosenbrock's function
def f(x):
    return (lambda x : (100 * (x[1] - math.pow(x[0], 2))) + math.pow((1 - x[0]), 2))(x)

# rosenbrock gradient
def g(x):
    return (lambda x: np.array([ -400 * (x[1] - math.pow(x[0],2)) * x[0], 
    200 * (x[1] - math.pow(x[0], 2))]))(x)