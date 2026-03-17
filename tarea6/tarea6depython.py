import pandas as polar
import numpy as np
from datetime import datetime, timedelta
import sqlalchemy
import psycopg2
import mysql.connector
import etl
#lo primero que tenemo aqui es la conexion de la base de datos mysql
#como mysql esta desde el xaamp no requiere de ninguna contraseña solamente señalar el host
#y como usuario ssiempre es root para poder acceder a todas lass bases de datos 
#mi base de datos en mysql se llama "etl_proyecto"
BaseDeDatosMysql = mysql.connector.connect(
    #utilizamos mysql.connector.connect() que basicamente es la llamada a la base de datos
    # y queda asi al pendiente pa cuando yo ocupe cualquier consulta ya sabe pa
    host="localhost",
    user="root",
    password = "",
    database="etl_proyecto"
)
#lo mismo que arriba 
conexion = psycopg2.connect(
    database="etl_proyecto",
    user="postgres",
    password="130802",
    host="127.0.0.1",
    port="5432"
)
#vamos a crear dos dataframe con la informacion que nos devuelva la funcion
#le pasamoss las conexiones a las bases de datos que conectamos
DataFrameVentas, DataFrameClientes = etl.ObtenerInformacion(BaseDeDatosMysql, conexion)
#como ya tenemoos los dataframes con onfirmacion de cada base de datos se la pasamos a la funcion ModificarInformacion
#que atiende el llamado desde el archivo importado etl
DataFrameLimpioFinal = etl.ModificarInformacion(DataFrameVentas, DataFrameClientes)
#despues pasamoslos datos de dataframefinal a la funcion para hacer el archivo csv que no hace mas que 
#generar el archivo con toda la info
etl.HacerNuevoArchivocsv(DataFrameLimpioFinal)




