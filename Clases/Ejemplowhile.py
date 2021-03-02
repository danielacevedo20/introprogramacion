#---Entradas---#
MENSAJE_BIENVENIDA= "Buenos días"
PREGUNTA_MENU = ''' Ingrese
    1. Para mostrar los números del 1 al 5
    2. Para preguntar tu nombre
    3. Para mostrar el año en el que estamos
    4. Salir
'''
PREGUNTA_NOMBRE = "Ingrese su nombre: "
MENSAJE_ERROR = "Número invalido, ingrese un número nuevamente"
entrada = 1
print (MENSAJE_BIENVENIDA)
while (entrada >=1 and entrada <=3):
    entrada= int(input(PREGUNTA_MENU))
    if (entrada==1):
        print (1,2,3,4,5)
    elif (entrada ==2):
        nombre = input (PREGUNTA_NOMBRE)
        print (f'Bienvenido {nombre} a este men')
    elif (entrada==3):
        print ("Estamos en el año 2021")
    elif (entrada ==4):
        print ('Muchas gracias por usar el programa ¡Feliz día!')
    else:
        entrada = 1
        print  (MENSAJE_ERROR)