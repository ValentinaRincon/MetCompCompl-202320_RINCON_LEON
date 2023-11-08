import numpy as np 
import sympy as sp 

M = np.array([[0.2,0.1,1.,1.,0.],
             [0.1,4.,-1.,1.,-1.],
             [1.,-1.,60.,0.,-2.],
             [1.,1.,0.,8.,4.],
             [0.,-1.,-2.,4.,700.]])

b = np.array([1.,2.,3.,4.,5.])

def conjugado (M,b,x_0,precision=0.01):
    
    x = x_0.copy()
    k = 0
    r_0 = (np.dot(M,x))-b
    p_0 = -r_0
    norma = np.linalg.norm(r_0)
    p = p_0
    while norma >= precision and k < 6:
        m_p = np.dot(M,p)
        a = - (np.dot(r_0.T,p))/(np.dot(p.T,m_p))
        x_1 = x + np.dot(a,p)
        r_1 = np.dot(M,x_1)-b
        print(r_1)
        b_1 = (np.dot(r_1.T,m_p))/(np.dot(p.T,m_p))
        print(b_1)
        p_1 = (-r_1 + np.dot(b_1,p))
        p = p_1
        x = x_1
        k +=1
        
    print(x_1)   
    return x_1
p = np.array([0,0,0,0,0])
conjugado(M,b,p)