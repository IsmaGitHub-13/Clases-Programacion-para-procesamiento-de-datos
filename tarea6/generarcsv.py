import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

print("Generando 3000 registros de ventas...")

fecha_inicio = datetime(2022, 1, 1)
fechas = [fecha_inicio + timedelta(days=random.randint(0, 730)) for _ in range(3000)]
id_clientes = [random.randint(1, 15) for _ in range(3000)]

montos = []
for _ in range(3000):
    prob = random.random()
    if prob < 0.05:
        montos.append(round(random.uniform(-500.0, -10.0), 2))
    elif prob < 0.10:
        montos.append(np.nan)
    else:
        montos.append(round(random.uniform(50.0, 5000.0), 2))

df_ventas = pd.DataFrame({
    'id_cliente': id_clientes,
    'monto': montos,
    'fecha': fechas
})

# AQUI ESTA LA MAGIA: Lo guardamos como CSV en tu compu
df_ventas.to_csv('ventas_para_mysql.csv', index=False)
print("✅ Archivo 'ventas_para_mysql.csv' creado en tu carpeta.")