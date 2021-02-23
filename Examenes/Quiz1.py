#-----Constantes-----#
MENSAJE_BIENVENIDA = "Buenos días, hoy vamos a saber si tus niveles de triglicéridos y homecisteína están en los valores adecuades"
MENSAJE_PREGUNTA_TRIGLICERIDOS = "Ingrese la concentración de triglicéridos en mg/dL: "
MENSJAE_OPTIMOTRIGLI = "Tu concentración de triglicerios es la optima!"
MENSAJE_LIMITETRIGLI = "Tu concentración de trigliceridos está al límite ¡PILAS!"
MENSAJE_ALTOTRIGLI = "Tu concentración de triglicéridos tiene un valor alto, acude a un especialista"
MENSAJE_MUYALTOTRIGLI = "Tu concentración de triglicéridos está MUY alta, ¡acude a un especialista lo más pronto posible!"
MENSAJE_PREGUNTA_HOMOC = "Ahora ingrese su concentración de homocisteína en micromoles/L: "
MENSJAE_OPTIMOHOMOC = "Tu concentración de homocisteína es la optima!"
MENSAJE_LIMITEHOMOC = "Tu concentración de homocisteína  está al límite ¡PILAS!"
MENSAJE_ALTOHOMOC = "Tu concentración de homocisteína  tiene un valor alto, acude a un especialista"
MENSAJE_MUYALTOHOMOC = "Tu concentración de homocisteína  está MUY alta, ¡acude a un especialista lo más pronto posible!"
MENSAJE_ERROR_HOMO = "Valor no aceptable, ingrese una concentracion mayor o igual a 2 micromoles/L"
MENSAJE_DESPEDIDA = "Muchas gracias por participar ¡Mantente saludable!"

#-----Entras de código------#
#Triglicéridos#
print (MENSAJE_BIENVENIDA)
trigliceridos = float (input(MENSAJE_PREGUNTA_TRIGLICERIDOS))
optimotrigli = trigliceridos < 150
limitetrigli = trigliceridos >= 150 and trigliceridos < 200
altotrigli = trigliceridos > 199 and trigliceridos <= 500
resultado = ""
if (optimotrigli):
    resultado = MENSJAE_OPTIMOTRIGLI
elif (limitetrigli):
    resultado = MENSAJE_LIMITETRIGLI
elif (altotrigli):
    resultado = MENSAJE_ALTOTRIGLI
else:
    resultado = MENSAJE_MUYALTOTRIGLI
print (resultado)
#Homocisteína#
homoc = float (input(MENSAJE_PREGUNTA_HOMOC))
datoerrorhomoc = homoc < 2
optimohomoc = homoc >= 2 and homoc <= 15
limitehomoc = homoc > 15 and homoc <= 30
altohomoc = homoc > 30 and homoc <= 100
resultado = ""
if (optimohomoc):
    resultado = MENSJAE_OPTIMOHOMOC
elif (limitehomoc):
    resultado = MENSAJE_LIMITEHOMOC
elif (altohomoc):
    resultado = MENSAJE_ALTOHOMOC
elif (datoerrorhomoc):
    resultado = MENSAJE_ERROR_HOMO
else:
    resultado = MENSAJE_MUYALTOHOMOC
print (resultado)
print (MENSAJE_DESPEDIDA)