# + -> Adição
# - -> Subtração
# * -> Multiplicação
# / -> Divisão
# // -> Divisão Inteira
# % ->
# int() -> Sempre tentar transformar em int
# str() - Sempre tentar transformar e string

print()

"""
ADiÇÃO/SUBTRAÇÃO
"""

print('ADIÇÃO/SUBTRAÇÃO')

print()

print(20 + 10)
print(10.5 + 10.5)
print(10.5 - 5)

print()

"""
MULTIPLICAÇÃO/DIVISÃO
"""

print('MULTIPLICAÇÃO/DIVISÃO')

print()

print(20 * 10)
print(5 / 10.5)
print(40.5 // 10.5)

print()

"""
PORCENTAGEM
"""

print('PORCENTAGEM')

print(20 % 10)
print(5 % 10.5)
print(20.5 % 10.5)
print(9 % 7)

print()

"""
INT()
"""

print('int()')

int('5')
print(type('5'))
print(type(int('5')))
print(type(float('5')))
print(float('5') + int('5'))
print(str(float(int('105'))))
print(int('4') + int('2'))
print(float(int('105')))
print('4' + '2')

print()

"""
VARIÁVEIS
"""

# = -> Atribuição

print('VARIÁVEIS')

idade = 5
idade = '5000'
idade = 35.8
idade = True
cor = str(idade)
print(idade, type(idade))
print(cor, type(cor))

print()

# Soma de Variáveis

numero_primeiro = 2
numero_segundo = '42'
print(numero_primeiro * numero_segundo)
print(float(numero_primeiro + int(numero_segundo)))
print(numero_primeiro + float(numero_segundo))