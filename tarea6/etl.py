import pandas as Polar
#aca ocurre la magia
def ObtenerInformacion(BaseDedatosMysql, BaseDeDatosPostgre):
    CursorMysql = BaseDedatosMysql.cursor()
    CursorMysql.execute("SELECT * FROM Ventas")
    datos_ventas = CursorMysql.fetchall()
    dataFrame_ventas = Polar.DataFrame(datos_ventas, columns=['id_venta', 'id_cliente', 'monto', 'fecha'])
    CursorMysql.close()

    CursorPostgre = BaseDeDatosPostgre.cursor()
    CursorPostgre.execute("SELECT * FROM Clientes")
    datos_clientes = CursorPostgre.fetchall()
    dataFrame_clientes = Polar.DataFrame(datos_clientes, columns=['id_cliente', 'nombre', 'ciudad'])
    CursorPostgre.close()
    #ambas consultas no sos mas que un SELECT de toda la informacion de ambas tablas en la bases de dtaos correspondientes
    # y despues insertados en dos data frame diferentes que retornamos para que los tome la funcion modificar informacion
    return dataFrame_ventas, dataFrame_clientes
def ModificarInformacion(DataFrameVentas, DataFrameClientes):
    DataFrameVentasLimpio = DataFrameVentas.drop_duplicates()
    DataFrameClientesLimpio = DataFrameClientes.drop_duplicates()
    #utilizamos.drop_duplicates() para limpiar ambas tablas de archivos que sean exactamente iguales y asi evitar datos basura
    #creamos dos nuevos dataframes donde ya no se encuentren esos duplicados
    DataFrameVentasLimpio = DataFrameVentasLimpio.dropna()
    DataFrameClientesLimpio = DataFrameClientesLimpio.dropna()
    #tomamos los dataframes sin duplicados y metemos otro filtro con .dropna()
    #elimina cualquier archivo vacio y lo quita de la tabla, igual y nos perdemos algun dato por no ponerle por ejemplo N/A
    # para que asi no desapareza por completa la linean de informacion
    DataFrameFinal = DataFrameClientesLimpio.merge(
        DataFrameVentasLimpio,
        on='id_cliente',
        how='inner'
    )
    #utilizamos dataframefinal como archivo donde juntaremos informacion sobre las dos tablas y la asociaremos de forma que si 
    #coinciden en el mismo id_cliente queire decir que los registros pertenecen ala persona o cosa a identificar
    DataFrameFinal['fecha'] = Polar.to_datetime(DataFrameFinal['fecha'])
    #le damos formato a la fecha de 00/00/0000 para que asi ya no aparezcan como strings si no mas bien como fechas
    DataFrameFinal.loc[DataFrameFinal['monto'] <= 0, 'monto'] = 0 
    #aqui tomamos todo el dataframe final y en la columba monto hacemos una condicion donde si la cantidad es menor o igual a cero 
    #pues que la iguale a cero para que asi no hayan datos negativos
    DataFrameFinal['Total_Gastado'] = DataFrameFinal.groupby('id_cliente')['monto'].transform('sum')
    #creamos una nueva columna llamada "total gastado" que suma todas las compras(monto) de todoss lo que tengan el mismo "id_cliente"
    #como solo van a coincidir todas las compras de la misma persona se suman e imprimen, muchass veces en cada linea porque no
    #quise hacer un nuevoa archivo
    DataFrameFinal['Numero_Venta_Ciudad'] = DataFrameFinal.groupby('ciudad').cumcount() + 1
    #lo mismo que con monto pero aca con ciudad, va contando 1 en uno cada que haya compras en la misma ciudad
    return(DataFrameFinal)

def HacerNuevoArchivocsv(DataFrameFinal):
    DataFrameFinal.to_csv(ruta_salida, index=False, sep=",")
    #hacemos el csv faak tuvo dificil
    #y hace poco descubri que era en equipo
    return(DataFrameFinal)
    
ruta_salida = r"D:\Clase sandre python\Tarea6.csv"
#aca e donde se creara el archivo 
