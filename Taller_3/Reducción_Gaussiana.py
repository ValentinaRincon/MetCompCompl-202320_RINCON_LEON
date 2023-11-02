import numpy as np 

"Punto a"

def punto_a():
    
    A = np.array([[3., 1., -1.],
              [1., -2., 3.],
              [4., -1., 1.]])
    b_a = np.array([2., 0., 3.])
    
    Ab_a = np.column_stack((A, b_a)) #Función que unifica A y b_a para formar la matriz ampliada
        
    # Se inicia el proceso de eliminación Gaussiana
    
    n = len(b_a)
    for i in range(n):   
        #Se busca el pivote para iniciar el cálculo     
        max_index = np.argmax(np.abs(Ab_a[i:, i])) + i
        Ab_a[[i, max_index]] = Ab_a[[max_index, i]]
    
        for j in range(i + 1, n):
            factor = Ab_a[j, i] / Ab_a[i, i]
            Ab_a[j, i:] -= factor * Ab_a[i, i:]
            
    #Se resuelve la matriz triangular superior        
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab_a[i, -1] - np.sum(Ab_a[i, i+1:n] * x[i+1:])) / Ab_a[i, i]
        
    print ("Las 3 fuerzas que actuan en el objeto son {0} newtons".format(x))

'Punto b'

def punto_b():
    
    B = np.array([[1., 1., 1.],
              [0., -8., 10.],
              [4., -8., 0.]])
    b_b = np.array([0., 0., 6.])
    
    Bb_b = np.column_stack((B, b_b)) #Función que unifica B y b_b para formar la matriz ampliada

    # Se inicia el proceso de eliminación Gaussiana
    n = len(b_b)
    for i in range(n):
        #Se busca el pivote para iniciar el cálculo     
        max_index = np.argmax(np.abs(Bb_b[i:, i])) + i
        Bb_b[[i, max_index]] = Bb_b[[max_index, i]]
        for j in range(i + 1, n):
            factor = Bb_b[j, i] / Bb_b[i, i]
            Bb_b[j, i:] -= factor * Bb_b[i, i:]
    #Se resuelve la matriz triangular superior        
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Bb_b[i, -1] - np.sum(Bb_b[i, i+1:n] * x[i+1:])) / Bb_b[i, i]
        
    print ("Las corrientes I_a, I_b e I_c en el circuito son {0} amperios".format(x))
punto_b()