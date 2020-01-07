# -*- encoding: utf-8 -*-
#---------------------------------
# Nova ferramenta de Criptografia - Symphony
#---------------------------------
#
# Python 3
#
# Matheus Victor.

# Array com as letras do alfabeto
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]

alfabeto_upper = []

# Cria novo array do alfabeto maiúsculo
for letra in alfabeto:
    alfabeto_upper.append(letra.upper())

for letra_upper in alfabeto_upper:
    print(letra_upper)
