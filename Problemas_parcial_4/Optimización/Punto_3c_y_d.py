import numpy as np 
from scipy.optimize import minimize

def f(variables):
    x,y,z = variables
    return -x*y*z

def g(variables):
    x,y,z = variables
    return x*y+2*y*z+2*x*z-12

valores_iniciales = [1,1,1]

restricciones =  {'type': 'eq', 'fun': g}

respuesta = minimize(f,valores_iniciales,constraints=restricciones,method='SLSQP')

#valores_op = respuesta.x
volumen_max = round(-respuesta.fun,3)

#print("Los valores óptimos para x, y, z son:", valores_op)
print("El volumen máximo obtenido es:", volumen_max, "cm^3")