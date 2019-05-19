#crear un programa que me calcule el interes a ganar y me muestre 
#el interes ganado sumado al sueldo por año

sueldo= float(input("Ingrese su sueldo a calcular: "))
años= int(input("Ingrese cantida de años: "))
tasa= float(input("Ingrese la tasa de interes a ganar: "))
c=0
i= 0
interes_total=0
for x in range (1,10000000):
	i=sueldo *tasa/100
	interes_ganado= sueldo*tasa/100
	sueldo +=i
	interes_total+= interes_ganado
	print ("Sueldo mas Interes Ganado en el año %s"%x,sueldo)
	c+= 1
	if c == años:
		print("Interes total ganado: ",interes_total)
		print ("Fin del calculo!!")
		break

