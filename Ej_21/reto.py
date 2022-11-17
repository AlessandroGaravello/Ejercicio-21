#Diseña un algoritmo que permita mostrar las
#tablas de multiplicar del 1 al 10

for x in range(11):
	print(f'Tabla de multiplicar del {x}:')
	for y in range(11):
		print(f'{x} x {y} = {x * y}')
	print()