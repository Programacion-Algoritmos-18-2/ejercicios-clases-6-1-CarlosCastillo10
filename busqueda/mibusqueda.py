class BusquedaBinaria(object):

	# Constructor
	def __init__(self, losdatos):
		self.agregar_datos(losdatos)

	# Metodos de agregar
	def agregar_datos(self, losdatos):
		self.datos = losdatos

	# Metodos de obtener
	def obtener_datos(self):
		return self.datos

	# Ordena la lista
	def ordenar(self):

		self.datos.sort()

	# Metodo de busqueda binaria
	def busquedaBinaria(self, elementoBusqueda):
		
		inferior = 0
		superior = len(self.datos) - 1
		medio = int((inferior + superior + 1) / 2)
		ubicacion = -1

		while((inferior <= superior) and (ubicacion == -1)):
			
			if(elementoBusqueda == self.obtener_datos()[medio]):
				ubicacion = medio

			else:
				if(elementoBusqueda < self.obtener_datos()[medio]):
					superior = medio - 1

				else:
					inferior = medio + 1


			medio = int((inferior + superior + 1) / 2)
		

		return ubicacion

	