arboles = ["manzano", "pino","madroño","eucalipto", "nogal","olivo", "almendro"]
arbolBuscado = "Tabachin"
if arbolBuscado in arboles :
    for Arbol in arboles :
        print(Arbol)
        if Arbol == arbolBuscado :
            break
else :
    print('El arbol "Tabachin" no esta en la lista')         