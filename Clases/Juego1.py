#Entradas#
MENSAJE_BIENVENIDA = "Vamos a jugar :D"
PREGUNTA_NUMERO ='''
        En este juego debes acertar un número
        que va desde el 1 hasta al 10, la idea es que
        lo puedes intenrar las veces que quieras
        ¡Éxitos!, ingresa tu número: 
'''
PREGUNTA_FALLIDA = "Aahhh! Fallaste ;c, ingresa otro número: "
MENSAJE_GANAR = "Felicidades, has ganado!!"
MENSAJE_PERDER = "Perdiste, vuelva a intentarlo"

#Entradas de código#
numerooculto = 7
vidas = 3
print (MENSAJE_BIENVENIDA)
numeroingresado= int(input(PREGUNTA_NUMERO))
if (numeroingresado != numerooculto):
    vidas = vidas - 1
while (numerooculto != numeroingresado and vidas > 0):
    numeroingresado =int (input(PREGUNTA_FALLIDA))
    vidas = vidas - 1

if (vidas > 0):
    print (MENSAJE_GANAR)
    print (f"Te quedaron {vidas} vidas")
else:
    print (MENSAJE_PERDER, ",el número era el",numerooculto)