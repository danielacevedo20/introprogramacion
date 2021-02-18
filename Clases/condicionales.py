#-----Constantes-----#
MENSAJE_BIENVENIDA = "Hola, espero que estés bien"
PREGUNTA_A = "Ingrese un número A: "
PREGUNTA_B = "Ingrese un número B: "
MENSAJE_MAYOR = "El número A es mayor"
MENSAJE_MENOR = "El número A es menor"
MENSAJE_IGUAL = "Los números son iguales"

#-----Entrada de código-----#
print (MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_A))
numeroB = int (input (PREGUNTA_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB

if (isMayor):
    print(MENSAJE_MAYOR)
elif (isMenor):
    print (MENSAJE_MENOR)
else: print (MENSAJE_IGUAL)