# Importamos las diferentes clases de los distintos paquetes
from paquete_archivos.miarchivo import MiArchivo
from busqueda.mibusqueda import BusquedaBinaria


# Creamos los objetos de la clase mi archivo
m1 = MiArchivo()

lista1 = m1.obtener_informacion() # Guardamos en lista1 lo que retorna el metodo 'obtener informacion'
lista1 = [x.split(",") for x in lista1] # Delimitamos por comas la lista

listado_enteros = []
elementoBuscar = 3

for x in lista1:
	for y in x:
		listado_enteros.append(int(y)) # convertimos a entero cada posicion de la sublista

# Creamos el objeto de tipo BusquedaBinaria
busqueda = BusquedaBinaria(listado_enteros)
busqueda.ordenar()

# Guardamos lo que retorna el metodo
ubicacion = busqueda.busquedaBinaria(elementoBuscar)

# Condicion que permite saber si se encontro o no el elemento
if(ubicacion == -1):
	print("\nEl elemento %d no ha sido encontrado" %(elementoBuscar))
else:
	print("\nEl elemento %d ha sido encontrado en la posicion %d\n" %(elementoBuscar, ubicacion))




