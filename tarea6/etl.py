import pandas as Polar

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
    return dataFrame_ventas, dataFrame_clientes
def ModificarInformacion(DataFrameVentas, DataFrameClientes):
    DataFrameVentasLimpio = DataFrameVentas.drop_duplicates()
    DataFrameClientesLimpio = DataFrameClientes.drop_duplicates()
    DataFrameVentasLimpio = DataFrameVentasLimpio.dropna()
    DataFrameClientesLimpio = DataFrameClientesLimpio.dropna()
    DataFrameFinal = DataFrameClientesLimpio.merge(
        DataFrameVentasLimpio,
        on='id_cliente',
        how='inner'
    )
    DataFrameFinal['fecha'] = Polar.to_datetime(DataFrameFinal['fecha'])
    DataFrameFinal.loc[DataFrameFinal['monto'] <= 0, 'monto'] = 0 
    DataFrameFinal['Total_Gastado'] = DataFrameFinal.groupby('id_cliente')['monto'].transform('sum')
    DataFrameFinal['Numero_Venta_Ciudad'] = DataFrameFinal.groupby('ciudad').cumcount() + 1
    return(DataFrameFinal)
def HacerNuevoArchivocsv(DataFrameFinal):
    DataFrameFinal.to_csv(ruta_salida, index=False, sep=",")
    return(DataFrameFinal)
    
ruta_salida = r"D:\Clase sandre python\Tarea6.csv"
