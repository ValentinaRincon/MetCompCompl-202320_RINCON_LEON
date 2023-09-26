import numpy as np 

t_values = np.linspace(0, 1, 250)

def Function(t):
    return np.pi * (0.125)**2 * 0.05 * np.cos(3.5*t) * np.cos(2 * np.pi * 7*t)

def Derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

def GetNewtonMethod(f, df, xn, itmax=100, precision=1e-8):
    error = 1.
    it = 0

    while error > precision and it < itmax:
        try:
            xn1 = xn - f(xn[0]) / df(f, xn[0])
            # Criterio de parada
            error = np.abs(f(xn[0]) / df(f, xn[0]))
        except ZeroDivisionError:
            print('Division por cero')
        xn[0] = xn1
        it += 1

    if it == itmax:
        return False
    else:
        return xn[0]
    
def GetAllRoots(x, tolerancia=10):
    Roots = np.array([])

    for i in x:
        root = GetNewtonMethod(Function, Derivative, np.array([i]))
        if root is not False:
            croot = np.round(root, tolerancia)
            if croot not in Roots:
                Roots = np.append(Roots, croot)

    Roots.sort()
    
    respuesta = [Roots[3], Roots[4], Roots[5]]
    return respuesta

print(GetAllRoots(t_values, tolerancia=10))
