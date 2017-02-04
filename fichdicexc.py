fd = open("/etc/passwd","r")
lineas = fd.readlines()
fd.close()

diccionario = {}
for linea in lineas:
	login = linea.split(':')[0]
	shell = linea.split(':')[-1][:-1]
	diccionario[login] = shell
	usuario1 = 'root'
	usuario2 = 'imaginario'
try:
	print("Usuario:", usuario1, "Shell:", diccionario[usuario1])
	print("Usuario:", usuario2, "Shell:", diccionario[usuario2])
except KeyError:
	print("el usuario no existe")