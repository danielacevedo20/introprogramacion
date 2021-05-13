from typing import OrderedDict, get_origin


texto = "Hola espero que todo esté muy bien"
lista = [1,32,21,34,54]
lista.sort ()
for elemento in lista:
    print(elemento)
for i in range (len(lista)):
    print(lista[i])

for letra in texto:
    print(letra)

palabras = texto.split(" ")
print(type(palabras))
eliminarE = texto.split("e")
print(eliminarE)

uniendo = "i".join(eliminarE)
print(uniendo)

listaNombres = ["Laura","Juan","Mario","Elsa","Katherine","daniel"]
print(max(listaNombres, key=len))

respuesta = input("Ingrese Si o No: ")
if respuesta.upper()== "SI":
    print ("Bienvenido al código")
else:
    print("Chao")

nombre = input("Ingrese su nombre: ")
print(nombre.capitalize())

correo = "ESPERO QUE ESTÉS BIEN"
print(correo.casefold().capitalize())
saludo = "Hola ¿cómo estás?"
nombre = "Maria Alejandra"
print(saludo.center(50))

enunciado = "Hola hola hola hola"
print(enunciado.upper().count("Hola" and "hola"))

print(enunciado.find("decir"))
print(enunciado[25:30])


txt = "Me gusta programar en java"
print (txt.replace("java","python"))

numeroID = "123214"
print(numeroID.isnumeric())

parrafo = "hola buenas tardes."
print(parrafo.endswith("."))
