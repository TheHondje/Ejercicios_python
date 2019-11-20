print("verificacion de acceso")

edad_usuario=int(input("introduce tu edad: "))

if edad_usuario<18:
	print("no puedes pasar")
	print("el programa ha finalizado")
elif edad_usuario>100:
	print("su edad es incorrecta")
else:
	print("puedes pasar")
	print("el programa ha finalizado con exito")
print("hasta luego")
