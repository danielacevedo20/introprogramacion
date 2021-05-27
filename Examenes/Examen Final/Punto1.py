def GraficarBarras (NombreGrafico, NombreColumnas, NombreValores,NumeroElementos):
    import matplotlib.pyplot as plt
    listaColumnas = []
    listaValores = []
    for i in range (NumeroElementos):
        columna = input (f"Ingrese un {NombreColumnas} para la columna: ")
        valores = input (f"Ingrese un {NombreValores} para los valores: ")
        listaColumnas.append(columna)
        listaValores.append(valores)
        print (f"Haga este proceso {(NumeroElementos - 1)-i} veces")
    print (listaColumnas)
    print(listaValores)
    plt.bar (listaColumnas,listaValores, width= 0.6)
    plt.title(NombreGrafico)
    plt.xlabel(NombreColumnas)
    plt.ylabel(NombreValores)
    plt.savefig(f"{NombreGrafico}.png")
    plt.show()

GraficarBarras("Alimentos favoritos","Alimento","Precio",8)
