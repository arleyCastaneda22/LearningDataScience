import re


def contar(texto):
    contador = 0
    contadorJ = 0
    texto2 = texto.upper()
    
    for x in texto2:
        if x == "R":
            contador += 1

        elif x == "J":
            contadorJ += 1
     
    
    return contador, contadorJ  # Retorna los valores

resultado = contar("RRJf")
print(f'Resultado final: R={resultado[0]}, J={resultado[1]}')



    



