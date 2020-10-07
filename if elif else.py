print("materias año 2018")
print("materias optativas: Informática gráfica - Pruebas de software - Usabilidad y Accesibilidad")
opcion=input("escribe la materia escogida: ")

materia=opcion.lower()

if materia in ("informática gráfica","pruebas de software","usabilidad y accesibilidad"):
	print("materia elegida "+ materia)
	print("felicitaciones")

else:
	print("materia erronea")

