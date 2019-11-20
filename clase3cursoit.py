#INICIALIZACION DE VARIABLEAS Y LISTAS
#Lista (Matriz) de alumnos
alumnos = [["Juana", 28, 10], 
			["Carla", 35, 8 ], 
			["Pedro", 24, 7], 
			["Tomasa", 25, 9], 
			["Casimiro", 24, 4],
			["Jacinta", 34, 7], 
			["Bartolomeo", 29, 3], 
			["Pepino", 36, 1]]
#Acumuladores y contadores
total_nota = 0
total_edad = 0
mayores_que_30 = 0
menores_que_30 = 0
aprobados = 0
desaprobados = 0

#CUERPO PRINCIPAL DEL PROGRAMA

#Imprimo un encabezado de solo decoración
print("----------------------------------------")
print("<<<<<<  Listado de Alumnos >>>>>>>>>>>>>")
print("----------------------------------------")
print("| Nombre | Edad | Nota |")

#Recorremos la matriz con un for
for alumno in alumnos:
	#Desconemos la matriz para trabajar con cada campo individualmente
	nombre, edad, nota = alumno
	#Imprimo el contenido de los campos de la lista
	print("| {} | {} | {}".format(nombre, edad, nota))
	#Acumuladores en accion 
	#(Notese que uso la forma a = a + c y a += c indistintamente porque tiene el mismo efecto)
	total_nota = total_nota + nota
	total_edad += edad
	#Pregunto si edad es mayor a 30, si es verdadero los cuento, de igual manera si son menores 
	if edad >= 30:
		mayores_que_30 += 1
	else:
		menores_que_30 += 1
	#Contabilizo aprobados y desaprobados
	if nota >= 4:
		aprobados += 1
	else:
		desaprobados += 1

#Solo decoración
print("----------------------------------------")

#Calculo promedios
#La instruccion round() lo que hace es redondear un valor decimal
promedio_nota = total_nota / len(alumnos)
promedio_edad = round(total_edad / len(alumnos))

#Muestro los resultados totales y promedios
print(" ")
print("> Promedio de edad: {}".format(promedio_edad))
print("> Promedio de nota: {}".format(promedio_nota))
print("> Cantidad de alumnos: {}".format(len(alumnos)))
print("> Cantidad de alumnos aprobados: {}".format(aprobados))
print("> Cantidad de alumnos desaprobados: {}".format(desaprobados))
print("> Alumnos mayores de 30: {}".format(mayores_que_30))
print("> Alumnos menores de 30: {}".format(menores_que_30))
print("----------------------------------------")
