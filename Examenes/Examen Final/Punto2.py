class Humano ():
    def __init__(self,nombreIn,sexoIn,edadIn):
        self.edad = edadIn
        self.nombre = nombreIn
        self.sexo = sexoIn
    def hablar (self, mensaje):
        print (f"Hola soy {self.nombre} y tengo un mensaje que decir...", mensaje)
Juan = Humano("Juan","Masculino",23)
Juan.hablar("Que tengan un feliz día!!")

class Doctor (Humano):
    def __init__(self,nombreIn,sexoIn,edadIn):
        Humano.__init__(self,nombreIn,sexoIn,edadIn)
    def calcularIMC (self, pesoIn, alturaIn):
        imc = pesoIn/(alturaIn**2)
        informacion = f"        El imc calculado es de {imc}"
        return informacion
María = Doctor("María","Femenino",22)
imc = María.calcularIMC(83,1.84)
print(imc)