nombres = []
print (type(nombres))
print (nombres)
nombres = ["Santi","Aleja","Elsa"]
print (nombres)
print (nombres[1])
nombres.append ("Mauricio")
print (nombres)

edades = [18,19,20,17]
estaturas = [1.62,1.80,1.67,1.98]
#Mostrar el último valor de la lista
print (edades[-1])
print (edades[0:2])
print (edades[:3])
print (edades[2:])
print (edades[:])
edades.sort()
print (edades)
edades.sort(reverse=True)
print(edades)
#Mayor
mayor = max (edades)
print(mayor)
#Menor
menor = min (edades)
print (menor)
#Como contamos cuntos elementos hay
largolista= len(edades)
print (largolista)
#Como sumamos
sumaEdades= sum(edades)
#Calcular el promedio
Promedio = sumaEdades/largolista
print (Promedio)
#Eliminar un elemento
edades.pop (2)
print(edades)

##Ciclos for y las listas
largolista= len(edades)
for indice in range (largolista):
    print (edades[indice])

LargoListaNombre = len(nombres)
for indice in range (LargoListaNombre):
    print (nombres[indice])

posicionesConValoresPares=[]
largolista= len(edades)
for posicion in range(largolista):
    if (edades[posicion]%2 == 0):
        posicionesConValoresPares.append (posicion)

print (edades)
print (posicionesConValoresPares)
#solo cuando les interese mostrar la lista
for edad in edades:
    print(edad)


posicion=0
posicionesPares = []
for edad in edades:
    if (edad%2==0):
        posicionesPares.append(posicion)