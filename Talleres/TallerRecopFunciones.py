def MostrarLista (lista):
    for elemento in lista:
        print (elemento)
listaEnteros = [11,23,14,45,21,2,5]
MostrarLista (listaEnteros)

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
CalculoLista (listaEnteros)

def Saludar (veces = 0):
    print ("¡Hola!"*veces)
Saludar (4)

def ListaPares (lista):
    Pares = []
    for elemento in lista:
        if elemento % 2 ==0:
            Pares.append (elemento)
    print (f" Los números pares en la lista son {Pares}")
ListaPares (listaEnteros)

def NumerosMayores24 (lista):
    listaMayores= []
    for elemento in lista:
        if elemento > 24:
            listaMayores.append(elemento)
    print (f"Los números mayores a 24 en la lista son {listaMayores}")
NumerosMayores24 (listaEnteros)

def CalcularIMC (altura, peso):
    return peso/(altura**2)
imc = round(CalcularIMC (1.83,75),2)
print (imc)

def Despedida ():
    print ("Hasta pronto programador, ¡Hora de salir a la MATRIX!")
Despedida ()