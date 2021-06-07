import pdb


def divisors(num):
	divisors = []
	pdb.set_trace()
	for i in range(1, num + 1):
		if num % i == 1:
			divisors.append(i)
	return divisors


def main():
	num = int(input('Ingresa un número: '))
	print(divisors(num))
	print('Terminó el programa.')


if __name__ == '__main__':
	main()