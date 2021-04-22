class ElementosDigitales ():
    def __init__ (self, nombreEntrada, creadorEntrada, fechaEntrada):
        self.nombre = nombreEntrada
        self.creador = creadorEntrada
        self.fecha = fechaEntrada
    
    def mostrarAtributos (self):
        print (f'''         El nombre es {self.nombre},
        el creador es {self.creador} y 
        la fecha de publicación fue en {self.fecha}
        ''')

facebook = ElementosDigitales("facebook","Mark","Febrero")
facebook.mostrarAtributos()
print ('#'*50)
class Usuario ():
    def __init__(self, nombreIn,edadIn, sexoIn, nacionalidadIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.sexo = sexoIn
        self. nacionalidad = nacionalidadIn
    def mostrarAtributos (self):
        print (f'''        El nombre del usuario es {self.nombre}
        su edad es {self.edad}
        su sexo es {self.sexo}
        y su nacionalidad es {self.nacionalidad}
        ''')
pedro = Usuario("Pedro",26,"Masculino","Colombiana")
pedro.mostrarAtributos()
print ('#'*50)
class Pagina ():
    def __init__ (self, tipoIn, formatoIn, fechaIn):
        self.tipo = tipoIn
        self.formato = formatoIn
        self.fecha = fechaIn
    
    def mostrarAtributos (self):
        print (f'''        La página es de tipo {self.tipo},
        su formato es {self.formato} 
        y su fecha de publicación fue {self.fecha}
        ''')

texto = Pagina ('artículo','PDF','Diciembre 2020')
texto.mostrarAtributos()
print ('#'*50)

class cancion (ElementosDigitales):
    def __init__ (self, nombreEntrada, creadorEntrada, fechaEntrada, generoIn, duracionIn):
        ElementosDigitales.__init__ (self, nombreEntrada, creadorEntrada, fechaEntrada)
        self.genero = generoIn
        self.duracion = duracionIn
        print (f'''        Se creó una canción nueva
        que se llama {self.nombre}
        y se creo el {self.fecha}''')
    def reproducircancion (self, numerorepeticiones):
        for i in range (numerorepeticiones):
            print (f''' La canción {self.nombre} ha sonado {i + 1} vez''')

Mine = cancion("Sweet Child Or Mine", "Guns And Roses", "24 de noviembre de 2001", "Rock", "300")
print ('#'*50)
Mine.reproducircancion (5)

