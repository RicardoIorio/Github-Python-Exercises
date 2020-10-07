class Coche():

	def __init__(self):
		self.__largoChasis=250
		self.__Anchochasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self, arrancamos):

		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			chequeo=self.__ChequeoInterno()

		if(self.__enmarcha and chequeo):
			return"El coche esta en marcha"

		elif(self.__enmarcha and chequeo==False):
			return "algo salio mal en el chequeo no se puede arrancar"

		else:

			return"el coche no esta en marcha"

	def estado(self):
		print("el coche tiene ",self.__ruedas,"ruedas. Un ancho de ",self.__Anchochasis,"y un largo de ", self.__largoChasis)

	def __ChequeoInterno(self):
		print("realizando chequeo interno")

		self.nafta="ok"
		self.aceite="ok"
		self.puertas="cerradas"


		if(self.nafta=="ok" and self.aceite=="no" and self.puertas=="cerradas"):

			return True

		else:

			return False
		
micoche=Coche()

print(micoche.arrancar(True))

micoche.estado()



print("-------------------------a continuacion creamos otro objeto---------------------------")

micoche2=Coche()

print (micoche2.arrancar(False))

micoche2.estado()
