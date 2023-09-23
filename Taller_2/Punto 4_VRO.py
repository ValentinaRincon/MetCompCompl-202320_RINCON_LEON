import numpy as np
import matplotlib.pyplot as plt


def func_integrate(x):
    return np.exp(-x)*np.sin(x)

def montecarlo (a=0,b=np.pi):
    
    N = 10
    
    arregloN = np.linspace(10,10e3,9991)
    arregloRaiz = np.array([])
    arregloE = np.array([])
    
    while N <= 10000:
        
        x = np.random.uniform(a,b,N)
        
        fi = func_integrate(x)
        
        I = (b-a)*sum(fi)/N
        
        Iteo = 0.5*(1+np.exp(-np.pi))
        
        error = ((abs(Iteo - I))/I)*100
        
        arregloE = np.append(arregloE,error)
        
        calculo = 1/(np.sqrt(N))
        
        arregloRaiz= np.append(arregloRaiz,calculo)
        
        N +=1
    
#Parte gráfica

    plt.figure(figsize=(10,4))
    #_________________________________#
    plt.subplot(1,2,1)
    plt.scatter(x = arregloN, y = arregloE, c="#E2725B")
    plt.title("Porcentaje de error vs N") 
    plt.xlabel("N")
    plt.ylabel("Porcentaje de error")
    
    #_________________________________#
    plt.subplot(1,2,2)
    plt.scatter(x = arregloN, y = arregloRaiz, c="#E2728B")
    plt.title("N vs $\sqrt{N}$") 
    plt.xlabel("$\sqrt{N}$")
    plt.ylabel("N")
    
    #_________________________________#
    plt.tight_layout()
    plt.show()
        
montecarlo()