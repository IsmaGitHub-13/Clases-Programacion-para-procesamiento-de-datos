import pandas as pd

# 1️ EXTRACCIÓN
def extraer(ruta):
    df = pd.read_csv(ruta)
    return df

# 2️ TRANSFORMACIÓN
def transformar(df):

    df_limpio = df.drop_duplicates()
    df_limpio["experience level"] = df_limpio["experience_level"].replace({
    "EN": "Junior",
    "MI": "Mid Level",
    "SE": "Senior",
    "EX": "Ejecutive"
})
    df_limpio["employment type"] = df_limpio["employment_type"].replace({
    "FT": "full time",
    "PT": "half-time",
    "CT": "contract",
    "FL": "Freelance"
})
    df_limpio["company size"] = df_limpio["company_size"].replace({
    "L": "BIG",   
    "M": "MEDIAN", 
    "S": "SMALL"   
})
    
    df_limpio["experience in the company"] = 2026 - df_limpio["work_year"].astype(int)
    df_limpio = df_limpio.drop(columns=["experience_level"])
    df_limpio = df_limpio.drop(columns=["employment_type"])
    df_limpio = df_limpio.drop(columns =["company_size"])
    def clasificar_salario(salario):
        if salario > 100000:
            return "HIGH"
        elif salario > 50000:
            return "MID"
        else:
            return "LOW"

    df_limpio["salary level"] = df_limpio["salary_in_usd"].apply(clasificar_salario)
    df_final = df_limpio[df_limpio["salary_in_usd"] > 0]
    return df_final
def cargar(df, ruta_salida):
    df.to_csv(ruta_salida, index=False, sep=";")
    
if __name__ == "__main__":

    ruta_entrada = r"D:\Clase sandre python\ds_salaries.csv"
    ruta_salida = r"D:\Clase sandre python\ds_salaries_procesado.csv"

    datos = extraer(ruta_entrada)
    datos_limpios = transformar(datos)
    cargar(datos_limpios, ruta_salida)

    print("Proceso ETL completado.")
   