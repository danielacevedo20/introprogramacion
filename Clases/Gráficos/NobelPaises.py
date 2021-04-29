import matplotlib.pyplot as plt


paises=["Estados Unidos","Alemania","Reino Unido","Francia","Rusia","Países Bajos","Japón","Suiza","Suecia","Italia","Dinamarca","Otros"]
encuesta = [88,25,23,12,10,9,8,6,4,4,3,19]
plt.bar(paises, encuesta, width=0.3, color = ["b","g","r","c","m","y","k","b","g","r","c","m"])


plt.title("Ganadores del premio nobel de física por país")
plt.xlabel("País")
plt.ylabel("Número de galardonados")
plt.savefig("ganadoresNobele.png")

plt.show()

plt.plot(paises,encuesta)
plt.s
plt.show()