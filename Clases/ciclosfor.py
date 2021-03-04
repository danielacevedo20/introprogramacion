# for iteracion in range (10):
#     print (iteracion)
# print ("#"*60)
# for iteracion in range (10):
#     print (iteracion+1)
# print ("#"*60)
# for iteracion in range (1,11):
#     print(iteracion)
# print ("#"*60)
# for iteracion in range (1,11,2):
#     print (iteracion)
# print ("#"*60)



# residuo = 5%4
# print (residuo)
# residuo = 4%4
# print (residuo)
# print ("#"*60)
# for iteracion in range (1,11):
#     if (iteracion % 2 == 0):
#         print (iteracion)
# print ("#"*60)
# for iteracion in range (1,11):
#     if(iteracion % 2 == 0):
#         print (iteracion, "--> Es un número par")
#     else:
#         print (iteracion, "-->Es un número impar")



rango = int(input("Ingrese el rango máximo: "))

opcion = int(input('''
     1- Ver solo impares
     2- Ver solo pares
     3- ver ambos
     n- no mostrar nada}
'''))
if (opcion==1):
    for iteracion in range (1,rango+1):
        if (iteracion % 2 != 0):
            print (iteracion)
elif (opcion == 2):
    for iteracion in range (1,11):
        if(iteracion % 2 == 0):
            print (iteracion)
elif (opcion ==3):
    for iteracion in range (1,11):
        if(iteracion % 2 == 0):
            print (iteracion, "--> Es un número par")
    else:
            print (iteracion, "-->Es un número impar")
else:
    print ("MOSTRAR NADA")