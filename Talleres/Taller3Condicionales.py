#-----Constantes-----#
MENSAJE_BIENVENIDA = "Hola, espero que estés bien, en primer lugar vamos a comparar 2 números"
PREGUNTA_A = "Ingrese un número A: "
PREGUNTA_B = "Ingrese un número B: "
MENSAJE_MAYOR = "El número A es mayor"
MENSAJE_MENOR = "El número A es menor"
MENSAJE_IGUAL = "Los números son iguales"
MENSAJE_FINAL1 = "2. Vamos a comparar tu edad"
PREGUNTA_EDAD = "Ingrese su edad: "
MENSAJE_EDADMENOR = "Eres menor de edad"
MENSAJE_JOVEN = "Eres joven"
MENSAJE_ADULTO = "Eres adulto"
MENSAJE_ADULTOMAYOR = "Eres adulto mayor"
MENSAJE_FINAL2 = "3. Ahora vamos a comparar un año con el actual"
MENSAJE_AÑO = "Ingrese un año que desee comparar con el actual: "
MENSAJE_AÑOACTUAL = "¿En qué año estás?: "
MENSAJE_FINAL3 = "4. Ahora vamos a convertir una medida en cm a las unidades que desee"
MENSAJE_CENTIMETROS = "Ingrese una longitud (en centimetros): "
PREGUNTA_UNIDAD = ''' ingrese en que unidades desea transformar :
      Km (Kilometros)
      M  (Metros) 
      mm (milimetros)
'''
MENSAJE_DESPEDIDA = "Muchas gracias por usar este programa, que esté muy bien :D"
#-----Entrada de código-----#
#PUNTO NÚMERO 1#
print ("#"*40)
print (MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_A))
numeroB = int (input (PREGUNTA_B))
isIgual = numeroA == numeroB
isMayor = numeroA > numeroB
resultado =""
if (isIgual):
    resultado = MENSAJE_IGUAL
elif (isMayor):
    resultado = MENSAJE_MAYOR
else:
    resultado = MENSAJE_MENOR
print (resultado)
#PUNTO NÚMERO 2#
print ("#"*40)
print (MENSAJE_FINAL1)
edad = int (input(PREGUNTA_EDAD))
isMenorEdad = edad < 18
isJoven = edad >= 18 and edad <= 25
isAdulto = edad >= 26 and edad <= 60
resultado = ""
if (isMenorEdad):
    resultado = MENSAJE_EDADMENOR
elif (isJoven):
    resultado = MENSAJE_JOVEN
elif (isAdulto):
    resultado = MENSAJE_ADULTO
else:
    resultado = MENSAJE_ADULTOMAYOR
print (resultado)
#PUNTO NÚMERO 3#
print ("#"*40)
print (MENSAJE_FINAL2)
añoactual = int (input(MENSAJE_AÑOACTUAL))
año = int (input(MENSAJE_AÑO))
isAñoIgual = año == añoactual
isAñoMayor = año > añoactual
if (isAñoIgual):
    print ("¡Son el mismo año!")
elif (isAñoMayor):
    añomayor = año - añoactual
    print (f"Faltan {añomayor} años para ese año")
else:
    añomenor = añoactual - año
    print (f"Han pasado {añomenor} años desde ese año")
#PUNTO NÚMERO 4#
print ("#"*40)
print (MENSAJE_FINAL3)
Medida = float (input (MENSAJE_CENTIMETROS))
Unidad = input (PREGUNTA_UNIDAD)
kilometros = Medida *10**-5
metros = Medida *10**-2
milimetros = Medida *10
resultado = ""
if (Unidad == "Km"):
    resultado = kilometros
elif (Unidad =="M"):
    resultado = metros
elif (Unidad == "mm"):
    resultado = milimetros
else:
    resultado = "Unidad invalida, ingrese Km, M o mm"
print (resultado)
print (MENSAJE_DESPEDIDA)