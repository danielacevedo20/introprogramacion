isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        edad = int (input("Ingrese su edad: "))
        isCorrectInfo = True
    except ValueError:
        print("Ingresaste un dato erroneo")


nombreArchivo = input("Ingrese el nombre del archivo que desdea encontrar: ")
try:
    archivo = open (nombreArchivo)
except FileNotFoundError:
    print (f"El archiivo {nombreArchivo} no se ha encontrado")


base= 4
divisor = 0
try:
    dividir = base/divisor
except ZeroDivisionError:
    print ("El divisor ingresado es 0, por lo tanto la solución no se encuentra dentro de los reales")

isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        nombre = input("Ingrese su nombre: ")
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print("Ingresaste un dato erroneo")
    except ValueError:
        print("Las edades son números enteros")

lista= [2,43,54,32]
try:
    lista [5]
except IndexError:
    print("El indice es mayor al tamaño de la lista")

