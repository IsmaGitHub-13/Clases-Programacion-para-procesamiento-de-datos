class Vuelo :
    def __init__(self,Numero_vuelo, numero_pasajeros, destino):
        self.Numero_vuelo = Numero_vuelo
        self.numero_pasajeros = numero_pasajeros
        self.destino = destino

class Avion :
    def __init__(self, Numero_sientos,lista_destinos):
        self.Numeroasientos = Numero_sientos
        self.lista_destinos = lista_destinos
        

print("--- REGISTRO DE VUELO ---")
vuelo_num = input("Introduce el número de vuelo: ")
Numero_pasajeros = input("Introduce el número de pasajeros: ")
vuelo_destino = input("Introduce el destino del vuelo: ")
mi_vuelo = Vuelo(vuelo_num, Numero_pasajeros, vuelo_destino)
print("\n--- REGISTRO DE AVIÓN ---")
Numero_asientos = input("Introduce el número de asientos del avión: ")
destinos = input("Introduce los destinos del avión (separados por coma): ")
a_destinos = destinos.split(',') 

mi_avion = Avion(Numero_asientos, a_destinos) 
    
Si_se_puede_pasajeros = Numero_asientos >= Numero_pasajeros 
Si_se_puede_destino = vuelo_destino in a_destinos 
    
if Si_se_puede_pasajeros and Si_se_puede_destino :
    print("El vuelo si se puede realizar") 
else :
    print("el vuelo no se puede realizar")
    if not Si_se_puede_pasajeros :
        print("El numero de pasajeros es mayor a los asientos") 
            
    if not Si_se_puede_destino :
            print("El avion no va a ese destino")