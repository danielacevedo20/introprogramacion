#Variables
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
mensaje_menu1 = '''Responda de acuerdo a lo que desee
            1. Para convertir la temperatura
            2. Para saber la categoría de la temperatura
            3. Ver el máximo, el mínimo y cada cuanto se tomó la temperatura
            4. Para salir del menú
            Ingrese una opción: '''

mensaje_conversion = '''Responda de acuerdo a lo que desee
            F.  Para convertir a Fahrenheit
            K.  Para convertir a Kelvin
            Ingrese una respuesta: '''

mensaje_invalido = "Respuesta invalida, ingrese una nuevamente"
mensajeOpcion = "Escogiste {} en el menú"
listaClasificacion =[]
listaFahrenheit = []
listaKelvin = []
menu = ""
####Código
print ('''¡Hola ingeniero biomédico!
Estas fueron las temperaturas tomadas
durante 24 horas a un neonato(°C)
usalas sabiamente''', Temperatura_Corporal)
print ("#"*70)
#Convertir a Fahrenheit
for elemento in Temperatura_Corporal:
    fahrenheit = (elemento*9/5)+32
    fahrenheit = round(fahrenheit,2)
    listaFahrenheit.append (fahrenheit)
#Convertir a Kelvin
for elemento in Temperatura_Corporal:
    kelvin = elemento + 273.15
    kelvin = round(kelvin,2)
    listaKelvin.append (kelvin)
#Clasificación
for elemento in Temperatura_Corporal:
    clasificacion = ""
    if (elemento<36):
        clasificacion = "Hipotermia"
    elif (elemento >=36 and elemento <37.6):
        clasificacion = "Temperatura normal"
    else:
        clasificacion = "Fiebre"
    listaClasificacion.append (clasificacion)
####Máximo, mínimo y cada cuanto se tomó la temperatura
mayor = max(Temperatura_Corporal)
menor = min (Temperatura_Corporal)
muestreo = 24/len(Temperatura_Corporal)
muestreo = round(muestreo,2)
###Menú
menu = int(input(mensaje_menu1))
while (menu !=4):
    if (menu ==1):
        print (mensajeOpcion.format(1))
        conversion = input (mensaje_conversion)
        if (conversion == "F"):
            print (listaFahrenheit)
        elif (conversion == "K"):
            print (listaKelvin)
        else:
            print (mensaje_invalido)
    elif (menu ==2):
        print (mensajeOpcion.format(2))
        print (listaClasificacion)
    elif (menu ==3):
        print (mensajeOpcion.format(3))
        print ("La temperatura mayor tomada al neonato fue", mayor)
        print ("La temperatura menor tomada al neonato fue", menor)
        print ('''Se realizó una estimación de cada cuanto se
tomaron las muestras al neonato y
dicha estimación es que por cada''', muestreo,"Hrs, se tomó una muestra")
    else:
        print (mensaje_invalido)
    menu = int(input(mensaje_menu1))
print ("Muchas gracias por usar el menú, ¡Suerte ingeniero!")