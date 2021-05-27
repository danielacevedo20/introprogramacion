def ConversorEurosEnDolares ():
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            nombre = input("Ingrese su nombre: ")
            assert (nombre.isalpha())
            isCorrectInfo = True
        except AssertionError:
            print("Ingresaste un dato erroneo")
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            dinero = float(input("Ingrese la cantidad de dinero (en dolares) que tiene: "))
            isCorrectInfo = True
        except ValueError:
            print("Ingresaste un dato erroneo")
    print(f'Hola {nombre}, la cantidad de dinero que tienes en euros es {dinero*0.82}')
ConversorEurosEnDolares()