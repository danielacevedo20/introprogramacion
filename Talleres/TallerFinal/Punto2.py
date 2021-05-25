
from typing import Text


isCorrectInfo = False
while(isCorrectInfo ==False):
    parrafo = input("Ingrese un parrafo y termine en punto: ")
    isCorrectInfo= parrafo.endswith(".")
    if isCorrectInfo == True:
        parrafo = parrafo[:-1]
        parrafo = parrafo.replace(",","")
        palabras = parrafo.split(" ")
        print(max(palabras, key = len))
        print(min(palabras, key = len))
    else:
        print("El parrafo no termina en punto")


