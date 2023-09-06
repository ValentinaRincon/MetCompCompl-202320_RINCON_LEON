import numpy as np
import matplotlib.pyplot as plt 

def funcion(x):
    euler = np.exp(1)
    return euler**-x - x
    #return euler^-x - x
x_1 = 1
x_2 = 0.5

x_0 = 0
x_1 = 1
x_2 = 0.5

def derivada(f,x,h=1e-6):
    return (f(x+h) - f(x-h))/(2*h)

def coeficientes(x_0,x_1,x_2,f):
    
    a = (((f(x_2)-f(x_1))/(x_2-x_1)) - (((f(x_1)-f(x_0))/(x_1-x_0)))/(x_2-x_0))
    
    b = ((f(x_1)-f(x_0))/(x_1-x_0)) - ((x_0+x_1) * (f(x_2)-f(x_1))/(x_2-x_1) * a)
    
    c = f(x_0) - (x_0)*((f(x_1)-f(x_0))/(x_1-x_0)) + (x_0*x_1)*a

    return a,b,c

d = coeficientes(x_0,x_1,x_2,funcion)

def x_3(d):
    
    a = d[0]
    b = d[1]
    c = d[2]
    
    num = -2*c
    deno =b + np.sqrt( b**2 - (4*a*c))
    
    x_3 = num/deno
    
    

