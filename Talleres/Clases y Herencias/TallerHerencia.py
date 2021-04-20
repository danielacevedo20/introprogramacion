class Persona ():
    def __init__(self, idIn,nombreIn,edadIn):
        self.edad = edadIn
        self.nombre = nombreIn
        self.id = idIn
    def hablar (self, mensaje):
        print (f"Hola soy {self.nombre} y tengo un mensaje que decir...", mensaje)
    def caminar (self, pasos):
        for i in range (pasos):
            print (f"He camino {i + 1} pasos")
Juan = Persona (12312,"Juan",32)
Juan.hablar ("Buenas señores")
Juan.caminar (10)
print ("#"*20)

class Doctor (Persona):
    def __init__(self, idIn,nombreIn,edadIn, especialidadIn):
        Persona.__init__(self, idIn,nombreIn,edadIn)
        self.especialidad = especialidadIn
    def tratar (self, enfermedadIn):
        print (f'''        Hola soy el doctor {self.nombre}, me especializo 
        en {self.especialidad} y voy a tratar la enfermedad {enfermedadIn}''')
Ricardo = Doctor (1212124,"Ricardo",28,"cardiología")
Ricardo.tratar ("arritmia")
print ("#"*20)

class Nutricionista (Persona):
    def __init__(self, idIn,nombreIn,edadIn, universidadIn):
        Persona.__init__(self, idIn,nombreIn,edadIn)
        self.universidad = universidadIn
    def calcularIMC (self, pesoIn, alturaIn):
        imc = pesoIn/(alturaIn**2)
        informacion = f"        El imc calculado es de {imc}"
        return informacion
Juana = Nutricionista (22234142, "Juana",22, "Universidad CES")
calculadoraDeIMC = Juana.calcularIMC (75,1.83)
print (calculadoraDeIMC)
print ("#"*20)

class Abogado (Persona):
    def __init__(self, idIn,nombreIn,edadIn,especialidadIn, universidadIn):
        Persona.__init__(self, idIn,nombreIn,edadIn)
        self.especialidad = especialidadIn
        self.universidad = universidadIn
    def representar (self,representado, caso):
        print (f'''procedo a representar al cliente
{representado} en el caso de {caso}''')
Ana = Abogado(23213,"Ana",23,"Derecho laboral", "Universidad CES")
Ana.representar ("Pedro", "demanda empresarial")