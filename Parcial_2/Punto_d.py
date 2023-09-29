import numpy as np 
import scipy as sp 
import sympy as sym 

raices = [0.41577456, 2.29428036, 6.28994508]
pesos = [0.71109301, 0.27851773, 0.01038926]

n = x-1

funcion = lambda x: (np.math.factorial(n))**(n)

I = 0
for i in range(3):
    
    I += pesos[i]*funcion(raices[i])
    
print(I)