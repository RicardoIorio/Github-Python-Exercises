from io import open

archivo_texto=open("archivo.txt","r+") #lectura y escritura

archivo_texto.write("Comienzo del texto")
#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines()

lista_texto[2]="esta linea ha sido incluida desde el exterior \n"


archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)
archivo_texto.close()