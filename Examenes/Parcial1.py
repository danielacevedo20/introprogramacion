def calculadora (numero1,numero2,numero3):
    suma = numero1+numero2+numero3
    resta = numero1-numero2-numero3
    multiplicacion = numero1*numero2*numero3
    division = numero1/numero2/numero3
    exponente = numero1**numero2**numero3
    return (f'''    la suma es {suma}
    la resta es {resta}
    la multiplicación es {multiplicacion}
    la division es {division}
    la función exponente es {exponente}''')

numeros = calculadora(2,3,2)
print (numeros)

def MostrarLista (listaA,listaB,listaC):
    if (len(listaA)==len(listaB) and len(listaC)==len (listaC)):
        for elemento in listaA:
            print (elemento)
        for elemento in listaB:
            print (elemento)
        for elemento in listaC:
            print (elemento)
    else:
        print ("Las listas no son del mismo tamaño")
lista1 = [2,3,4]
lista2 = [5,6,7]
lista3 = [8,9,10]
MostrarLista (lista1,lista2,lista3)

def AreaTriangulo (base, altura):
    area = (base*altura)/2
    return (area)
triangulo = AreaTriangulo (10, 2)
print (triangulo)

def CalculoLista (lista):
    mayor = max (lista)
    menor = min (lista)
    sumaLista = 0
    for elemento in lista :
        sumaLista = sumaLista + elemento
    promedio = sumaLista/ len(lista)
    promedio = round(promedio,2)
    print(f'''
    {mayor}--> Es el número mayor
    {menor}--> Es el número menor
    {promedio}--> Es el promedio de la lista
    ''')
listaEnteros = [2,4,3,8]
CalculoLista (listaEnteros)

def Fibonacci (Posicion):
    a = 0
    b = 1
    for elemento in range (Posicion -1):
        c = a + b
        a = b
        b = c
    return (a)

numero = Fibonacci (13)
print (numero)