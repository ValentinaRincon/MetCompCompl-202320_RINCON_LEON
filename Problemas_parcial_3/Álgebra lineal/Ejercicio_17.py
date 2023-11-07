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
Jn = sym.lambdify([x,y],J,'numpy')

def NewtonRapshon(Fn,Jn,p,itmax=1000,precision=1e-6):
    x = p
    error = 1
    it = 0
   
    while error > precision and it < itmax:
       
        IFn = Fn(x[0],x[1])
        IJ = Jn(x[0],x[1])
        Inv_Jn = np.linalg.inv(IJ)
        x1 = x - np.matmul(Inv_Jn,IFn)
        error = np.max(np.abs(x1-x))
        
        x = x1
        it += 1
    return x
p = np.array([0.5, 0.5])
NewtonRapshon(Fn,Jn,p)

N = 50
x = np.linspace(-1,1,N)
y = np.linspace(-1,1,N)

z0 = np.array([-0.5,np.sqrt(3)/2])
z1 = np.array([-0.5,-np.sqrt(3)/2])
z2 = np.array([1,0])


Fractal = np.zeros((N,N), np.int64)
for i in range(N):
    for j in range(N):
        a = NewtonRapshon(Fn,Jn,np.array([x[i],y[j]]))
        d0 = np.max(np.abs(z0-a))
        d1 = np.max(np.abs(z1-a))
        d2 = np.max(np.abs(z2-a)) 
        minimo = min(d0,d1,d2)
        if d0  == minimo:
            Fractal[i][j] = 20
        elif d1 == minimo:
            Fractal[i][j] = 100
        else:
            Fractal[i][j] = 255
         
plt.imshow(Fractal, cmap='coolwarm' ,extent=[-1,1,-1,1])
