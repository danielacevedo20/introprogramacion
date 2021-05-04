import matplotlib.pyplot as plt

tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9,10]
plt.plot(tiempo,sensor,"r")
plt.title("Gráfico de sensor contra tiempo")
plt.xlabel("Tiempo(s)")
plt.ylabel("Voltaje (mV)")
plt.show()



plt.plot(tiempo,sensor,"<")
plt.show()

plt.plot(tiempo,sensor,"--,c")
plt.show()

diccionario{}
diccionario["NombreEstudiantes"] = ["Jacobo","Daniel","Maria","Elena"]
diccionario["Edad"] = [18,17,24,32]
diccionario["Peso"] = [54,76,87,68]
print(diccionario)
print(diccionario["NombresEstudiantes"][-1], ["Edad"][-1],["Peso"][-1])