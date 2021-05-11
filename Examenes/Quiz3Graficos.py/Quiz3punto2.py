import matplotlib.pyplot as plt

listaCiudades = []
listaPoblaciones = []
for i in range (5):
    ciudad = input("Agregue un ciudad: ")
    poblacion = input("Agregue la población de esta ciudad: ")
    listaCiudades.append (ciudad)
    listaPoblaciones.append (poblacion)
    print (f"Haga este proceso {4-i} veces")
print (listaCiudades)
print (listaPoblaciones)
maximo = listaPoblaciones.index(max(listaPoblaciones))
pieExplode = [0,0,0,0,0]

pieExplode [maximo]= 0.2

plt.pie(listaPoblaciones, labels=listaCiudades, explode= pieExplode)
plt.title("Población de las ciudades favoritas")
plt.savefig("Ciudades.png")
plt.show()