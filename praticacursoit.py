print("Bienvenido al programa para contrataciones")

ciudad= input("Por favor, ingrese su ciudad: ")

if ciudad== "cordoba":
	print("la ciudad ingresada es la solicitada")
	edad=int(input("Por favor,ingrese su edad: "))
	if edad>=18 and edad<=65:
		print("la edad es la solicitadad")
		print("usted esta contratado")
	else:
		print("la edad no es la solicitada")	
		print("el programa ha finalizado")


else:
	print("ciudad no requerida")	
	print("el programa ha finalizado")