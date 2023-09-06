import numpy as np

def func(x:int):
    euler = np.exp(1)
    return euler**(-x) - x

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

def biseccion(func,a,b, tolerancia = 1e-7, itmax=100):
    
    respuesta = None
    
    if func(a) * func(b) >=0:
        respuesta = "Metodo no valido" 
              
    i = 0
    
    while (b-a) /2 > tolerancia and i < itmax:
        c = (a+b) / 2
        if func(c) == 0:
            respuesta = c
        elif func(c) * func(a) > 0:
            b = c
        else:
            a = c
        i +=1
    
    respuesta = (a + b)/2
    
    return respuesta   

d = coeficientes(x_0,x_1,x_2,func)

def x_3(d):
    
    a = d[0]
    b = d[1]
    c = d[2]
    
    num = -2*c
    deno =b + np.sqrt( b**2 - (4*a*c))
    
    x_3 = num/deno
   
    return x_3

def met_Newton (f,df,x_3,itmax=100,precision=1e-11):
    
    error = np.abs(f(x_3)) #Valor de tipo float
    it = 0 #La iteración inicia en 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = x_3 - f(x_3)/df(f,x_3)
            #Criterio de parada
            error = np.abs(f(x_3)/df(f,x_3))
            
        except ZeroDivisionError:
            print('División por cero')
            
        x_3 = xn1
        it += 1
        
    #print('Raiz',x_3,it)
    
    if it == itmax:
        return False
    else:
        return x_3
    
r = (met_Newton(func,derivada,x_3,itmax=100,precision=1e-11))

print("La raíz de la función dada es {0}".format(r))