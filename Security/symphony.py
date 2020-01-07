# -*- encoding: utf-8 -*-
#--------------------------------------------#
# Nova ferramenta de Criptografia - Symphony #
#--------------------------------------------#
#
# Python 3
#
# Matheus Victor.

# Entrada
valor = input('[+] Entre com algum valor...: ')

# Arrays com caracteres de criptografia
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]
alfabeto_upper = []
numeros = [1,2,3,4,5,6,7,8,9]
specials = ['@',',','/','#','(',')','?','-',';','^','[',']','~','{','}','"','`','$','%','&','*']

# Cria novo array do alfabeto maiúsculo
for letra in alfabeto:
    alfabeto_upper.append(letra.upper())

# Encontra as letras do alfabeto no valor
for letra in alfabeto:
	if valor.find(letra) >= 0:
		print("Letras", letra ,"encontradas na posição...: ",valor.find(letra))


