import pandas as pd

def extraer(ruta):
    df = pd.read_csv(ruta, sep=',')
    return df

def Prediccion(df, w1, w2, b):
    df['Peso'] = pd.to_numeric(df['Peso']).fillna(0)
    df['Potencia'] = pd.to_numeric(df['Potencia']).fillna(0)
    df['consumo_predicho'] = (df['Peso'] * w1) + (df['Potencia'] * w2) + b
    if 'Consumo' in df.columns:
        df['error_prediccion'] = df['consumo_predicho'] - df['Consumo']
    return df

def perroParado(df):
    m = len(df)
    Sumatoria = ((df['consumo_predicho'] - df['Consumo'])**2).sum()
    ResultadoFuncionCosto = (1 / (2*m)) * Sumatoria
    return ResultadoFuncionCosto

def GradienteDesendiente(df, w1, w2, b):
    m = len(df)
    alpha = 0.0000001 
    error = df['consumo_predicho'] - df['Consumo']
    derivada_w1 = (1/m)*(error * df['Peso']).sum()
    derivada_w2 = (1/m)*(error * df['Potencia']).sum()
    derivada_b  = (1/m)*error.sum()
    w1_nuevo = w1 - (alpha * derivada_w1)
    w2_nuevo = w2 - (alpha * derivada_w2)
    b_nuevo = b - (alpha * derivada_b)
    
    return w1_nuevo, w2_nuevo, b_nuevo
ruta_entrada = r"D:\Clase sandre python\CalcularConsumo.csv"
datos = extraer(ruta_entrada)

W1_Peso = 0.01
W2_Potencia = 0.01
B_Sesgo = 0.01
for i in range(10000):
    datos = Prediccion(datos, W1_Peso, W2_Potencia, B_Sesgo)
    costo = perroParado(datos)
    W1_Peso, W2_Potencia, B_Sesgo = GradienteDesendiente(datos, W1_Peso, W2_Potencia, B_Sesgo)
    if i % 1000 == 0:
        print(f'Iteración {i}: Costo = {costo:.4f}')
print(f'Pesos finales: W1={W1_Peso:.2f}, W2={W2_Potencia:.2f}, B={B_Sesgo:.2f}')
print(f'Costo final: {perroParado(datos):.4f}')
print("Tabla final de predicciones:")
print(datos[['Peso', 'Potencia', 'Consumo', 'consumo_predicho']])