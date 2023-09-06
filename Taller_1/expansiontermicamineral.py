import csv
import matplotlib.pyplot as plt
from mineral import Mineral
import numpy as np

class ExpansionTermicaMineral(Mineral):
    
    def __init__(self,archivo):
    
        with open(archivo, 'r', newline='') as archivo_csv:
            
        # Crea un lector CSV
        
            lector = csv.reader(archivo_csv, delimiter='\t')
            
            primer_ciclo = True

        # Itera a través de las filas y descarga los archivos .yml
            lis_temperatura = np.array([])
            lis_volumen = np.array([])
            for fila in lector:
                
                if primer_ciclo:
                    primer_ciclo = False
                    continue  # Omitir el primer ciclo

                temperatura = float(fila[0].split(',')[0])
                volumen = float(fila[0].split(',')[1])
                
                lis_temperatura = np.append(lis_temperatura,temperatura)
                lis_volumen = np.append(lis_volumen,volumen)
            
            alpha = ExpansionTermicaMineral.alpha(lis_temperatura,lis_volumen)
            error = ExpansionTermicaMineral.error(alpha)
            ExpansionTermicaMineral.graficar(lis_temperatura,lis_volumen,alpha,error)
                
                
    def pendiente(lis_temperatura,lis_volumen):
    
        t1 = lis_temperatura[0]
        t2 = lis_temperatura[-1]
        
        v1 = lis_volumen[0]
        v2 = lis_volumen[-1]
        
        return (v2-v1)/(t2-t1)
    
    def alpha(lis_temperatura, lis_volumen):
        
        pendiente = ExpansionTermicaMineral.pendiente(lis_temperatura,lis_volumen)
        
        lis_a = np.array([])
        
        for vol in lis_volumen:
            
            a = (1/vol)*pendiente
            
            lis_a = np.append(lis_a,a)
            
        return lis_a
    
    def error(a):
        
        return np.std(a)/np.sqrt(len(a))
    
    def graficar(lis_temperatura,lis_volumen,lis_a,error):
        
        fig,axs = plt.subplots(nrows=1,ncols=2,figsize=(15,4.5))
        
        t = lis_temperatura
        v = lis_volumen
        a = lis_a
        e = error
        
        
        axs[0].scatter(x=t,y=v)
        axs[0].set_ylabel(r'Volumen, (cm^3)')
        axs[0].set_xlabel('Temperatura (°C)')
        axs[0].set_title('Temperatura vs Volumen')
        
        axs[1].scatter(x=a,y=v)
        axs[1].set_ylabel(r'Coeficiente de expansión térmica, (1/°C)')
        axs[1].set_xlabel('Temperatura (°C)')
        axs[1].set_title('Temperatura vs Coeficiente de expansión térmica')
        
        plt.suptitle('Temperatura y Volumen, el error de aplha es '+str(e))
        
        plt.tight_layout()
        plt.show()
                

    
        
        