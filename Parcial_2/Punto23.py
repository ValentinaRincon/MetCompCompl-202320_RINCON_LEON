import numpy as np 
import scipy as sp 
import sympy as sym 

x = sym.Symbol('x',real=True)

#Cuadratura de Laguerre

# Denominador

N = 20

f = lambda x: (x**3)/(np.exp(x)-1)*np.exp(x)
f1 = lambda x: (x**3)/(np.exp(x)-1)

def cuadratura_laguerre(f,n):
    
    raices_t,pesos_t = np.polynomial.laguerre.laggauss(n)
    
    I = np.sum(pesos_t*f(raices_t))
    
    return I

d = cuadratura_laguerre(f,N)
#print(cuadratura_laguerre(f,N))

# Numerador
# Cuadratura de Legrendre

h = 6.626 * (10 **(-34))
k = 1.3806 * (10 **(-23))
c = 3*(10**8)
T = 5772
l_0 = 1*(10**(-7)) #en metros
l_1 = 4*(10**(-7)) #en metros

v_0 = c/l_0
v_1 = c/l_1

b = (h*v_0)/(k*T) #Limite inferior
a = (h*v_1)/(k*T) #Limite superior

def cuadratura_legendre(n):
    
    raices_t,pesos_t = np.polynomial.legendre.leggauss(n)
    
    #I = np.sum(pesos_t*f(raices_t))
    
    return raices_t,pesos_t

g = cuadratura_legendre(N)

def integral_numerador(a,b,g):
    
    I = np.sum(g[1]*f1(0.5*(g[0]*(b-a)+a+b)))
    
    respuesta = I *0.5 * (b-a)
    
    return respuesta

p = integral_numerador(a,b,g)

division = p/d
resultado = round(division * 100,2)

print("El resultado de la fracción de los rayos es {0}%, aproximadamente".format(resultado))

print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

print("La razón de que el valor obtenido versus el valor de IDEAM Bogotá no concuerden, es porque \nlo que se calculó en este parcial es el porcentaje de rayos UVA, UVB y UVC, en general, de rayos UV que salen del sol. \n Por otra parte, el valor de IDEAM es obtenido a partir de la Tierra en Bogotá. \nLo que sucede es que la existencia de la atmósfera hace que se dispercen los rayos, en donde los rayos UVC son completamente rechazados, \nlos rayos UVB solamente entran un 5 a 10%, por último los UVA ingresan entre un 90 a un 95%  ")

