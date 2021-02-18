#------Constantes-----#
PREGUNTA_ESTATURA = "Cuál es tu estatura en mt?: "
PREGUNTA_PESO = "Cuánto pesas en Kg?: "
MENSAJE_BIENVENIDA = "Hola, Voy a calcular tu IMC"
MENSAJE_IMC = "Tu IMC es..."
MENSAJE_DESPEDIDA = "El resultado de la prueba de obesidad es..."
MENSAJE_BAJO_PESO = "Estás delgado"
MENSAJE_ADECUADO = "Estás bien"
MENSAJE_SOBREPESO = "Estás rellenito de amor"
MENSAJE_OBESO = "Eres MUYYY rellenito de amor"

#-----Entrada código------#
print (MENSAJE_BIENVENIDA)
estatura = float(input(PREGUNTA_ESTATURA))
peso = float(input(PREGUNTA_PESO))
imc = peso/(estatura**2)
isBajoPeso = imc < 18.5
isAdecuado = imc >= 18.5 and imc < 25
isSobrepeso = imc >= 25 and imc < 30
resultado = ""
if(isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isAdecuado):
    resultado = MENSAJE_ADECUADO
elif (isSobrepeso):
    resultado = MENSAJE_SOBREPESO
else:
    resultado = MENSAJE_OBESO
print (MENSAJE_DESPEDIDA,imc)
print (resultado)