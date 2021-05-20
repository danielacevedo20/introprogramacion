import sys

from pandas.core.series import Series
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura: "))


nombreArchivo = "estudiantes.txt"
try:
    archivo = open(nombreArchivo)
    print(1)
except FileNotFoundError:
    archivo = open(nombreArchivo, "w", encoding="UTF-8")
    print(2)
    descripcion = "Archivos de datos de estudiantes"
    archivo.writelines(descripcion)
    sys.exit(1)
archivo = open(nombreArchivo,"a")

linea = "\nNombre: "+ nombre + " Edad: "+ str(edad) + " Estatura: "+ str(estatura)
archivo.writelines(linea)
archivo.close

with open(nombreArchivo) as reader:
    for line in reader:
        print(line)

import pandas as pd
diccionario = {}
diccionario["nombre"] = "Daniel"
diccionario["edad"] = 18
diccionario["estatura"] = 1.84
serie = pd.Series(diccionario)
print(serie)
serie.to_csv("datos.csv",sep=";")