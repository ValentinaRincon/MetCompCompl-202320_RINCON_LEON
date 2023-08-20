#Punto 2.1

class Mineral:
    def _init_(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composición, sistema_cristalino, specific_gravity):
        
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composición = composición
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity
        
    def leer(self):
        print(f"Nombre: {'self.nombre'}")
        print(f"Dureza: {'self.dureza'}")
        print(f"Lustre: {'self.lustre'}")
        print(f"Rompimiento_por_fractura: {'VERDADERO' if self.rompimiento_por_fractura else 'FALSO'}")
        print(f"Color: {self.color}")
        print(f"Composición: {self.composición}")
        print(f"Sistema_Cristalino: {self.cristalino}")
        print(f"Specific_gravity: {self.specific_gravity}")
        
#Falta el punto 2.2