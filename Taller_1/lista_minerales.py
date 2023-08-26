import numpy as np 
from mineral import Mineral
lista= []
f = open("Taller_1/minerales.txt","r", encoding="utf-8")
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
        
    mineral_i = Mineral(nombre,dureza,rompimiento_por_fractura,color,composicion,lustre,specific_gravity,sistema_cristalino)
        
    lista.append(mineral_i)
    
def contar_silicatos():

    for mineral in lista:
        print(mineral)
        contador = 0

        if mineral.silicato() is True:

            contador +=1

    return contador
print(contar_silicatos())

