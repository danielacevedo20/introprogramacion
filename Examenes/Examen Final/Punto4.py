import sys
nombreArchivo = "Pacientes.txt"
encabezado = '''Documento referente a los datos del paciente, 
una breve descripción y el precio de su consulta'''

isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        nombre = input("Ingrese el nombre del paciente: ")
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print("Ingresaste un dato erroneo")

descripcion = input("Ingrese una descripción de la patología del paciente: ")

isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        precio = float(input("Ingrese el precio de la consulta: "))
        isCorrectInfo = True
    except ValueError:
        print("Ingresaste un dato erroneo")


try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, "w", encoding="UTF-8")
    archivo.writelines(encabezado)
    sys.exit

archivo = open(nombreArchivo, "a")
linea = "\nNombre: "+ nombre + " Descripción: "+ str(descripcion) + " Precio: "+ str(precio)
archivo.writelines(linea)
archivo.close