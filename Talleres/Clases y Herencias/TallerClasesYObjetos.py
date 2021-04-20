class Torta ():
    def __init__ (self, formaIn, saborIn, alturaIn):
        self.forma = formaIn
        self.sabor = saborIn
        self.altura = alturaIn
    def mostrarAtributos (self):
        print (f'''        La torta es de sabor {self.sabor}
        su forma es {self.forma}
        y mide {self.altura}cms de alto''')
tortaMora = Torta("Redonda", "Mora", 20)
tortaMora.mostrarAtributos ()
print ("#"*20)
class Estudiante ():
    def __init__ (self, edadIn, nombreIn, idIn, carreraIn, semestreIn):
        self.edad = edadIn
        self.nombre = nombreIn
        self.id = idIn
        self.carrera = carreraIn
        self.semestre = semestreIn
    def estudiarMateria (self,materiaIn, horasEstudio):
        print (f'''        el alumno estudiará la asignatura
        {materiaIn} durante {horasEstudio}hrs''')
Daniel = Estudiante (18,"Daniel",24124124,"Ing biomédica",3)
Daniel.estudiarMateria ("Morfofisiología",4)

print ("#"*20)
class Nutricionista ():
    def __init__(self, edadIn, nombreIn, universidadIn):
        self.edad = edadIn
        self.nombre = nombreIn
        self.universidad = universidadIn
    def calcularIMC (self, pesoIn, alturaIn):
        imc = pesoIn/(alturaIn**2)
        informacion = f"        El imc calculado es de {imc}"
        return informacion
Juana = Nutricionista (22, "Juana", "Universidad CES")
calculadoraDeIMC = Juana.calcularIMC (75,1.83)
print (calculadoraDeIMC)

print ("#"*20)
class Canguro ():
    def __init__ (self, edadIn, idIn, nombreIn):
        self.edad = edadIn
        self.nombre = nombreIn
        self.id = idIn
    def saltar (self, cantidadDeSaltos):
        for i in range (cantidadDeSaltos):
            print (f"El canguro a dado {i +1} salto")
Spike = Canguro(8,312412,"Spike")
Spike.saltar(5)

print ("#"*20)
class Guitarra ():
    def __init__ (self, tipoIn, marcaIn, colorIn):
        self.tipo = tipoIn
        self.marca = marcaIn
        self.color = colorIn
    def tocarGuitarra (self, cancion):
        print(f"Están tocando la canción {cancion} en la guitarra")
azula = Guitarra("Eléctrica","Yamaha","Azul")
azula.tocarGuitarra ("Sweet Child Or Mine")