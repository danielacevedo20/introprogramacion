#Ingresamos variables
edad = 18
estatura = 1.8
peso = 75
NOMBRE = "Jose Daniel Acevedo Restrepo"
#Aprendimos a usar funciones de lógica buleana "bool"
isMayorEdad = edad >= 18
#Comparamos el valor de las variables
print ("#"*15,"¿Es mayor de edad?", "#"*15)
#Mostramos en pantalla true o false con la función print como resultado de la función bool
print (isMayorEdad)

#Practicamos la función bool
isEstaturaPromedio = estatura > 1.7
print("#"*20,"¿Es mayor a la estatura promedio?","#"*20)
print (isEstaturaPromedio)
print("#"*20,"¿Tiene un peso Diferente de 84?","#"*20)
isPesoDiferente = peso != 84
print (isPesoDiferente)
# Vamos a ver si un apellido está en el nombre completo por medio de la función in
apellido = "Acevedo"
IsApellido = apellido in NOMBRE
print("#"*20,"¿Está el apellido en el nombre?","#"*20)
print (IsApellido)
