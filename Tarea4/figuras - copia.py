import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sqlite3

def poblar_ventas():
    print("1. Generando 3500 registros de Ventas...")
    
    num_registros = 3500 
    
    # Generamos fechas aleatorias para el último año
    fecha_inicio = datetime(2023, 1, 1)
    fechas = [fecha_inicio + timedelta(days=int(np.random.randint(0, 365))) for _ in range(num_registros)]
    
    # Creamos el DataFrame con la estructura exacta que pediste
    Mi_Tabla_Ventas = pd.DataFrame({
        'ID_Cliente': np.random.randint(1, 501, num_registros), # Asignamos ventas a los clientes del 1 al 500
        'monto': np.round(np.random.uniform(50.0, 5000.0, num_registros), 2),
        'fecha': [fecha.strftime('%Y-%m-%d') for fecha in fechas] # Formato de fecha limpio
    })
    
    # ¡TRUCO DE LIMPIEZA! Agregamos algunos nulos en la columna 'monto' 
    # para que tu script ETL tenga algo que limpiar con .dropna()
    indices_nulos = np.random.choice(Mi_Tabla_Ventas.index, 80, replace=False)
    Mi_Tabla_Ventas.loc[indices_nulos, 'monto'] = None
    
    print("2. Guardando en la base de datos...")
    
    # --- PARA USAR MYSQL REAL DESCOMENTA ESTO Y COMENTA LO DE SQLITE ---
    # from sqlalchemy import create_engine
    # uri_mysql = "mysql+pymysql://usuario:password@localhost:3306/base_datos"
    # conexion = create_engine(uri_mysql)
    
    # --- PARA CREAR EL ARCHIVO SQLITE COMO EN TU IMAGEN ---
    conexion = sqlite3.connect('DatosVentas_FuenteB.db')
    
    # Guardamos el DataFrame en la tabla 'Ventas'
    Mi_Tabla_Ventas.to_sql('Ventas', conexion, index=False, if_exists='replace')
    
    # Cerramos la conexión de SQLite
    if isinstance(conexion, sqlite3.Connection):
        conexion.close()
        
    print(f"¡Listo! Se han generado {num_registros} registros en la tabla Ventas.")

if __name__ == "__main__":
    poblar_ventas()