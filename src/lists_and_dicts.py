def main():
	my_list = [1, 'Sakura', True, 4.5]
	my_dict = {'firstname':'Francisco', 'lastname':'Méndez'}

	super_list = [
	    {'firstname':'Francisco', 'lastname':'Méndez'}, 
	    {'firstname':'Sakura', 'lastname':'Kinomoto'}, 
	    {'firstname':'Jessica', 'lastname':'Ángeles'}, 
	    {'firstname':'Juan', 'lastname':'Zepeda'}, 
	]

	super_dict = {
	    'naturla_nums':[1, 2, 3, 4, 7],
	    'integer_nums':[-1, -2, 0, 1, 2],
	    'floating_nums':[1.1, 4.5, 6.43],
	}

	for key, value in super_dict.items():
		print(key, '-', value)

	for value in super_list:
		print(value)


if __name__ == '__main__':
	main()