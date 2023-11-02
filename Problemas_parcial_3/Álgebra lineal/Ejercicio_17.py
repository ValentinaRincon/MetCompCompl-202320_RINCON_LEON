import numpy as np
import matplotlib.pyplot as plt 
import sympy as sym 

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def f(x,y):
    
    z = x + sym.I*y 
    f = z**3-1
    f = f.expand()
    
    return sym.re(f),sym.im(f)

f0,f1 = f(x,y)
F = [f0,f1]
F

J = sym.zeros(2,2)

for i in range(2):
    for j in range(2):
        if j==0:
            J[i,j] = sym.diff(F[i],x,1)
        else:
            J[i,j] = sym.diff(F[i],y,1)

J

Fn = sym.lambdify([x,y],F,'numpy')

J_i = np.linalg.inv(J)

G = np.array([lambda x,y,z: 6*x - 2*np.cos(y*z) - 1.,
     lambda x,y,z: 9*y + np.sqrt( x**2 + np.sin(z) + 1.06 ) + 0.9,
     lambda x,y,z: 60*z + 3*np.exp(-x*y)+10*np.pi - 3])