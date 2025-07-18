ruta="C:/Users/2909287/Pictures/Evidencia eventos/Julio 2025/mi_imagen.png"

with open(ruta, "rb")as f:
    imagen = f.read()
    print(len(imagen))



nuevo_contenido = "Este es el nuevo contenido del archivo. Todo lo anterior ha sido reemplazado"
with open("Hola.txt", "w", encoding="utf-8") as j:
    contenido =j.write(nuevo_contenido)




