import pickle

class persona:

	def __init__(self,nombre,genero,edad):
		self.genero=genero
		self.nombre=nombre
		self.edad=edad
		print("se ha creado una persona nueva con el nombre de ",self.nombre)


	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)


class listapersonas:

	personas=[]

	def __init__(self):
		listadepersonas=open("fichero_externo","ab+")
		listadepersonas.seek(0)

		try:


			self.personas=pickle.load(listadepersonas)
			print("se cargaron {} personas del fichero externo".format(len(self.personas)))

		except:
			print("el fichero esta vacio")

		finally:
			listadepersonas.close()
			del(listadepersonas)

	def agregarpersonas(self, p):
		self.personas.append(p)
		self.guardarpersonasenficheroexterno

	def mostrarpersonas(self):
			for p in self.personas:
				print(p)

	def guardarpersonasenficheroexterno(self):
		listadepersonas=open("fichero_externo", "wb")
		pickle.dump(self.personas,listadepersonas)
		listadepersonas.close()
		del(listadepersonas)

	def mostarinfoficheroexteno(self):
		print("la info del fichero externo es la sig: ")
		for p in self.personas:
			print (p)

milista=listapersonas()
persona=persona("sandra", "femenino",29)
milista.agregarpersonas(persona)





