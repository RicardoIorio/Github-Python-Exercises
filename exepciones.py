import math

def calculaRaiz(num1):

	if num1<0:
		raise ValueError ("El numero no puede ser negativo")

	else:
		return math.sqrt(num1)

op1=(int(input("inroduce un numero: ")))

try:

	print(calculaRaiz(op1))

except ValueError as Errordenumeronegativo:
	print(Errordenumeronegativo)

print("programa terminado")