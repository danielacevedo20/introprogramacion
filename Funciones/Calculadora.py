def linedesing (cantidad):
    print ("#"*cantidad)
    return None
linedesing(30)

def linedesing2 (cantidad=10, patrón= "#"):
    print (patrón*cantidad)
    return None
linedesing2(30,"$")

#-----Mostrar lista-----#
def mostrarLista (listaEntrada):
    for elemento in listaEntrada:
        print (elemento)
    return None
lista = [231,32,34,234,2324,24234,34]
lista2 = [3454,56,46,46,45,45,45,34,54]
linedesing2 (30,"♦")
mostrarLista(lista)
linedesing2 (30,"♦")
mostrarLista(lista2)
lista3 = [23.2,23.4323,43.34345,233.2132]
#----Sumar dos números-----#
def Sumar (a = 0, b=0):
    suma = a + b 
    return suma
linedesing2 (10,"♥")
resultado = Sumar ()
print (Sumar(12,14))