import yaml
import numpy as np

def recibir_informacion_yml():
    
    archivo_yml=input("Introduzca la ruta del archivo que quiere hallar: ")
    
    #Cargar archivo
    
    with open(archivo_yml, 'r') as yml_file:
        
        dato = yaml.safe_load(yml_file)
        
    #Iniciar las tuplas
    
    parejas = []
    
    #Leer archivo
    
    if 'DATA' in dato and dato['DATA']:
        for entrada in dato['DATA']:
            if 'data' in entrada and entrada['data']:
                lineas = entrada['data'].strip().split('\n')
                
                for valor in lineas:
                    par = valor.split()
                    
                    if len(par) == 2:
                        pares = (float(par[0]), float(par[1]))
                        parejas.append(pares)
    return  parejas

#archivo_yml= 'Taller_1/Adhesivos_Ópticos/NOA61.yml'

print(recibir_informacion_yml())

#Falta revisar bien la ruta del archivo

