print("programa de evaluacion de notas de alumnos")
nota_alummno=input("indtroduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
		calificacion=7
	return valoracion

print(evaluacion(int(nota_alummno)))
