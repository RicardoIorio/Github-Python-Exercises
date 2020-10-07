def generador(*ciudades):
	for elemento in ciudades:
		#for subelemento in elemento:
			yield from elemento

ciudades_devueltas=generador("neuquen","Buenos aires","berlín")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))