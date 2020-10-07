import math
print("programa de calculo de raiz cuadrada")
numero=int(input("introduzca el numero: "))

intentos=0

while numero<0:
	intentos=intentos+1

	print("no se puede realizar la raíz de ese número")

	if intentos==2:
		print("has consumido demasiada droga")
		break;
	numero=int(input("introduce el numero: "))

if intentos<2:
	solucion=math.sqrt(numero)
	print("la raíz cuadrada de ",numero,"es",solucion)