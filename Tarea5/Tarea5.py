import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sqlalchemy import create_engine

def poblar_mysql():
    print("1. Generando 3000 registros de Ventas...")
    
    # Generamos fechas aleatorias para el último año
    fecha_inicio = datetime(2023, 1, 1)
    fechas = [fecha_inicio + timedelta(days=int(np.random.randint(0, 365))) for _ in range(3000)]
    
    # Creamos el DataFrame simulando la estructura que necesitas
    Mi_Tabla_Ventas = pd.DataFrame({
        'ID_Cliente': np.random.randint(1, 501, 3000), # Clientes del 1 al 500
        'monto': np.round(np.random.uniform(50.0, 5000.0, 3000), 2),
        'fecha': fechas
    })
    
    # Metemos algunos valores nulos y negativos aleatorios (como en tu ejemplo) para probar la limpieza después
    indices_nulos = np.random.choice(Mi_Tabla_Ventas.index, 50, replace=False)
    Mi_Tabla_Ventas.loc[indices_nulos, 'monto'] = None
    
    indices_negativos = np.random.choice(Mi_Tabla_Ventas.index, 20, replace=False)
    Mi_Tabla_Ventas.loc[indices_negativos, 'monto'] = -50.00
    
    print("2. Conectando a MySQL...")
    # CAMBIA ESTOS DATOS por los de tu servidor MySQL local
    usuario = 'root'
    password = 'tu_password'
    host = 'localhost'
    puerto = '3306'
    base_datos = 'tu_base_de_datos'
    
    # Creamos el motor de conexión usando SQLAlchemy y PyMySQL
    uri_mysql = f"mysql+pymysql://{usuario}:{password}@{host}:{puerto}/{base_datos}"
    conexion_mysql = create_engine(uri_mysql)
    
    print("3. Cargando los datos en la tabla 'Ventas' de MySQL...")
    # if_exists='replace' creará la tabla si no existe, o la sobreescribirá si ya existe
    Mi_Tabla_Ventas.to_sql('Ventas', conexion_mysql, index=False, if_exists='replace')
    
    print("¡Listo! Los 3000 registros ya están en tu gestor de MySQL.")

if __name__ == "__main__":
    poblar_mysql()