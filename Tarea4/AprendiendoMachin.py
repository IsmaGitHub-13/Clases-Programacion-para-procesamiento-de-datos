import pandas as Polar

def ObtenerInformacion(ruta):
    Mi_DataFrame = Polar.read_csv(ruta, sep= ",")
    return(Mi_DataFrame)

def ModificarInformacion(Mi_DataFrame):
    Mi_DataFrame['Precio_Unitario'] = Mi_DataFrame['Precio_Unitario'] * 2
    return(Mi_DataFrame)

def HacerNuevoArchivocsv(Mi_DataFrame, ruta_salida):
    Mi_DataFrame.to_csv(ruta_salida, index=False, sep=",")
    return(Mi_DataFrame)
    

ruta_salida = r"D:\Clase sandre python\panda_practica_modificado.csv"
ruta_entrada  = r"D:\Clase sandre python\panda_practica.csv"
datos = ObtenerInformacion(ruta_entrada)
MisDatosTransformados = ModificarInformacion(datos)
print("--------------------------------------------------------------------------------------")
HacerNuevoArchivocsv(MisDatosTransformados, ruta_salida)
print(MisDatosTransformados)

