class Usuario ():
    def __init__(self, nombreIn,edadIn, sexoIn, nacionalidadIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.sexo = sexoIn
        self. nacionalidad = nacionalidadIn
    def mostrarAtributos (self):
        print (f'''        El nombre del usuario es {self.nombre}
        su edad es {self.edad}
        su sexp es {self.sexo}
        y su nacionalidad es {self.nacionalidad}
        ''')
pedro = Usuario("Nacional",26,"Masculino","Colombiana")
pedro.mostrarAtributos