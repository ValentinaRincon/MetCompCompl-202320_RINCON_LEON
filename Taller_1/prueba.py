import numpy as np
from mineral import Mineral

f = open("Taller_1/minerales.txt","r", encoding="utf-8")
file = f.readlines()
f.close()
n_minerales = len(file) - 1  # Calcula el número de minerales en el archivo
minerales = np.empty(n_minerales, dtype=Mineral)  # Crea un arreglo de NumPy con el tamaño adecuado
for i, linea in enumerate(file[1:18]):
    atributos = linea.strip().split("\t")
    nombre = atributos[0]
    dureza = atributos[1]
    rompimiento_por_fractura = atributos[2]
    color = atributos[3]
    composicion = atributos[4]
    lustre = atributos[5]
    specific_gravity = atributos[6]
    sistema_cristalino = atributos[7]

    mineral_i = Mineral(nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino)
    minerales[i] = mineral_i

print(minerales)