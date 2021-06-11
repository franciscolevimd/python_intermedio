import random
import os
import re

HANGMANPICS = [
'''
  +---+
  |   |
      |
      |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
, '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

KEY_WORD = 'word'
KEY_HIDDEN_WORD = 'hidden_word'
SPECIAL_CHARACTERS = [',',';','.',' ']
VOWELS = {
	'Á':'A',
	'A':'A',
	'É':'E',
	'E':'E',
	'Í':'I',
	'I':'I',
	'Ó':'O',
	'O':'O',
	'Ú':'U',
	'U':'U',
	'Ü':'U',
}
MESSAGE_LETTER_USED = 'YA HAS USADO ESA LETRA, INTENTA CON OTRA'
MESSAGE_USE_ABC_LETTER = 'DEBES ESCRIBIR UNA LETRA DEL ABECEDARIO'


def load_countries():
	"""Loads a list of country names from a text file.

	Returns: 
		list - List of countries.
	"""
	with open('./files/countries.txt','r', encoding='utf-8') as f:
		return [country[:-1].upper() for country in f]


def random_country():
	"""Retrieve a random country name.

	Returns: 
		str - Country name.
	"""
	return random.choice(load_countries())


def get_game_word():
	"""Retrieves the playing word and the same word but in hidden.

	The hidden word is represented with underscore for each letter.

	Returns:
		dict - Contains the clear word and the hidden word.
	"""
	country = random_country()
	return {
		KEY_WORD:list(country)
		, KEY_HIDDEN_WORD: [character if character in SPECIAL_CHARACTERS else '_' for character in country]
	}


def display_warning(message):
	"""
	"""
	print('X' * 100)
	print(f'¡{message.upper()}!')
	print('X' * 100)


def find_letter(word, letter):
	"""
	"""
	found = False
	hidden_word = word.get(KEY_HIDDEN_WORD)
	clear_word = word.get(KEY_WORD)	
	for i in range(0, len(clear_word)):
		clear_letter = clear_word[i]
		if VOWELS.get(clear_letter, None) and VOWELS.get(clear_letter) == letter:
			hidden_word[i] = clear_letter
			found = True
		elif clear_letter == letter:
			hidden_word[i] = letter
			found = True
	return found


def board(word):
	"""
	"""
	attempts = 0
	used_letters = []
	while True:
		print(HANGMANPICS[attempts])
		for hidden_letter in word.get(KEY_HIDDEN_WORD):
			print(hidden_letter, end=' ')
		letter = input('\n\nEscribe una letra: ').upper()
		os.system('clear')
		if letter == '.':
			break
		elif letter in used_letters:
			display_warning(MESSAGE_LETTER_USED)
		elif re.search('[A-ZÑ]', letter) is None:
			display_warning(MESSAGE_USE_ABC_LETTER)
		else:
			if not find_letter(word, letter):
				attempts += 1				
				if attempts >= len(HANGMANPICS) - 1:
					print(f'HAS PERDIDO =(')
					print(HANGMANPICS[attempts])
					print(f'La palabra es: {"".join(word.get(KEY_WORD))}')
					input('Presiona cualquier letra para terminar')
					break
			elif '_' not in word.get(KEY_HIDDEN_WORD):
				print(f'¡FELICIDADES, HAS GANADO!')
				print(f'La palabra es: {"".join(word.get(KEY_WORD))}')
				input('Presiona cualquier letra para terminar')
				break
			used_letters.append(letter)
		if len(used_letters) > 0:
			print(f'Letras usadas: {"".join(used_letters)}')


def main():
	os.system('clear')
	board(get_game_word())


if __name__ == '__main__':
	main()