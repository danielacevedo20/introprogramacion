import matplotlib.pyplot as plt

listaSnacks = []
listaPrecios = []
for i in range (5):
    snack = input("Agregue un snack: ")
    precio = input("Agregue el precio de ese snack: ")
    listaPrecios.append (precio)
    listaSnacks.append (snack)
    print (f"Haga este proceso {4-i} veces")
print (listaSnacks)
print (listaPrecios)
colores = ["b","g","r","c","m"]
plt.bar (listaSnacks,listaPrecios, width= 0.6, color = colores)
plt.title("Precio de los Snack favoritos")
plt.xlabel("Snacks")
plt.ylabel("Precio")
plt.savefig("Snacks.png")
plt.show()

