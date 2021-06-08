# import pdb


def divisors(num):
	divisors = []
	try:
		if num < 0:
			raise ValueError('El número solo puede ser un número positivo.')
	except ValueError as ve:
		print(ve)
	else:
		# pdb.set_trace()
		for i in range(1, num + 1):
			if num % i == 0:
				divisors.append(i)
	finally:
		return divisors


def main():
	try:
		num = int(input('Ingresa un número: '))
		print(divisors(num))
	except ValueError:
		print('Debes ingresar un número.')
	finally:
		print('Terminó el programa.')


if __name__ == '__main__':
	main()