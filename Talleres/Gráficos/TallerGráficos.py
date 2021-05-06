import matplotlib.pyplot as plt

ingresos = [1200000,1000000,980000,870000,1400000,900000,1200000,850000,800000,950000,1050000,1500000]
meses = ["Enero", "Febrero", "Marzo", "Abril" , "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
colores = ["b","g","r","c","m","y","k","b","g","r","c","m"]

plt.bar(meses, ingresos, width=0.6, color = colores)
plt.title("Ingresos mensuales de una persona")
plt.xlabel("Meses del año")
plt.ylabel("Ingresos")
plt.show()


def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        porcentaje = round(sizes[i]/acumulador*100,2)
        pieLabels[i] += indicador+str(porcentaje) +'%'


pieExplode = [0.2,0,0,0,0]
acumulador = 0
sizes = [8380801,2569007,2496346,1249804,1057767]
pieLabels = ["Bogotá","Medellín","Cali","Barranquilla","Cartagena"]
etiquetarElementosPorcentuales(sizes,pieLabels)

plt.pie(sizes,labels=pieLabels, 
        explode=pieExplode, 
        shadow= True, 
        counterclock = True, 
        startangle= 90)
plt.title("Ciudades más pobladas de Colombia")
plt.show()

import pandas as pd

ppgData = pd.read_csv ("ppg.csv",encoding="UTF-8",header=0,delimiter=";").to_dict()
muestras = list(ppgData["muestra"].values())
valores = list(ppgData["valor"].values())
plt.plot(muestras, valores)
plt.xlabel("Tiempo (ms)")
plt.ylabel("Voltaje (mV)")
plt.title("Fotopletismografía")
plt.show()