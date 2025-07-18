
#calcular la edad

# num =2023;
# año_nacimeinto =1983;

# edad = num -año_nacimeinto
# print(f'Tu edad es: {edad}')


#Calcular el pago que se le da a obrero

# pago_por_hora = int(input("Ingrese el pago por horas"))
# horas_trabajadas =int(input("Ingrese las horas trabajadas"))

# total_pago =pago_por_hora *horas_trabajadas
# print(f'Su pago es {total_pago}')

#Lista_de_claves

# claves_usuario =["Admin1", "Admind2", "Admin3"]
# contador=0;
# contador2=0;

# for n in claves_usuario:
#     ingreso_clave =input("Ingrese la clave: ")
#     if ingreso_clave in n:
#         contador +=1
#         print("No se encuentra la clave")
#         print(f'Errores{contador}')
#     else:
#         contador2 +=1
#         print(f'Aciertos{contador2}')
#         print("puedes pasar")



contraseña ="CICOELMEJOR"
intentos =0;

while True:
    ingreso_contraseña =input("Ingrse su contraseña: ");
    if contraseña == ingreso_contraseña:
        intentos+=1;
        print("Bienvenido a Banistmo")
        break
    else :
        print("contraseña incorrecta")
        intentos +=1
        if intentos>=3:
            print("Su cuenta está bloqueda ")
            break



