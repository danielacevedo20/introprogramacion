import sys
from pandas.core.series import Series

nombre = input("Ingrese el nombre del producto: ")
descripcion = input("Ingrese una descripción del producto: ")
precio = float(input("Ingrese el precio del producto: "))
nombreArchivo = "Mantenimiento.txt"
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, "w", encoding="UTF-8")
    encabezado = "Manejo de Clientes"
    archivo.writelines(encabezado)
    sys.exit

archivo = open(nombreArchivo, "a")
linea = "\nNombre: "+ nombre + " Descripción: "+ str(descripcion) + " Precio: "+ str(precio)
archivo.writelines(linea)
archivo.close

