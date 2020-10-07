print("programa de evaluacionde notas de alumnos")
nota_alumno=input("nota del alumno = ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<=5:
		valoracion="desaprobado"
		calificación=7
	return valoracion


print(evaluacion(int(nota_alumno)))