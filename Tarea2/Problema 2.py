
class Personaje : 
    def __init__(self,nombrepersonaje, nivelalcanzado, puntosvida):
        self.nombrepersonaje = nombrepersonaje
        self.nivelalcanzado = nivelalcanzado
        self.puntosvida = puntosvida
        
class Guerrero(Personaje):
    def __init__(self, nombrepersonaje, nivelalcanzado, puntosvida, Fuerza):
        super().__init__(nombrepersonaje, nivelalcanzado, puntosvida)
        self.fuerza = Fuerza
    def DatosUsuario(self,) :
        return f'!!El guerrero a sido creado¡¡ Nombre del guerrero: {self.nombrepersonaje} Nivel del personaje: {self.nivelalcanzado} puntos de vida: {self.puntosvida} Fuerza: {self.fuerza}'
                   
class Mago(Personaje):
    def __init__(self, nombrepersonaje, nivelalcanzado, puntosvida, puntosrecuperacion):
        super().__init__(nombrepersonaje, nivelalcanzado, puntosvida)      
        self.puntosrecuperacion = puntosrecuperacion
    def DatosUsuario(self,) :
        
        return f'¡¡El mago a sido creado!! Nombre del mago: {self.nombrepersonaje} Nivel del personaje: {self.nivelalcanzado} puntos de vida: {self.puntosvida} puntos de recuperacion: {self.puntosrecuperacion}'     
    
OpcionDeJugador = int(input("Presione 1 si quiere un guerrero, presione 2 para un mago: ")) 
NombrePersonaje = None
NivelAlcanzado = None
PuntosDeVida = None
match OpcionDeJugador :
    case 1 : 
        NombrePersonaje = input(f"Ingrese el nombre del guerrero: ")
        NivelAlcanzado = input(f"Ingrese el nivel alcanzado: ")
        PuntosDeVida = input(f"Ingrese los puntos de vida: ")
        Fuerza = input(f"ingrese la fuerza del guerrero: ")
        MiPersonaje = Guerrero(NombrePersonaje, NivelAlcanzado, PuntosDeVida, Fuerza)
        print(MiPersonaje.DatosUsuario())        
    case 2 :
        NombrePersonaje = input(f"Ingrese el nombre del mago: ")
        NivelAlcanzado = input(f"Ingrese el nivel alcanzado: ")
        PuntosDeVida = input(f"Ingrese los puntos de vida: ")
        PuntosDeRecuperacion = input(f"ingrese los puntos de vida extra: ")
        MiPersonaje = Mago(NombrePersonaje, NivelAlcanzado, PuntosDeVida, PuntosDeRecuperacion)
        print(MiPersonaje.DatosUsuario())  
         

        
