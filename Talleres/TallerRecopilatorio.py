#Variables
listaDolares = [20000,30000,4000,2500,1000,7600]

mensaje_menu1 = '''¡Hola! hoy te mostraremos tus últimos ingresos
            1. Para convertir dolares
            2. Para saber la categoría de sus ingresos
            3. Ver el máximo, el mínimo y el promedio de ingresos
            4. Para salir del menú
            Ingrese una opción: '''
mensaje_conversion = ''' ¡Hola! Responda de acuerdo a lo que desee
            C.  Para mostrar la lista en pesos colombianos
            D. Para mostrar la lista en dolares
            E. Para mostrar la lista en euros
Ingrese: '''
mensaje_invalido = "Respuesta invalida, ingrese una nuevamente"
listaClasificacion = []
listaPesos = []
listaEuros = []
menu = ""
#Código
#Conversión a pesos
for elemento in listaDolares:
    pesos = elemento *3700
    listaPesos.append (pesos)
#Conversión euros
for elemento in listaDolares:
    euros = elemento * 0.84
    listaEuros.append (euros)
#Clasificación
for elemento in listaDolares:
    clasificacion = ""
    if (elemento < 1000):
        clasificacion = "Ingresos bajos"
    elif (elemento >=1000 and elemento < 7000):
        clasificacion = "Ingresos medios"
    elif (elemento >= 7000 and elemento <20000):
        clasificacion = "Ingresos altos"
    else:
        clasificacion = "Ingresos elevados"
    listaClasificacion.append (clasificacion)
#Máximo, mínimo y promedio
mayor = max (listaDolares)
menor = min (listaDolares)
suma = 0
for elemento in listaDolares:
    suma = elemento + suma
promedio = suma/len (listaDolares)
print (promedio)
#Menu
menu = int(input(mensaje_menu1))
while (menu !=4 ):
    if (menu ==1):
        conversion = input (mensaje_conversion)
        if (conversion == "C"):
            print (listaPesos)
        elif (conversion == "D"):
            print(listaDolares)
        elif (conversion == "E"):
            print (listaEuros)
        else:
            print (mensaje_invalido)
    elif (menu ==2):
        print (listaClasificacion)
    elif (menu ==3):
        print ("El ingreso mayor fue: ", mayor)
        print ("El ingreso menor fue: ", menor)
        print ("El promedio de ingresos fue: ", promedio)
    else:
        print (mensaje_invalido)
    menu = int(input (mensaje_menu1))
print ("muchas gracias por usar el menú")