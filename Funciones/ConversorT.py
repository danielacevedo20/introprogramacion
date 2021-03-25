def conversionTemperatura (temperaturas, unidad):
    '''Convierte una lista de temperaturas
    según la unidad ingresada, puede ser
    K --> Para kelvin
    F --> Para fahrenheint
    '''
    listaConvertida = []
    for temperatura in temperaturas:
        conversion = None
        if (unidad == "F"):
            conversion = temperatura*1.8 +32
        elif (unidad=="K"):
            conversion = temperatura + 273.15
        else:
            listaConvertida = None
        listaConvertida.append (conversion)
    return listaConvertida

def clasificadorT (temperaturas)
    listaClasificacion = []
    for elemento in temperaturas:
        clasificacion = ""
        if (elemento<36):
            clasificacion = "Hipotermia"
        elif (elemento >=36 and elemento <37.6):
            clasificacion = "Temperatura normal"
        else:
            clasificacion = "Fiebre"
        listaClasificacion.append (clasificacion)
    return listaClasificacion
