import numpy as np
from scipy import integrate

p_a = -0.01
b= 0.01

n = 1000

h= abs(p_a-b)*0.5

f = lambda x:np.sqrt(0.01**2-x**2)/(0.5+x)

class Integrator:
    
    def __init__(self,x,f):
        
        self.x = x
        self.h = self.x[1] - self.x[0]
        self.y = f(self.x)
        
        self.Integral = 0.
        
    def GetIntegral(self):
        
        self.Integral += 0.5*(self.y[0]+self.y[-1])
        
        #self.Integral += np.sum( self.y[1:-1] )
        
        for i in range(1,self.y.shape[0]-1):
            self.Integral += self.y[i]
        
        self.Integral *= self.h
        
        return self.Integral
    
    def GetError(self):
        
        valor_teorico = np.pi*(0.5-np.sqrt(0.5**2-0.01**2))
        
        valor_experimental = self.Integral
        
        error = ((abs(valor_experimental - valor_teorico))/valor_teorico)*100
        
        return error
        

x = np.linspace(-0.01,0.01,n)
y = f(x)


I = Integrator(x,f)

print("El valor de la integral es: ",I.GetIntegral())

print("El error por medio del método del trapecio es: ",I.GetError())
