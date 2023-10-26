import numpy as np 

"Punto a"

A = np.array([[3,1,-1],
              [1,-2,3],
              [4,-1,1]])

b_a = np.array([2,0,3])

x_a = np.zeros(len(b_a))

for i in range(len(b_a)):
    x_a[i] = b_a[i]/A[i][i]
    
resultado_a = ("Las 3 fuerzas que actuan en el objeto son {0} N".format(x_a))

"Punto b"

B = np.array([[1,1,1],
              [0,-8,10],
              [4,-8,0]])

b_b = np.array([0,0,6])

x_b = np.zeros(len(b_b))

for j in range(len(b_b)):
    x_b[i] = b_b[i]/A[i][i]
    
resultado_b = ("Las corrientes I_a, I_b e I_c en el circuito son {0} A".format(x_b))

