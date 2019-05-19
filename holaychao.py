#Crear una funcion que salude dependiendo del numero ingresado, si es igual o menor a 100 "hola"
# si esta entre 100 y 200 "chao", si es mayor a 200 "adios"
def a():
	b = int(input("Ingrese un numero: "))
	if b < 100 :
		print("hola")
	elif b >= 100 and b <=200:
		print("chao")
	elif b >= 201:
		print("adios")

while True:
	a()