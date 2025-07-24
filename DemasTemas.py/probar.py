from consumo_Api import obtener as o
import pandas as pd
# url2 = "https://rickandmortyapi.com/api/character"
# resultado = o(url2)


diccionario ={"Nombre": "Julian", "Edad": 25}
print(diccionario.values())
print(diccionario.keys())
lista =[1,2,3,8,5,126,8,13,24]
print(lista)
lista2=[]

for n in lista:
    if n %2==0:
        lista2.append(n)
    else:
        print("No pasas de esta esuina")

print(lista2)
print(lista2.pop())
lista2.reverse()
print(lista2)

# df =pd.DataFrame(diccionario)

# print(df)



