#La librería es muy grande. así que sólo importamos una parte
import matplotlib.pyplot as plt
##
lenguajes=["Py","Java","Dart","Ts","Elixir"]
encuesta = [50,10,20,10,10]
##
plt.bar(lenguajes, encuesta, width=0.6, color = "c")
##
plt.title("Lenguajes más usados")
plt.xlabel("Lenguajes de programación")
plt.ylabel("% de uso de lenguajes")
plt.savefig("graficoslenguaje.png")
##
plt.show()