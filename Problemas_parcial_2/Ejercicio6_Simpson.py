import numpy as np 
from scipy import integrate

f = lambda x:np.sqrt(0.01**2-x**2)/(0.5+x)
n = 1000
x = np.linspace(-0.01,0.01,n+1)
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
    
    def GetDerivative(self):
        
        d = (f(self.x + 2*self.h) - 4*f(self.x + self.h) + 6*f(self.x) - 4*f(self.x - self.h) + f(self.x - 2*self.h))/self.h**4
        
        return d
    
    def GetError(self):
        
        valor_teorico = np.pi*(0.5-np.sqrt((0.5**2)-(0.01**2)))
        
        valor_experimental = (self.GetIntegral())
        
        error = ((abs(valor_experimental - valor_teorico))/valor_teorico)*100
        
        return error

I = Simpson(x,f)
print("El valor de la Integral al calcularlo con el método de Simpson es: ",I.GetIntegral())
print("El error de este método es: ",I.GetError())
