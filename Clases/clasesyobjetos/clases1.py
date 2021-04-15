class Humano ():
    '''Mensaje que define a la clase



    '''
    def __init__ (self, nombreEntrada, edadEntrada, entradaEstatura):
        print ("Hola soy humano")
        self.edad = (edadEntrada)
        self.raza = "Humano"
        self.nombre = nombreEntrada
        self.estatura = entradaEstatura
        self.dinero = 0
    def hablar (self, mensaje):
        print (f"Hola soy {self.nombre} y tengo un mensaje que decir...", mensaje)
    def mostrarAtributos (self):
        print (f'''Mi nombre es {self.nombre}
        Mi edad es {self.edad}
        Mi estatura es {self.estatura}''')
    def recorrerDistancia (self, distanciaMetros):
        for i in range (distanciaMetros):
            print (f"Hola soy {self.nombre} y he recorrido {i+1} metros")
    def ahorrarDinero (self):
        preguntaIngresarMontos ='''S para añadir montos
        N para finalizar: '''
        preguntaMonto = "Cuanto vas a ingresar: "
        ingresarMontos = input(preguntaIngresarMontos)
        while(ingresarMontos != "N"):
            monto = float(input(preguntaMonto))
            self.dinero = self.dinero + monto
            print (f"Llevas {self.dinero} ahorrado")
            ingresarMontos = input(preguntaIngresarMontos)
        return self.dinero

class Biomedico (Humano):
    def mantenimiendo (self, equipo):
        print (f"Hola soy un ingeniero biomédico y me llamo {self.nombre} y puedo arreglar un {equipo}")


humano1 = Humano("Daniel",18,1.83)

humano1.hablar("Espero que estén muy bien")
humano1.mostrarAtributos ()
humano1.recorrerDistancia(5)
totalAhorrado = humano1.ahorrarDinero()
print (totalAhorrado)
ingeniero = Biomedico("Daniel", 18,1.83)
ingeniero.mostrarAtributos ()
ingeniero.mantenimiendo("Electrocardiograma")