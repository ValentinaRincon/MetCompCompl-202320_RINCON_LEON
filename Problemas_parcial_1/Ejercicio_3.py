import numpy as np

def funcion(x):
    return 3*x**5 + 5*x**4-x**3

x = np.linspace(-2.5,1.5,30)

def derivada(f,x,h=1e-6):
    return (f(x+h) - f(x-h))/(2*h)

def met_Newton (f,df,xn,itmax=90,precision=1e-8):
    
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


