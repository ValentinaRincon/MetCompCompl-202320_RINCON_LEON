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
    u = x.copy()
    k = 0
    r_0 = np.linalg.norm(np.dot(M,x)-b)
    p_0 = -r_0
    
    while r_0 >= precision and k < 6:
        
        #u[:]=0
        a = - (np.dot(r_0.T,p_0))/(np.dot(p_0.T,np.dot(M,p_0)))
        x_1 = x + np.dot(a,p_0)
        r_1 = np.linalg.norm(np.dot(M,x_1)-b)
        b_1 = (np.dot(r_1.T,np.dot(M,p_0)))/(np.dot(p_0.T,np.dot(M,p_0)))
        p_1 = -(r_1 + np.dot(b_1,p_0))
        p_0 = p_1
        k +=1
        
    print(x)    
    return x
p = np.array([-1.0,2.1,12.,1.,3.])
conjugado(M,b,p)