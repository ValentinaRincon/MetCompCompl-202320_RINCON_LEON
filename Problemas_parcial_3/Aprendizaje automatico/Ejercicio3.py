import numpy as np
from tqdm import tqdm

def f(x):
    return abs(x-2)

Dx = lambda f,x,h=1e-5: (f(x+h) - f(x-h))/(2*h)

def Minimizer(f, N=300, gamma=0.01):
    
    r = np.zeros(N)
    # Seed
    r[0] = np.random.uniform(-5,5)
    
    for i in tqdm(range(1,N)):
        r[i] = r[i-1] - gamma*Dx(f,r[i-1])
        
    return r

x = Minimizer(f)

Cost = f(x)

print(x)

print("Para la función dada de |x-2|, no es posible obtener un mínimo por medio del descenso del gradiente. Esto es porque la función dada \n no es derivable. Por lo tanto, el método jamás terminará satisfactoriamente el ejercicio y estará 'brincando' de lado a lado \n hasta terminar con las iteraciones dadas. En otras palabras, no va a converger al mínimo.")