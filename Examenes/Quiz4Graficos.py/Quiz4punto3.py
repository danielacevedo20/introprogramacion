import pandas as pd
import matplotlib.pyplot as plt
print ('''Un electrocardiograma (ecg), es una 
prueba que muestra la actividad del corazón midiendo
los impulsos electricos que este manda (en mV)
en función del tiempo (ms)''')

ecgData = pd.read_csv ("ecg.csv",encoding="UTF-8",header=0,delimiter=";").to_dict()
muestras = list(ecgData["muestra"].values())
valores = list(ecgData["valor"].values())
plt.plot(muestras, valores)
plt.xlabel("Tiempo (ms)")
plt.ylabel("Voltaje (mV)")
plt.title("Electrocardiograma")
plt.savefig("ecg.png")
plt.show()

print('''Una fotopletismografía (ppg)
es una técnica usada para determinar el volumen de un órgano,
lo hace por medio de un haz de luz incidente con el cual mide la respuesta
del órgano (en mV) en función del tiempo (ms)''')

ppgData = pd.read_csv ("ppg.csv",encoding="UTF-8",header=0,delimiter=";").to_dict()
muestras = list(ppgData["muestra"].values())
valores = list(ppgData["valor"].values())
plt.plot(muestras, valores)
plt.xlabel("Tiempo (ms)")
plt.ylabel("Voltaje (mV)")
plt.title("Fotopletismografía")
plt.savefig("ppg.png")
plt.show()