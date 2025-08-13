import pandas as pd

# Cargar el archivo CSV
ruta = 'data/TelecomX_Data_tratado.csv'
df = pd.read_csv(ruta)

# Mostrar las primeras filas y las columnas
print('Columnas originales:')
print(df.columns)

# Eliminar columnas irrelevantes (por ejemplo, identificadores únicos)
# Reemplaza 'customerID' por el nombre real de la columna identificadora si es diferente
columnas_a_eliminar = ['customerID']  # Modifica según corresponda

# Eliminar las columnas
for col in columnas_a_eliminar:
    if col in df.columns:
        df = df.drop(col, axis=1)

print('Columnas después de eliminar irrelevantes:')
print(df.columns)

# Guardar el nuevo archivo limpio
df.to_csv('data/TelecomX_Data_limpio.csv', index=False)
print('Archivo limpio guardado como TelecomX_Data_limpio.csv')
