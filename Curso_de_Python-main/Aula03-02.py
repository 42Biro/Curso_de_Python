# Concatenação de String f-string
# input ("texto que mostra na tela") -> Função utilizada para:...
# -> Capturar informações da tela, sempre retornará do tipo string, não importa se o usuário informar um número

"""
#----------------------------------------------------------------
Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras.
#----------------------------------------------------------------
"""


print()
print("😊 Olá sou um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras 🐎")
print()
quantidade_ferraduras_por_cavalo = 4
quantidade_cavalos = int(input("🗒️ Quantos cavalos você tem? = "))
print()
print(f"🐴 Você vai precisar comprar {quantidade_cavalos * quantidade_ferraduras_por_cavalo} para os seus {quantidade_cavalos} cavalos 🐴")
print()