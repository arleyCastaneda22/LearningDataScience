import pandas as pd 

personas = {"jesus": ["Juan", "Ana", "Luis", "Pedro"],"rodolfo": [25, 30, 35, 40]}

df=pd.DataFrame(personas)
print(df.head())
heders=['nombre','edad']
df.columns = heders
print(df.head())
