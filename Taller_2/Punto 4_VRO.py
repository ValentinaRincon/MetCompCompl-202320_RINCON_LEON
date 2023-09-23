import numpy as np
import matplotlib.pyplot as plt


def func_integrate(x):
    return np.exp(-x)*np.sin(x)

def montecarlo (a=0,b=np.pi):
    
    N = 10
    
    arregloN = np.linspace(10,10e3,9991)
    
    arregloE = []
    
    while N <= 10000:
        
        x = np.random.uniform(a,b,N)
        
        fi = func_integrate(x)
        
        I = (b-a)*sum(fi)/N
        
        Iteo = 0.5*(1+np.exp(-np.pi))
        
        error = (abs(Iteo - I))/I
        
        arregloE.append(error)
        
        #print(arregloE)

        N +=1
    print("La longitud de arreglo del error es {0}".format(len(arregloE)))    
    print("La longitud de arreglo de las N es {0}".format(len(arregloN)))    
    fig, ax = plt.subplots()
    ax.scatter(x = arregloN, y = arregloE)
    #plt.scatter(arregloN,arregloE)
    
    plt.show()
        
montecarlo()

"""
Falta hacer la gráfica de 1/sqtr(N)
Falta resolver el error para que dé 10e5 la gráfica. Buscar alternativa para el arreglo del error.
"""