from unidecode import unidecode
import yaml
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

#Función auxiliar

#def dar_titulo(ruta:str)-> str:
    
    #nombre= ruta
    
    #titulo = nombre[-1]
    
    #return titulo

#print(dar_titulo())

#Punto 1.3

def recibir_informacion_yml(archivo_yml)-> list:
     
    #ruta = dar_titulo(archivo_yml)
    #Cargar archivo
    with open(archivo_yml,'r') as yml_file:
        
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



#print(recibir_informacion_yml("Taller_1\Descargas\Adhesivos Opticos\Loctite.yml"))

#Punto 1.4

def auxiliar_categoria(ubicacion_archivo):
    
    cambio = ubicacion_archivo.split("/")
    categoria = cambio[3].split(".")[-2]
        
    return categoria

def graficar_indice_vs_longitud(ruta:str):
    
    archivo = recibir_informacion_yml(ruta)
    
    #Obtener la información de acuerdo con las posiciones del índice o la longitud según corresponda
    
    for tupla in archivo:
        
        eje_x = [tupla[0] for tupla in archivo]
        eje_y = [tupla[1] for tupla in archivo]
        
    #Cálculo promedio
        
    promedio = round(sum(eje_y)/len(eje_y),3)
    desviación = round(np.std(eje_y),3)
        
    #Gráfico de dispersión
        
    plt.scatter(eje_x,eje_y)
    
    #Obtención del título de la categoría
    categoria = auxiliar_categoria(ruta) 
    
    #Nombre ejes
        
    plt.title("Gráfica de "+str(categoria) +" el n promedio es:" +str(promedio)+"\n" " y su desviación estándar es: " + str(desviación))
    plt.xlabel("Longitud de onda")
    plt.ylabel("Índice de refracción") 

#Revisar ciclo que mande a cada imagen de acuerdo a su carpeta

    if categoria == "NOA1348":
        carpeta_guardar = "Taller_1/Descargas/Adhesivos Ópticos"
        os.makedirs(carpeta_guardar, exist_ok=True)
        ruta_guardar = os.path.join(carpeta_guardar, "NOA1348.png")
        plt.savefig(ruta_guardar)
        
    else:
        carpeta_guardar = "Taller_1/Descargas/Plásticos Comerciales"
        os.makedirs(carpeta_guardar, exist_ok=True)
        ruta_guardar = os.path.join(carpeta_guardar, "Kapton.png")
        plt.savefig(ruta_guardar)
    
    plt.show()
        

#Descomentar desde lista_archivos hasta el for para ver el punto 1_4
#lista_archivos = ["Taller_1/Descargas/Plásticos Comerciales/Kapton.yml", "Taller_1/Descargas/Adhesivos Ópticos/NOA1348.yml"]


#for elemento in lista_archivos:
    
    #grafica = graficar_indice_vs_longitud(elemento)
    
    #print()

#Punto 1.5

def rutas():
    
    # Nombre de la carpeta principal
    carpeta_principal = 'Taller_1/Descargas'
    
        # Abre el archivo CSV en modo lectura
    with open('Taller_1/indices_refraccion.csv', 'r', newline='') as archivo_csv:
        # Crea un lector CSV
        lector = csv.reader(archivo_csv, delimiter='\t')  # Ajusta el delimitador según tu archivo CSV

        # Inicializa una variable booleana para rastrear si es el primer ciclo
        primer_ciclo = True

        # Itera a través de las filas y descarga los archivos .yml
        for fila in lector:
            if primer_ciclo:
                primer_ciclo = False
                continue  # Omitir el primer ciclo
            
            categoria = fila[0].split(',')[0]
            material = fila[0].split(',')[2]
            
            ruta_guardado = f"{carpeta_principal}/{categoria}/{material}.yml"
            
            ruta_decodificada = ruta_guardado.encode('latin-1').decode('utf-8')
            
            print(ruta_decodificada)
            
            graficar_indice_vs_longitud_todos(ruta_decodificada)
            

        
def auxiliar_grupo(ubicacion_archivo):

    cambio = ubicacion_archivo.split("/")
    grupo = cambio[2]
        
    return grupo
        
def graficar_indice_vs_longitud_todos(ruta:str):
    
    plt.figure()
    
    archivo = recibir_informacion_yml(ruta)
    
    #Obtener la información de acuerdo con las posiciones del índice o la longitud según corresponda
    
    for tupla in archivo:
        
        eje_x = [tupla[0] for tupla in archivo]
        eje_y = [tupla[1] for tupla in archivo]
        
    #Cálculo promedio
        
    promedio = round(sum(eje_y)/len(eje_y),3)
    desviación = round(np.std(eje_y),3)
        
    #Gráfico de dispersión
        
    plt.scatter(eje_x,eje_y)
    
    #Obtención del título de la categoría
    categoria = auxiliar_categoria(ruta)
    grupo = auxiliar_grupo(ruta)
    
    #Nombre ejes
        
    plt.title("Gráfica de "+str(categoria) +" el n promedio es:" +str(promedio)+"\n" " y su desviación estándar es: " + str(desviación))
    plt.xlabel("Longitud de onda")
    plt.ylabel("Índice de refracción") 
    
    carpeta_guardar = "Taller_1/Descargas/"+grupo
    os.makedirs(carpeta_guardar, exist_ok=True)
    ruta_guardar = os.path.join(carpeta_guardar, categoria+".png")
    plt.savefig(ruta_guardar)
    plt.close()
    
if __name__ == "__main__":
    rutas()
    