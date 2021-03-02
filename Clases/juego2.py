#Entradas#
MENSAJE_BIENVENIDA = "Vamos a jugar :D"
PREGUNTA_NUMERO ='''
        En este juego debes acertar un número
        que va desde el 1 hasta al 10, intente
        hasta acabar sus vidas
        ¡Éxitos!, ingresa tu número: 
'''
PREGUNTA_DIFICULTAD = '''
    1-Fácil
    2-Moderado
    3-Difícil
'''
PREGUNTA_FALLIDA = "Aahhh! Fallaste ;c, ingresa otro número: "
MENSAJE_GANAR = "Felicidades, has ganado!!"
MENSAJE_PERDER = "Perdiste, vuelva a intentarlo"
import random
#Entradas de código#
numerooculto = random.randint (1,10)
vidas = None
print (MENSAJE_BIENVENIDA)
dificultad =int (input(PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad !=2 and dificultad !=3):
    print ("Ingrese una opción valida")
    dificultad =int (input(PREGUNTA_DIFICULTAD))
if (dificultad==1):
    vidas = 5
elif (dificultad==2):
    vidas = 3
else:
    vidas=1
print (f"Tienes {vidas} vidas")
numeroingresado= int(input(PREGUNTA_NUMERO))
if (numeroingresado != numerooculto):
    vidas = vidas - 1
while (numerooculto != numeroingresado and vidas > 0):
    numeroingresado =int (input(PREGUNTA_FALLIDA))
    vidas = vidas - 1

if (vidas >= 0 and numeroingresado==numeroingresado):
    print (MENSAJE_GANAR)
    print (f"Te quedaron {vidas} vidas")
else:
    print (MENSAJE_PERDER, "el número era el",numerooculto)