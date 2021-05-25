isCorrectInfo = False
while(isCorrectInfo == False):
    try:
        nombre = input("Ingrese su nombre: ")
        assert (nombre.isalpha())
        isCorrectInfo = True
        print(f"Hola {nombre} ¡bienvenido al programa!")
    except AssertionError:
        print("Ingresaste un dato erroneo")

def CalcularIMC():
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            peso = float (input("Ingrese su peso: "))
            isCorrectInfo = True
        except ValueError:
            print("Ingresaste un dato erroneo")
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            estatura = float (input("Ingrese su estatura: "))
            isCorrectInfo = True
        except ValueError:
            print("Ingresaste un dato erroneo")
    imc =round (peso/(estatura**2),2)
    print(f"Tu IMC es {imc}")
CalcularIMC()