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
    
    b = ((f(x_1)-f(x_0))/(x_1-x_0)) - ((x_0+x_1)  * a)
    
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
   
    return x_3

def met_Newton (f,df,xn,itmax=100,precision=1e-11):
    
    error = 1. #Valor de tipo float
    it = 0 #La iteración inicia en 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            #Criterio de parada
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('División por cero')
            
        xn = xn1
        it += 1
        
    #print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn

def todas_las_raices (x, tolerancia=10):
    
    raices = np.array([])
    
    for i in x:
        
        raiz = met_Newton(funcion,derivada,i)
        
        if raiz is not False:
            
            raiz_2 = np.round(raiz,tolerancia)
            
            if raiz_2 not in raices:
                raices = np.append(raices,raiz_2)
                
    raices.sort()
    
    return raices

raices = todas_las_raices(x)
            
print(raices[0],np.sqrt(3/5))
