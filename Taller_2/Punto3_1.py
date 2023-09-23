#Gauss-Laguerre

import numpy as np
import sympy as sym

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetLaguerre (n,x):
    
    if n == 0:
        poli = sym.Number(1)
    elif n ==1:
        poli = (1-x)
    else:
        poli = ((2*n-1-x)*GetLaguerre(n-1,x)-(n-1)*GetLaguerre(n-2,x))/n
        
    return sym.expand(poli,x)

def derivadasLaguerre(n,x):
    
    derivadas = GetLaguerre(n,x)
    
    return sym.diff(derivadas,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
    
def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots
    
def GetAllRootsGLag(n):
    
    xn = np.linspace(-1,1,100)
    
    Laguerre = []
    D_Laguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerre(i,x))
        D_Laguerre.append(derivadasLaguerre(i,x))
    
    poli = sym.lambdify([x],Laguerre[n],'numpy')
    D_poli = sym.lambdify([x],D_Laguerre[n],'numpy')
    Roots = GetRoots(poli,D_poli,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)

    Laguerre = []
    
    for i in range(n+2):
        Laguerre.append(GetLaguerre(i,x))
    
    poli = sym.lambdify([x],Laguerre[n+1],'numpy')
    Weights = Roots/(((n+1)**2)*(poli(Roots)**2))
    
    return Weights
    