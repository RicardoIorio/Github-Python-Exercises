class persona():
	def __init__(self,nombre,edad,lugarderesidencia):
		self.nombre = nombre

		self.edad=edad

		self.Lugarderesidencia=lugarderesidencia

	def descripcion(self):

		print("nombre:",self.nombre,"Edad: ",self.edad,"residencia:",self.Lugarderesidencia)

class empleado(persona):

	def __init__(self,salario,antiguedad,nombre,empleadoedad,residencia_empleado):

		super().__init__("antonio","55","argentina")

		self.salario=salario

		self.antiguedad=antiguedad

antonio=persona("manuel",55,"argentina")

antonio.descripcion()

print(isinstance(antonio, empleado))
	