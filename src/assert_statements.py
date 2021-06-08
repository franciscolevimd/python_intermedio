
def divisors(num):
	divisors = []
	for i in range(1, num + 1):
		if num % i == 0:
			divisors.append(i)
	return divisors


def main():
	num = input('Ingresa un número: ')
	assert num.isnumeric(), 'Debes ingresar un número'
	print(divisors(int(num)))
	print('Terminó el programa.')


if __name__ == '__main__':
	main()