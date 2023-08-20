import yaml
import numpy as np
import matplotlib.pyplot as plt
import os

#Función auxiliar

#def dar_titulo(ruta:str)-> str:
    
    #nombre= ruta
    
    #titulo = nombre[-1]
    
    #return titulo

#print(dar_titulo())

#Punto 1.3

def recibir_informacion_yml()-> list:
    
    archivo_yml=input("Introduzca la ruta del archivo que quiere hallar de acuerdo con la ruta implementada en las carpetas de cada material- (Ejemplo: Taller_1/Plásticos_Comerciales/kapton.yml): ")
    
    #ruta = dar_titulo(archivo_yml)
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
                        pares = (float(par[1]), float(par[0]))
                        parejas.append(pares)
    return  parejas

#print(recibir_informacion_yml())

#Falta revisar bien la ruta del archivo

#Punto 1.4

def graficar_indice_vs_longitud():
    
    archivo = recibir_informacion_yml()
    
    #Obtener la información de acuerdo con las posiciones del índice o la longitud según corresponda
    
    for tupla in archivo:
        
        eje_x = [tupla[0] for tupla in archivo]
        eje_y = [tupla[1] for tupla in archivo]
        
    #Cálculo promedio
        
    promedio = sum(eje_y)/len(eje_y)
    desviación = np.std(eje_y)
        
    #Gráfico de dispersión
        
    plt.plot(eje_x,eje_y)
        
    #Nombre ejes
        
    plt.title("Gráfica de NOA1348\n" "el n promedio es: " + str(promedio) + "\n y su desviación estándar es: " + str(desviación))
    plt.xlabel("Longitud de onda")
    plt.ylabel("Índice de refracción") 
    
#Revisar ciclo que mande a cada imagen de acuerdo a su carpeta
    carpeta_guardar = "Taller_1/Adhesivos_Ópticos"
    os.makedirs(carpeta_guardar, exist_ok=True)
    
    ruta_guardar = os.path.join(carpeta_guardar, "NOA1348.png")
    plt.savefig(ruta_guardar)
        
    plt.savefig(ruta_guardar)
    plt.show()
        
#archivo_1 = Taller_1/Plásticos_Comerciales/Kapton.png
#archivo_2 = Taller_1/Adhesivos_Ópticos/ NOA1348.png

graficar_indice_vs_longitud()


#Punto 1.5

###PENDIENTE: Revisar como hacer el 1.2 si se puede en python o toca con cilos en bash
### Preguntar que archivo es para el 1.3
###Ver si se puede hacer un ciclo en el 1.4
### Revisar el 1.5

##SEGÚN CHATGPT es así
#def leer_carpetas(carpetas):
    #for categoria in categorias:
        #for archivo in os.listdir(categoria):
            #if archivo.endswith(".yml"):
                #ruta_archivo = os.path.join(categoria, archivo)
                #carpeta_guardar = os.path.join("Resultados", carpeta)
                #os.makedirs(carpeta_guardar, exist_ok=True)
                #graficar_indice_vs_longitud(ruta_archivo, carpeta_guardar)
#carpetas = ["Adhesivos_Ópticos", "Combustible", "Materia Inorgánica", "Materia Orgánica", "Mezclas", "Plásticos_Comerciales", "Vidrio"]
#leer_carpetas(carpetas)