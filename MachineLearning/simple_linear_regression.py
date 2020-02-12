# -*- encoding: utf-8 -*-

'''
 Calculo simples de regressão linear

    - Uma empresa resolveu estudar a variação de demanda de seu produto em função do preço
    de venda praticado.


 Python 3+.
 DevBy Matheus Victor.

'''

# Dataset
precox = [36, 43, 49, 55, 61, 63, 69, 72, 74, 77]
demanday = [350, 330, 296, 252, 230, 218, 203, 196, 188, 167]

# Variáveis de atribuição
xquandrado_array = []
yquadrado_array = []
xy_array = []

somatoriax = 0
somatoriay = 0
xquandrado_total = 0
yquadrado_total = 0
xy_total = 0

contador = 0

# Percorre o array de preços e faz a somatoria
for preco, demanda in zip(precox, demanday):

    # Calculando a somatória de x e y
    somatoriax += preco
    somatoriay += demanda
    xy_array.append(preco * demanda)

    # Inclui nos array de calculos de elevação ao quadrado
    xquandrado_array.append(preco**2)
    yquadrado_array.append(demanda**2)

    contador += 1

# Calcula o total dos x e y ao quadrado
for xquadrado, yquadrado in zip(xquandrado_array, yquadrado_array):
    xquandrado_total += xquadrado
    yquadrado_total += yquadrado

for xy in xy_array:
    xy_total += xy

# Exibição das variáveis
print("Somatória de X: ", somatoriax)
print("Somatório de y: ", somatoriay)
print("Somatória de x ao quadrado: ", xquandrado_total)
print("Somatŕoia de y ao quadrado: ", yquadrado_total)

# Calculo de regressão
r_cima = (contador * xy_total) - (somatoriax * somatoriay)
r_baixo = (((contador * xquandrado_total) - somatoriax**2) * ((contador * yquadrado_total) - somatoriay**2)) ** 0.5

r = r_cima/r_baixo

print(r)
