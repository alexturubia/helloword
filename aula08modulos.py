
# importação de bibliotecas

# from math import sqrt
# num = int(input('Digite um número: '))
# raiz = sqrt(num)

# print('A raiz de {} é {}: '.format(num, raiz))

# Digite um número: 81
# A raiz de 81 é 9.0:

# -----------------------------------------------

# Desafios 16 a 21

# from math import trunc
# num = float(input('Digite qualquer número fracionado: '))
# print('o valor do número {}, e a sua parte inteira é {}'.format(num, trunc(num)))

# Digite qualquer número fracionado: 10.20
# o valor do número 10.2, e a sua parte inteira é 10

# -----------------------------------------------

# Desafios 17

# co = float(input('Comprimento do cateto opposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print('A hipotenusa mede {:.2f}'.format(hi))

# Comprimento do cateto opposto: 2
# Comprimento do cateto adjacente: 2.5
# A hipotenusa mede 3.20

# from math import hypot
# co = float(input('Comprimento do cateto opposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = hypot(co, ca)

# print('A hipotenua mede {:.2f}'.format(hi))

# Comprimento do cateto opposto: 2
# Comprimento do cateto adjacente: 2.5
# A hipotenua mede 3.20

# -----------------------------------------------

# Desafios 18

# import math
# an = float(input('Digite um ângulo: '))
# seno = math.sin(math.radians(an)) 
# cosseno = math.cos(math.radians(an))
# tangente = math.tan(math.radians(an))

# print('Para o angulo {} \nSeu seno é {:.2f} \nseu cosseno é {:.2f} \nsua tangente é {:.2f}'.format(an, seno, cosseno, tangente))

# Digite um ângulo: 45
# Para o angulo 45.0 
# Seu seno é 0.71 
# seu cosseno é 0.71 
# sua tangente é 1.00

# -----------------------------------------------

# Desafios 19

# import random
# a1 = input('Primeiro aluno(a): ')
# a2 = input('Segundo aluno(a): ')
# a3 = input('Terceiro aluno(a): ')
# a4 = input('Quarto aluno|(a): ')
# lista = [a1, a2, a3, a4]
# escolha = random.choice(lista)
# print('O Aluno escolhido foi {}'.format(escolha))

# Primeiro aluno(a): Pedro
# Segundo aluno(a): Alex
# Terceiro aluno(a): Maria
# Quarto aluno|(a): Ana
# O Aluno escolhido foi Maria

# -----------------------------------------------

# Desafios 20

# import random
# a1 = input('primeiro: ')
# a2 = input('segundo: ')
# a3 = input('terceiro: ')
# a4 = input('quarto: ')

# lista = [a1, a2, a3, a4]
# random.shuffle(lista)
# print(lista)

# primeiro: Alex
# segundo: Vanessa
# terceiro: Matheus
# quarto: Benicio 

# -----------------------------------------------

# Desafios 20 (Tocando Mp3)



