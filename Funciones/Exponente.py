mensaje_bienvenida = '''Hola, bienvenido a la calculadora
    1. Para sumar dos números
    2. Para restar dos números
    3. Para múltiplicar dos números
    4. Para dividir dos números
    5. Para calcular un exponente
    Ingrese su opción: '''

mensaje_numeroA = "Ingrese el número A: "
mensaje_numeroB = "Ingrese el número B: "
def linedesing (cantidad):
    print ("#"*cantidad)
    return None
linedesing(30)

def linedesing2 (cantidad=10, patrón= "#"):
    print (patrón*cantidad)
    return None
linedesing2(30,"$")

numeroA = float (input(mensaje_numeroA))
numeroB = float (input(mensaje_numeroB))

def Sumar (numeroA = 0, numeroB=0):
    suma = numeroA + numeroB 
    return suma
linedesing2 (10,"♥")
resultado = Sumar ()
print (Sumar(numeroA, numeroB))

print ("Vamos a calcular un exponente")

numeroA = int (input(mensaje_numeroA))
numeroB = int (input(mensaje_numeroB))

def funcion (base = 1, exponente=1):
    exponente = base**exponente
    return exponente
linedesing2 (10,"♥")
resultado = funcion ()
print (funcion (numeroA,numeroB))


