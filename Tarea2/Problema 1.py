class UsuarioRedSocial:
    def __init__(self,nombreusuario,amigos_usuario, lista_publicaciones):
        self.nombreusuario = nombreusuario
        self.amigos_usuario = amigos_usuario
        self.lista_publicaciones = lista_publicaciones
    def DatosUsuario (self,):
        return f'Nombre del usuario {self.nombreusuario} amigos del usuario {self.amigos_usuario} publicaciones del usuario {self.lista_publicaciones}'

amigos_usuario = []
lista_publicaciones = []   
NombreUsuario = input(f"Introduce tu nombre: ")
for i in range(3): 
    nuevo_amigo = input(f"Nombre del amigo: ") 
    amigos_usuario.append(nuevo_amigo) 
 
for i in range(3):
    nueva_publicacion = input(f"inserte la publicacion: ")
    lista_publicaciones.append(nueva_publicacion)
 
facebook = UsuarioRedSocial(NombreUsuario, amigos_usuario, lista_publicaciones)
print(facebook.DatosUsuario())     
    
       
        
    
