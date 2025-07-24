filename ="C:/Users/arley/OneDrive/Documentos/AprendiendoApiPython/El mejor.txt"

numeros =[1,2,3,4,5,6,7,8,9,10]

with open(filename , 'w') as file:
    for numero in numeros:
        file.write(f' {str(numero)}\n') 


with open(filename,"r") as file:
    line = file.readline()
    for line in file:
        print(line)

