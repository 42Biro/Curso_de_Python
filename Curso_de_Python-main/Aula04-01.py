"""
Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço sabendo-se que este sofreu um desconto de 10%

"""

print()
print("😊 Olá sou um algoritmo para calcular 10 por cento de esconto no valor de um produto 💰")
print()

dez_por_cento = 0.1
valor_do_produto = float(input("💸 Qual o valor do produto você deseja calcular? = "))
print()
valor_com_desconto = valor_do_produto * dez_por_cento
print()    
print(f'🤑 O valor do produto com desconto de 10% é R${valor_do_produto - valor_com_desconto}')
print()
