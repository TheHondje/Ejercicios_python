print("Bienvenido al programa de contratción")

ciudad_usuario= input("ingrese su ciudad: ")

if ciudad_usuario== "cordoba":
	print("ciudad solicitada")

	edad_usuario= int(input("ingrese su edad: "))

else:
	print("la ciudad no es la requerida")
	print("el programa ha finalizado")

		
if ciudad_usuario== "cordoba" and edad_usuario>=18 and edad_usuario<=64:
		print("Usted esta contratado")
		print("el programa ha finalizado")


if ciudad_usuario== "cordoba" and edad_usuario<=17:
		print("usted es menor de edad, no podemos contratarlo")


if ciudad_usuario== "cordoba" and edad_usuario>=65:
		print("la edad es muy alta")
		print("usted no cumple con los requisitos")
		print("el programa ha finalizado")







