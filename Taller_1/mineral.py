import matplotlib.pyplot as plt

#Punto 2.1

class Mineral:
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composición, specific_gravity, sistema_cristalino):
        
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composición = composición
        self.specific_gravity = specific_gravity
        self.sistema_cristalino = sistema_cristalino
        
    def leer(self):
        print(f"Nombre: {'self.nombre'}")
        print(f"Dureza: {'self.dureza'}")
        print(f"Lustre: {'self.lustre'}")
        print(f"Rompimiento_por_fractura: {'VERDADERO' if self.rompimiento_por_fractura else 'FALSO'}")
        print(f"Color: {self.color}")
        print(f"Composición: {self.composición}")
        print(f"Sistema_Cristalino: {self.cristalino}")
        print(f"Specific_gravity: {self.specific_gravity}")
        
#Punto 2.2

    def silicato(self): 
        si = "Si"
        o = "O"
        return si in self.composición and o in self.composición
    
    def densidad(self):
        densidad_agua = 1000
        return self.specific_gravity * densidad_agua
    
    def color_comun(self):
        
        colores = self.color
        mineral = self.nombre
        
        plt.bar(mineral, [1] * len(mineral), color=colores)
        plt.show()
            
    def caracteristicas(self):
        rompimiento =  "Escision"
        if self.rompimiento_por_fractura is True:
            rompimiento = "Fractura"
        print("{0},{1}.{2}").format(self.dureza,rompimiento,self.sistema_cristalino)
        

        
        