
import requests as app
import pandas as pd

def obtener(url):
    r = app.get(url)
    if r.status_code==200:
        datos = r.json()
        datos=datos["results"]
        df =pd.DataFrame(datos)
        return df
    else:
        return "Hubo un error"
url1 ="https://rickandmortyapi.com/api/character"

resultado =obtener(url1);
mayores =resultado["id"]<10 
print(mayores)

for i in mayores:
    print(i)




