class vehiculos():

	def __init__(self,marca,modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):

		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha,"\nArranca:",self.acelera,"\nFrena:",self.frena)


class moto(vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="voy haciendo un willie"

	def estado(self):
		print("marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha,"\nArranca:",self.acelera,"\nFrena:",self.frena,"\n",self.hcaballito)

class Camioneta(vehiculos):
	
	def carga(self,cargar):
		self.cargado=cargar

		if(self.cargado):
			return("la camioneta esta cargada")
		else:
			return("la camioneta no esta cargada")



class VElectricos(vehiculos):
	def __init__(self,marca,modelo):

		super().__init__(marca,modelo)

	def __init__(self):
		self.autonomia=100
	def cargarenergía(self):
		self.cargando=True





