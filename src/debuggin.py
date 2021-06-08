# import pdb


def divisors(num):
	divisors = []
	# pdb.set_trace()
	for i in range(1, num + 1):
		if num % i == 1:
			divisors.append(i)
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