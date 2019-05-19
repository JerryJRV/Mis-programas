#calcular la media de 4 notas
print ("Bienvenido!!!")
nota_1= int(input("Porfavor Ingrese la Nota 1: "))
nota_2= int(input("Ahora la Nota 2: "))
nota_3= int(input("La Nota 3: "))
nota_4= int(input("Y por ultimo Ingrese la Nota 4: "))
promedio= nota_1+nota_2+nota_3+nota_4
if promedio/4 <= 10:
	print ("Usted esta reprobado")
else:
	print ("Usted Aprobo el Curso!!!")

print ("El promedio de sus notas es: ",promedio/4)