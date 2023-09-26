import numpy as np 
import matplotlib.pyplot as plt
import sympy as sp

t = sp.Symbol('t',real=True)
t_values = np.linspace(0, 1, 250)

def funcion(t):
    return sp.pi * (0.125)**2 * 0.05 * sp.cos(3.5*t) * sp.cos(2 * sp.pi * 7*t)

def Dfuncion(t):
    ecu = funcion(t)
    return sp.diff(ecu, t)

# Convierte la derivada simbólica en una función numérica
t_symbolic = sp.symbols('t')
Dfunc = sp.lambdify(t_symbolic, Dfuncion(t_symbolic), 'numpy')

def corriente_vs_tiempo():
    
    Decu = Dfunc(t_values)
    
    corriente = 1/0.125 * Decu*-1
    
    plt.scatter(t_values, corriente, c="#FF4000")
    plt.xlabel('Tiempo')
    plt.ylabel('Corriente')
    plt.title('Gráfico de Corriente vs. Tiempo')
    plt.show()

corriente_vs_tiempo()
