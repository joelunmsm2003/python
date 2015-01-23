class MiClase:
	i=12345
	def __init__(self):
		self.datos = []



x=MiClase()

print x


class Perro:

	def __init__(self,nombre):
		self.nombre = nombre
		self.trucos =[]

	def agregar_truco(self,truco):
		self.trucos.append(truco)


d=Perro('Fido')
e=Perro('Buddy')


print e.nombre

d.agregar_truco('girar')
d.agregar_truco('cagar')

print d.trucos
