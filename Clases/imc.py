#------Constantes-----#
PREGUNTA_ESTATURA = "Cuál es tu estatura en mt?: "
PREGUNTA_PESO = "Cuánto pesas en Kg?: "
MENSAJE_BIENVENIDA = "Hola, Voy a calcular tu IMC"
MENSAJE_IMC = "Tu IMC es..."
MENSAJE_DESPEDIDA = "El resultado de la prueba de obesidad es..."

#-----Entrada código------#
print (MENSAJE_BIENVENIDA)
estatura = float(input(PREGUNTA_ESTATURA))
peso = float(input(PREGUNTA_PESO))
imc = peso/(estatura**2)
print(MENSAJE_IMC,imc)
isObeso = imc >= 30
print (MENSAJE_DESPEDIDA,isObeso)