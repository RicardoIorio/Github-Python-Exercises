email=input("tu email: ")

while (email.isdigit()==True):
	print("inroduce tu email")
	email=input("tu email: ")

if(email.find("@")==0):
	print("email incorrecto")

elif (email.rfind("@")==-1):
	print("email incorrecto")

elif (email.count("@")==1):
	print("email correcto")
else:
	print("no tiene @")
