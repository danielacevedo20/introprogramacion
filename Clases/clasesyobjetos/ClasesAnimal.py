
import random
class Lobo ():
    def __init__ (self, nameIn, razaIn, edadIn, colorIn, sexoIn):
        print ("¡Cuidado!, hay un lobo cerca")
        self.edad = edadIn
        self.raza = razaIn
        self.color = colorIn
        self.sexo = sexoIn
        self.name = nameIn
    def aullar (self):
        veces = int(input("¿Cuántas veces escuchaste los aullidos?: "))
        for i in range (veces):
            print("Oehehehehehehhhhhooeoeoeoe")
    def acercarse (self):
        print("Un lobo se está acercando ¿Qué vas a hacer?")
        pregunta = int(input('''
        1. Para correr
        2. Para acercarme y verlo de cerca
        :'''))
        if (pregunta == 1):
            print ("¡Corre! Te está  siguiendo")
        elif (pregunta == 2):
            accion = random.randint (1,2)
            if (accion == 1 ):
                print (f'''
                Un lobo se está acercando, parece amigable
                Ves que es de raza {self.raza}
                Su pelaje tiene un color {self.color}
                También observas que es {self.sexo}
                Le calculas una edad de {self.edad} años
                Y como es amigable decides llamarlo {self.name}''')
            else:
                print ("Te mordió!! Corre como nunca")
        else:
            print ("Opción invalida")


Ghost = Lobo("Ghost","Huargo", 5, "Albino", "Macho")
Ghost.aullar()
Ghost.acercarse ()
Fenrir = Lobo ("Fenrir","Timber Wolf", 7,"Negro", "Macho")
Fenrir.acercarse()
