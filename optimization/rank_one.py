import numpy as np
from numpy import linalg as LA
from scipy import optimize

a = np.array([[1, 0], [0, 2]])
b = np.array([1, -1])

def f(x):
    return (lambda x : np.matmul(np.matmul(np.dot(0.5, x.transpose()), a), x) - np.matmul(x.transpose(), b) + 7)(x)

def g(x):
    return (lambda x : np.matmul(a, x) - b)(x)

# only pass np values - no internal checking
def quad_alpha(x, d):
    return np.matmul(np.dot(-1, g(x)), d) / np.matmul(np.matmul(d.transpose(), a), d)

# rank one correction formula
def rank_one(x0, max, tol):
    # step 1
    k = 0
    x0 = np.array(x0)
    H = np.array([[1, 0], [0, 1]])

    while k < max: 
        # step 2
        print(LA.norm(g(x0)))
        if LA.norm(g(x0)) < tol:
            return x0
        else:
            d = np.matmul(np.dot(-1, H), g(x0))

        # step 3
        alpha = quad_alpha(x0, d)
        delta_x = np.dot(alpha, d)
        x1 = x0 + delta_x
        
        # step 4
        delta_x = np.dot(alpha, d)
        delta_g = g(x1) - g(x0)

        num = np.matmul((delta_x - np.matmul(H, delta_g)), (delta_x - np.matmul(H, delta_g)).transpose())
        denom = np.matmul(delta_g.transpose(), (delta_x - np.matmul(H, delta_g)))
    
        H1 = H + (num / denom)
        # loop back
        H = H1
        x0 = x1
        k = k + 1

# # SciPy offers BFGS as part of its library
# print(optimize.fmin_bfgs(f, np.array([0, 0])), g)

# # NOTE: x must be entered as a 2-D array
# # there is a ZeroDivisionError increasing the error range
# print(rank_one([0, 0], 10, 0.5)) 