lista_estudiantes={}
class Estudiante():
	nombre=""
	apellido=""
	cedula=0
	pnf=""
	def __init__(self):
		self.nombre=""
		self.apellido=""
		self.cedula=0
		self.pnf=""
	def menu(self):
		print("Estudiantes de la UPTBAL")
		print("1. Registrar Estudiante")
		print("2. Buscar Estudiante")
		print("3. Borrar Estudiante")
		print("4. Estudiantes Registrados")
		print("5. Salir del Menu")
		opcion=int(input("introducir la opcion que desea: "))
		if opcion==1:
			self.registrar()
		elif opcion==2:
			self.buscar()
		elif opcion==3:
			self.borrar()
		elif opcion==4:
			self.registro()
		elif opcion==5:
			print("Saliendo del programa....")
			exit()
		self.menu()
	def registrar(self):
		datos_estudiantes=[]
		print("_________________________________")
		print("Registrar Estudiante en la UPTBAL")
		print("_________________________________")
		self.ci=input("Introducir Cedula del Estudiante: ")
		c=self.comprobar(self.ci)
		if not (c):
			self.nombre=str(input("Nombre del Estudiante: "))
			self.apellido=str(input("Apellido del Estudiante: "))
			self.pnf=str(input("PNF que Estudia: "))
			datos_estudiantes.append(self.nombre)
			datos_estudiantes.append(self.apellido)
			datos_estudiantes.append(self.pnf)
			lista_estudiantes[self.ci]=datos_estudiantes
	def comprobar(self,ci):
		if ci in lista_estudiantes:
			print("Estudiante Registrado")
			v=True
		else:
			print("Estudiante No Registrado")
			v=False
		return v	
	def buscar (self):
		print("_______________________________")
		print("Buscar Estudiantes de la UPTBAL")
		print("_______________________________")
		ci=input("Introducir Cedula del Estudiante: ")
		if ci in lista_estudiantes:
			print (lista_estudiantes[ci])
	def registro(self):
		print("____________________________________")
		print("Estudiantes Registrados en la UPTBAL")
		print("____________________________________")
		if len(lista_estudiantes) == 0:
			print("No se encuentran ningun Estudiante Registrado")
		else:
			print (lista_estudiantes)
	def borrar (self):
		print("________________________________")
		print("Borrar Estudiantes de la UPTBAL ")
		print("________________________________")
		ci=input("Introducir Cedula del Estudiante: ")
		if ci in lista_estudiantes:
			del(lista_estudiantes[ci])
			print("Estudiante Borrado")
		else:
			print("El Estudiante no se Encuentra Registrado")
estudiantes = Estudiante()
estudiantes.menu()