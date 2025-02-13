import pandas as pd

# Crear un DataFrame

personas = {"nombre": ["Juan", "Ana", "Luis", "Pedro"],"edad": [25, 30, 35, 40]}

df=pd.DataFrame(personas)
y = df[['nombre']]
print(y)
print(df[df['edad'] > 30])
