preguntaNumero = '''Ingrese algunas de estas opciones
        1. Hacer conversión de pesos o dolares
        2. Agrege un valor a la lista de pesos
        3. Mostrar el valor más alto, el más bajo y el promedio
        4. Eliminar elemento de la lista
        5. Salir
'''


listaPesos = [20000,30000,4000,2500,1000,7600]
OpcionEscogida = int(input(preguntaNumero))
while (OpcionEscogida!=5):
    if (OpcionEscogida ==1):
        print ("Escogiste 1")
    elif(OpcionEscogida ==2):
        print("Escogiste 2")
    elif (OpcionEscogida ==3):
        print ("Escogiste 3")
    elif (OpcionEscogida ==4):
        print ("Escogiste 4")
    else:
        print ("Respuesta no valida")
    OpcionEscogida = int(input(preguntaNumero))           