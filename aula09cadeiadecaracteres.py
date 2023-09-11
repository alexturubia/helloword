# Cadeia de caracteres

# frase = ('Curso em Vídeo Python')
# print(frase[9::3])

#Análise de string quantos caracteres
# print(len(frase))

# quantidades de letras iguais na frase
# print(frase.count('o'))

#contagem com fatiamento 
# print(frase.count('o',0,14))

# início da contagem do caracteres de um trecho de texto
# print(frase.find('deo'))

# localização de palavra dentro da frase
# print('curso'in frase)

#tranformação de frase

# print(frase.replace('python','alex')) subistii palavra

# print(frase.upper()) tranformar tudo em maiúscula

# print(frase.lower()) tranformar tudo em minuscula

# print(frase.capitalize()) tranformar apenas a primeira letra em maíscula

# print(frase.title()) tranformar todas as primeiras letra em maíscula

# frase =('   Aprenda Python  ')

# print(frase.strip()) Remove espaços anteriores e posteriores

# print(frase.rstrip()) Remove espaços posteriores

# print(frase.lstrip()) Remove espaços anteriores

# frase = ('Curso em Vídeo Python')

# print(frase.split()) separar as palavras da frase criando uma divisão de caracteres (novos índices)

# print(''.join(frase)) junta as palavras fromando um frase única

# print(frase[3])  Localiza a letra do caracter (S posição 3)

# print(frase[3:13]) so em Víde

# print(frase[3:13:2]) seleciona e pula letras de 2 em 2

# -----------------------------------------------------------
# desafíos 22 a 27

# Exercício 22

# n = str(input('Digite seu nome completo: ')).strip()

# print('Seu nome em letras maiúscula é: {}'.format(n.upper()))
# print('Seu nome em letras minúscula é: {}'.format(n.lower()))
# print('Seu nome completo tem {} letras'.format(len(n) - n.count(' ')))
# separa = n.split()
# print('Seu primeiro nome é: {}, e tem {} letras'.format(separa[0], len(separa[0])))

# Digite seu nome completo: Maria Jose
# Seu nome em letras maiúscula é: MARIA JOSE
# Seu nome em letras minúscula é: maria jose
# Seu nome completo tem 9 letras
# Seu primeiro nome é: Maria, e tem 5 letras

# -----------------------------------------------------------------------------------------
# Exercício 22

# num = int(input('Digite um número de 0 à 9999: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10

# print('Analisando o numero {}'.format(num))
# print('Sua unidade é: {}'.format(u))
# print('Sua dezena é: {}'.format(d))
# print('Sua centena é: {}'.format(c))
# print('Sua milhar é: {}'.format(m))

# Digite um número de 0 à 9999: 12
# Analisando o numero 12
# Sua unidade é: 2
# Sua dezena é: 1
# Sua centena é: 0
# Sua milhar é: 0

# -----------------------------------------------------------------------------------------
# Exercício 24

cid = ('Cidade')