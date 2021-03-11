listaPesos = [20000,30000,4000,2500,1000,7600]

preguntaMoneda = '''
    C. Mostrar el valor en pesos colombianos
    D. Mostrar en dolares
    E = Mostrar en Euro
'''
listaEuros =[]
for elemento in listaPesos:
    Conversor =round (elemento*0.00023,2)
    listaEuros.append (Conversor)
listaDolares =[]
for elemento in listaPesos:
    Conversor = round (elemento*0.00028,2)
    listaDolares.append (Conversor)


opcionMoneda = input(preguntaMoneda)
if (opcionMoneda=="C"):
    print ("Mostrando lista original (Pesos colombianos)")
    print(listaPesos)
elif (opcionMoneda=="D"):
    print("Mostrar lista en dolares")
    print(listaDolares)
elif (opcionMoneda=="E"):
    print("Mostrar lista en Euros")
    print(listaEuros)
else:
    print("Valor ingresado no valido")