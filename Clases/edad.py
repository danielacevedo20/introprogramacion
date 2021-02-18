#-----Entradas-----#
#-----Constantes-----#
MENSAJE_BIENVENIDA = "Bienvenido al PC"
PREGUNTA_EDAD = "Cuántos años tienes?: "
MENSAJE_MAYOR_EDAD ="Eres mayor de edad, puedes seguir"
MENSAJE_MENOR_EDAD = "Eres menor de edad, no puedes seguir"

#-----Entradas de código-----#
print (MENSAJE_BIENVENIDA)
edad = int(input(PREGUNTA_EDAD))
isMayor = edad >= 18
resultado = ""
if (isMayor):
    resultado = MENSAJE_MAYOR_EDAD
else:
    resultado = MENSAJE_MENOR_EDAD
print (resultado)