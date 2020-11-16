import numpy as np
import math

def conjugate_grad(A, b, x=None):
    if not x:
        x = np.ones(len(b))

    r = np.dot(A, x) - b
    p = - r
    r_k_norm = np.dot(r, r)
    for i in range(2* len(b)):
        Ap = np.dot(A, p)
        alpha = r_k_norm / np.dot(p, Ap)
        x += alpha * p
        r += alpha * Ap
        r_kplus1_norm = np.dot(r, r)
        beta = r_kplus1_norm / r_k_norm
        r_k_norm = r_kplus1_norm
        if r_kplus1_norm < 1e-5:
            print ('Itr:', i)
            break
        p = beta * p - r
    return x

# here dimension is 2, so it's hardcoded in

def conj_grad(x0, B):
    i = 0
    while i < 2: 
        d = -1 * g(x0)
        
        # CG
        if B == 0: 
            num = np.matmul(g(x0).transpose(), d)
            denom = np.matmul(np.matmul(d.tranpose(), Q), d) 
        # Hestenes-Stiefel
        elif B == 1:
            num = 
        
        alpha = num / denom

        x1 = x0 + np.dot(alpha, d)
        x0 = x1

        i+= 1


