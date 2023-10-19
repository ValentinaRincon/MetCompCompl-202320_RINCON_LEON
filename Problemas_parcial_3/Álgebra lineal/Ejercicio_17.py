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

def GetJacobian(f,r,h=1e-6):
    
    n = r.shape[0]
    
    J = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            
            rf = r.copy()
            rb = r.copy()
            
            rf[j] = rf[j] + h
            rb[j] = rb[j] - h
            
            J[i,j] = ( f[i](rf[0],rf[1],rf[2]) - f[i](rb[0],rb[1],rb[2])  )/(2*h)
            
    
    return J
u = GetJacobian(F,np.array([1.,1.,1.]))
print(u)

Fn = sym.lambdify([x,y],F,'numpy')
