# OPERADORES ARITIMÉTICOS
#  + adição
# - subitração
# * multiplição
# / divisão
# ** potência
# // divisão inteira
# % resta da divisão

# Ordem de Precedência
# 1º []
# 2º **
# 3º *  /  //  % 
# 4º + e -

# print(int(5+3*2))
# print(int(3*5+4**2))

# print(int(3*(5+4)**2))

#  Raiz quadra 

# print(int(81**(1/2)))
# print(int(25**(1/2)))

# nome = input('Qual é o seu nome?: ')
# print('prazer em te conhecer {:^20}!'.format(nome))

# n1=int(input('Digite um númeor: '))
# n2=int(input('Digite outro número: '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# d1 = n1 // n2
# e = n1 ** n2

# print('A soma vale: {} o produto é {} a divisão é {:.3f}'.format(s, m, d), end=' ')
# print('A divisão inteira e {} e a potencia é {}'.format(d1,e))

# Exercicios

#  Exercicio 05
# n1 = int(input('Digite um número: ' ))
# n2 = n1-1
# n3 = n1+1
# print('Analisando o valor {} o antecessor é {} e o sucessor é {}'.format(n1,n2,n3))

# ou print('Analisando o valor {} o antecessor é {} e o sucessor é {}'.format(n1,(n1-1),(n1+1))) (sem as variáveis n2 e n3)

#  Digite um número: 2
# Analisando o valor 2 o antecessor é 1 e o sucessor é 3

# ------------------------------------------------------------------------------------

# Exercicio 06

# n1 = int(input('Digite um número: '))
# print('Dobro de {} vale {}'.format(n1, (n1*2)))
# print('O triplo de {} vale {}'.format(n1, (n1*3)))
# print('A raiz quadrade {} vale {:.2f}'.format(n1, (n1**(1/2))))

# Digite um número: 18
# Dobro de 18 vale 36
# O triplo de 18 vale 54
# A raiz quadrade 18 vale 4.24

# ----------------------------------------------------------------------------------------------

#  Exercicio 07

# p1 =float(input('Primeira nota:  '))
# p2 =float(input('Segunda Nota:  '))

# print("A média entre {:.1f}, e {:.1f} é {:.1f}".format(p1, p2, ((p1+p2)/2)))

# Primeira nota:  5.5
# Segunda Nota:  2
# A média entre 5.5, e 2.0 é 3.8

# -------------------------------------------------------------------------------------

#  Exercicio 08

# m = float(input('Distância: '))
# a = m/1000
# b = m/100
# c = m/10
# d = m*10
# e = m*100
# f = m*1000

# print('A média de {} metros correspondem a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m, a, b, c, d, e, f))

# Distância: 3
# A média de 3.0 metros correspondem a 
# 0.003km 
# 0.03hm 
# 0.3dam 
# 30dm 
# 300cm 
# 3000mm

# -------------------------------------------------------------------------------------

#  Exercicio 09

# t = int(input('Digite um número para ver sua tabulada:  '))
# print('-------'*8)
# print('{} X {:2} = {}'.format(t, 1, t*1))
# print('{} X {:2} = {}'.format(t, 2, t*2))
# print('{} X {:2} = {}'.format(t, 3, t*3))
# print('{} X {:2} = {}'.format(t, 4, t*4))
# print('{} X {:2} = {}'.format(t, 5, t*5))
# print('{} X {:2} = {}'.format(t, 6, t*6))
# print('{} X {:2} = {}'.format(t, 7, t*7))
# print('{} X {:2} = {}'.format(t, 8, t*8))
# print('{} X {:2} = {}'.format(t, 9, t*9))
# print('{} X {} = {}'.format(t, 10, t*10))
# print('-------'*8)

# --------------------------------------------------------
# 6 X  1 = 6
# 6 X  2 = 12
# 6 X  3 = 18
# 6 X  4 = 24
# 6 X  5 = 30
# 6 X  6 = 36
# 6 X  7 = 42
# 6 X  8 = 48
# 6 X  9 = 54
# 6 X 10 = 60
# --------------------------------------------------------

#  Exercicio 10

# real = float(input('Valor em reais: '))
# dolar = real / 4.90
# print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))

# Valor em reais: 5.20
# Com R$5.20 você pode comprar U$1.06

# ---------------------------------------------------------------------

#  Exercicio 11

# largura = (float(input('largura em metros da parede: ')))
# altura = (float(input('Altura em metros da parede: ')))
# Metros = largura * altura
# Litros = 2

# # print('essa parede tem {} Metros qudrados'.format(Metros))
# print('Para pintar uma parece de {:.2f} metros voce precisa de {:.2f} litros de tinta'.format(Metros, (Metros/Litros)))

# ---------------------------------------------------------------------

#  Exercicio 12

# valor =float(input('Digite o valor R$: '))
# novo = valor - (valor * 5 / 100)

# print('Seu desconto no produto é de R${}'.format(novo))

# Digite o valor R$: 100
# Seu desconto no produto é de R$95.0

# ---------------------------------------------------------------------

#  Exercicio 13

# salario =float(input('Seu salário atual é de R$:  '))
# reajuste = salario + (salario * 15 / 100)

# print ('Seu salário atual de R${:.2f} com o reajuste de 15% ficará R${:.2f}'.format(salario, reajuste))

# Seu salário atual é de R$:  1000.00
# Seu salário atual de R$1000.00 com o reajuste de 15% ficará R$1150.00

# ---------------------------------------------------------------------

#  Exercicio 15

km = float(input('KM: '))
dias = float(input('dias: '))
kilometros = km * 0.15
carro = dias * 60
pagar = kilometros + carro

print('Você rodou {} Kms em { } dias e deve pagar R${}'.format(km, dias, pagar))

