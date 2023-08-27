import numpy as np

from mineral import Mineral

lista = []
f = open("Taller_1/minerales.txt","r", encoding="utf-8")
#with open('Taller_1/minerales.txt', 'r') as file:
file = f.readlines()
for linea in file[1:17]:
    
    atributos = linea.strip().split("\t")
    nombre = atributos[0]
    dureza = atributos[1]
    rompimiento_por_fractura = atributos[2]
    color = atributos[3]
    composicion = atributos[4]
    lustre = atributos[5]
    specific_gravity = atributos[6]
    sistema_cristalino = atributos[7]
        
    mineral_i = Mineral(nombre,dureza,lustre,rompimiento_por_fractura,color,composicion,specific_gravity,sistema_cristalino)
        
    lista.append(mineral_i)
    
#Mineral.leer(lista[1])
#print(Mineral.densidad(lista[1]))

def contar_silicatos():
    
    contador = 0
    
    densidad_promedio = 0

    for mineral in lista:

        if mineral.silicato():

            contador +=1
            densidad_promedio += mineral.densidad()
            
    densidad = densidad_promedio/contador
    
    return contador,densidad
print(contar_silicatos())


