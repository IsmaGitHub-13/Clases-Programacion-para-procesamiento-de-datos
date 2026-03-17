class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def mostrar_info(self) :
        return f"Producto: {self.nombre} - Precio: ${self.precio}"
    
class Laptop(Producto): 
    def  __init__(self, nombre, precio,ram):
        super().__init__(nombre, precio)
        self.ram = ram
    def calcular_total(self, cantidad):
        resultado = self.precio * cantidad
        return f"Total por {cantidad} laptops ({self.ram} GB RAM): ${resultado}"
    
laptops = int(input("¿Cuantas Laptops quieres comprar: "))
Laptop = Laptop("ASUS", 15000, 16)
print(Laptop.mostrar_info())
print(Laptop.calcular_total(laptops))

      
    
        