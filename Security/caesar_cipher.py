# -*- encoding: utf-8 -*-

#--------------------------------------------#
# Python 3
#
# Matheus Victor.
#--------------------------------------------#
#
# Base de criptografia => Cifra de Cesar 
#
#--------------------------------------------#

# Imports
import sys	# Pacotes de argumentos do sistema

# Variáveis
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ROT = 13

# Criptografa
def encrypt(message):
	crypt_character = ''
	for character in message:
		if character in ALPHABET:
			character_index = ALPHABET.index(character) # Verifica qual o indice em relação ao alfabeto
			crypt_character += ALPHABET[(character_index + ROT) % len(ALPHABET)] # faz a rotação
		else:
			crypt_character += character
	print(crypt_character)

# Descriptografa
def decrypt(message):
	crypt_character = ''
	for character in message:
		character_index = ALPHABET.index(character) # Verifica qual o indice em relação ao alfabeto
		crypt_character += ALPHABET[(character_index - ROT) % len(ALPHABET)] # faz a rotação
	print(crypt_character)

# Função principal
def main():
	command = sys.argv[1].lower()
	message = sys.argv[2].lower()
	
	if command == 'encrypt':
		encrypt(message)
	elif command == 'decrypt':
		decrypt(message)

if __name__ == '__main__':
	main()
	
