import pandas as pd

# 1. EXTRACCIÓN
def extraer(ruta):
    df = pd.read_csv(ruta, sep=',')
    return df

# 2. TRANSFORMACIÓN
def transformar(df):
    df['Precio'] = df['Precio'].fillna(0)
    df['Precio'] = pd.to_numeric(df['Precio'])
    df['Cantidad'] = pd.to_numeric(df['Cantidad'])
    
    df['total_venta'] = df['Precio'] * df['Cantidad']
    
    return df

# 3. CARGA
def cargar(df, ruta_salida):
    df.to_csv(ruta_salida, index=False, sep=';')

# BLOQUE PRINCIPAL
if __name__ == "__main__":
    ruta_entrada = r"D:\Clase sandre python\ventas_detalladas.csv"
    ruta_salida = r"D:\Clase sandre python\resultado.csv"

    print("Iniciando proceso ETL...")
    datos = extraer(ruta_entrada)
    datos_transformados = transformar(datos)
    cargar(datos_transformados, ruta_salida)

    print("Proceso ETL completado con éxito. Se ha generado el archivo 'resultado.csv'.")