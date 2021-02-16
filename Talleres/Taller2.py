#------Constantes-----#
MENSAJE_BIENVENIDA = "Bienvenido, hoy vamos a realizar algunas operaciones"
MENSAJE_NUMEROA = "Ingrese un número: "
MENSAJE_NUMEROB = "Ingrese un segundo número: "
MENSAJE_SUMA ="Vamos a sumarlos"
MENSAJE_RESULTADOSUMA = "El resultado de la suma es..."
MENSAJE_RESTA = "Vamos a restarlos"
MENSAJE_RESULTADORESTA = "El resultado de la resta es..."
MENSAJE_MULTIPLICACION = "Vamos a multiplicarlos"
MENSAJE_RESULTADOMULTIPLICACION = "El resultado de la multiplicación es..."
MENSAJE_DIVISION = "Vamos a dividirlos"
MENSAJE_RESULTADODIVISION = "El resultado de la division es..."
MENSAJE_EXPONENCIAL = "Vamos a elevar el primer número, las veces del segundo"
MENSAJE_RESULTADOEXPONENCIAL = "El resultado de elevarlos es..."
MENSAJE_IGUALES = "Calcularé si son el mismo número"
MENSAJE_RESULTADOIGUALES = "El resultado de si son el mismo número es..."
MENSAJE_DESPEDIDA = "Muchas gracias por participar!!!"

#-----Entrada código-----#
print (MENSAJE_BIENVENIDA)
numeroA = float(input(MENSAJE_NUMEROA))
numeroB = float(input(MENSAJE_NUMEROB))
print (MENSAJE_SUMA)
sumar = numeroA + numeroB
print (MENSAJE_RESULTADOSUMA, sumar)
print ("#"*40)
print (MENSAJE_RESTA)
restar = numeroA - numeroB
print (MENSAJE_RESULTADORESTA, restar)
print ("#"*40)
print (MENSAJE_MULTIPLICACION)
multiplicar = numeroA*numeroB
print(MENSAJE_RESULTADOMULTIPLICACION,multiplicar)
print ("#"*40)
print (MENSAJE_DIVISION)
dividir = numeroA/numeroB
print(MENSAJE_RESULTADODIVISION,dividir)
print ("#"*40)
print (MENSAJE_EXPONENCIAL)
elevar = numeroA**numeroB
print (MENSAJE_RESULTADOEXPONENCIAL,elevar)
print ("#"*40)
print (MENSAJE_IGUALES)
isIGUALES = dividir == 1
print (MENSAJE_RESULTADOIGUALES, isIGUALES)
print (MENSAJE_DESPEDIDA)