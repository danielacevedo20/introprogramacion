#----Constantes----#
MENSAJE_BIENVENIDA = "Hola! vamos a ver si te alcanza para tu nuevo pc"
PREGUNTA_VALOR_PC = "¿Cuánto vale el pc que deseas?: "
MENSAJE_CUANTO_TIENE = "¿Cuánto dinero tienes ahorrado?: "
MENSAJE_AHORRO = "Llevas ahorrado ..."

#Entradas
print (MENSAJE_BIENVENIDA)
Valor = float (input(PREGUNTA_VALOR_PC))
ahorrado = float (input(MENSAJE_CUANTO_TIENE))

while (Valor > ahorrado):
    print (MENSAJE_AHORRO, ahorrado, "Te faltan...", Valor-ahorrado)
    ahorrado = ahorrado + 1000
print (Valor==ahorrado)