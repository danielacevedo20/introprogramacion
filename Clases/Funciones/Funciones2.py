import ConversorT as ct
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
TemperaturaCorporalFahrenheint = ct.conversionTemperatura(Temperatura_Corporal, "K")
print (TemperaturaCorporalFahrenheint)

TemperaturaCorporalKelvin = ct.conversionTemperatura(Temperatura_Corporal, "F")
print (TemperaturaCorporalKelvin)

clasificacionTemperaturas = ct.clasificadorT (Temperatura_Corporal)
print (clasificacionTemperaturas)