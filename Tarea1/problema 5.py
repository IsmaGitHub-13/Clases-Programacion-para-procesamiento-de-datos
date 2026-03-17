Palabra = "Jugo" 
letra_vocales = ["a","e","i","o","u","A","E","I","O","U"]

def Contar_Vocales(Texto):
  Contador_De_Vocales = 0
  for letra in Texto:
      if (letra in letra_vocales):
       Contador_De_Vocales = Contador_De_Vocales + 1
  return Contador_De_Vocales
    
print("La cantidad de vocales en el texto es:", Contar_Vocales(Palabra))
    
    
