print("Programa de evaluacion de notas de alumnos")

notas_alumno=input("introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<=5:
		valoracion="suspenso"
	return valoracion
	

print(evaluacion(int(notas_alumno)))