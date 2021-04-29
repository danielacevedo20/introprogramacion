import matplotlib.pyplot as plt
#Labels: Nombres de las porciones de la torta
pielabels = ["Py","Java","Dart","Ts","Elixir"]
# Sizes: Tamaños para cada porción de la torta  
piesizes = [40,25,15,10,10]
#Explode: Que tan alejado del origen de la torta
pieexplode = [0,0.2,0,0,0]

plt.pie(piesizes, labels = pielabels, explode = pieexplode, shadow = True, startangle = 45)
plt.title("Lenguajes más usados")
plt.show()


def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        pieLabels[i] += indicador+str(sizes[i]/acumulador*100) +'%'


pieExplode = [0,0,0.2,0]
acumulador = 0
sizes = [50,25,15,10]
pieLabels = ['python', 'java', 'dart', 'js',]
etiquetarElementosPorcentuales(sizes,pieLabels,'☺')

plt.pie(sizes,labels=pieLabels, 
        explode=pieExplode, 
        shadow= True, 
        counterclock = True, 
        startangle= 45)
#####################
plt.title('Uso de lenguajes de programación en el 2021')
plt.savefig('tortasLenguajes.png')
#####################
plt.show()
