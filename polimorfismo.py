class coche():

	def desplazamiento(self):
		print("me desplazo utilizando 4 ruedad")

class moto():

	def desplazamiento(self):
		print("me desplazo utilizando 2 ruedas")


class camion():
	def desplazamiento(self):
		print("me desplazo utilizando 6 ruedas")




def desplazamientovehiculo(vehiculo):
	vehiculo.desplazamiento()


micamion=moto()
desplazamientovehiculo(micamion)




