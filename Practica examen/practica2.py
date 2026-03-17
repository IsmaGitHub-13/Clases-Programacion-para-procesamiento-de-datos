class Articulo:
    def __init__(self,nombre, stock):
        self.nombre = nombre
        self.stock = stock
    def agregar_stock(self, cantida_nueva):
        self.stock = self.stock + cantida_nueva
        return f"Se agregaron {cantida_nueva} unidades. Stock total de {self.nombre} es {self.stock}"
    def mostrar_informacion(self):
        return f"Quedan {self.stock} unidades"
class Videojuego(Articulo):
    def __init__(self, nombre, stock, consola):
        super().__init__(nombre, stock)
        self.consola = consola
    def vender(self, cantidad_vender):
        if (cantidad_vender <= self.stock):
            self.stock = self.stock - cantidad_vender
            return f"Vendiste {cantidad_vender} copias de {self.nombre}" 
        else:
            return f"Error: No hay suficiente stock. Solo quedan {self.stock} unidades."

Juego = Videojuego("zelda", 5,"switch")
print(Juego.vender(3))  
print(Juego.agregar_stock(10))
print(Juego.vender(3))  
print(Juego.mostrar_informacion())    