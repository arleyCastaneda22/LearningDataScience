# class Personas:
#     def __init__(self, nombre, edad, peso):
#         self.nombre = nombre
#         self.edad = edad
#         self.peso =peso

#     def cumplir_años(self):
#         self.edad +=2
#         print(f"feliz cumpleaños {self.edad}")

#     def calcular_imc(self, altura):
#         altura_metros =altura*100
#         imc = self.peso/(altura_metros**2)
#         return f"El imc es el {imc}"
    
# class Empleado(Personas):

#     def horas_trabajadas_por_mes(self, horas):

#         return f"Estás trabajando {horas}"

# pedro =Personas(nombre ="Juana",edad= 25, peso=47)

# print(pedro.nombre, pedro.edad, pedro.peso)
# pedro.cumplir_años()
# print(pedro.calcular_imc(147))


def calcular_promedio_de_una_lista(lista):

    return sum(lista) /len(lista)

try:
    promedio = calcular_promedio_de_una_lista(lista=[])
    print(promedio)

except Exception as e:
    print("Hubo un error")
    print(e)


