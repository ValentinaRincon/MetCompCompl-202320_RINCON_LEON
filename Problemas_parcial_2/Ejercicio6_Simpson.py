import numpy as np 
from scipy import integrate

class Integrator:
    
    def __init__(self,x,f):
        
        self.x = x
        self.h = self.x[1] - self.x[0]
        self.y = f(self.x)
        
        self.Integral = 0.
        
class Simpson(Integrator):
    
    def __init__(self,x,f):
        Integrator.__init__(self,x,f)
        
    def GetIntegral(self):
        
        self.Integral = 0.
        
        self.Integral += self.y[0] + self.y[-1]
        
        for i in range( len(self.y[1:-1]) ):
            
            if i%2 == 0:
                self.Integral += 4*self.y[i+1]
            else:
                self.Integral += 2*self.y[i+1] 
          
        return self.Integral*self.h/3
    
    def GetError(self):
        
        valor_teorico = np.pi*(0.5*np.sqrt(0.5**2-0.01**2))
        
        valor_experimental = self.Integral*self.h/3
        
        error = (abs(valor_experimental - valor_teorico))/valor_teorico
        
        return error
    
f = lambda x:np.sqrt(0.01**2-x**2)/(0.5+x)
n = 1000
x = np.linspace(-0.01,0.01,n+1)

Integrador = Simpson(x,f)
print("b es",Integrador.GetError())
print("c es",integrate.simpson(f(x),x))