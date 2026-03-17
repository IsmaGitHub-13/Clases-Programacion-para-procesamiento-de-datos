import pandas as pd
import io
csv_data = """Peso,Potencia,Consumo
10,2,40
30,5,70
50,8,90"""
df = pd.read_csv(io.StringIO(csv_data))
df.to_csv(r"D:\Clase sandre python\CalcularConsumo.csv", index=False)
print("¡Datos de la libreta cargados exitosamente!")
print(df)