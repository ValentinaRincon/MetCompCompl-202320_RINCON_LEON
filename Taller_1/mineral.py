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

    def __str__(self):
        return f"Mineral: {self.nombre}\n" \
            f"Dureza: {self.dureza}\n" \
            f"Rompimiento por Fractura: {'VERDADERO' if self.rompimiento_por_fractura else 'FALSO'}\n" \
            f"Color: {self.color}\n" \
            f"Composición: {self.composición}\n" \
            f"Lustre: {self.lustre}\n" \
            f"Gravedad Específica: {self.specific_gravity}\n" \
            f"Sistema Cristalino: {self.sistema_cristalino}\n"

#Punto 2.2

    def silicato(self): 
        si = "Si"
        ox = "O"
        
        return si in self.composición and ox in self.composición
    
    def densidad(self):
        densidad_agua = 1000
        return float(self.specific_gravity) * densidad_agua
    
    def color_comun(self):
        
        colores = self.color
        mineral = self.nombre
        
        plt.bar(mineral, [1] * len(mineral), color=colores)
        plt.show()
            
    def caracteristicas(self):
        rompimiento =  "Escision"
        tipo = self.rompimiento_por_fractura
        if tipo.title() is True:
            rompimiento = "Fractura"
        print("{0},{1}.{2}").format(self.dureza,rompimiento,self.sistema_cristalino)