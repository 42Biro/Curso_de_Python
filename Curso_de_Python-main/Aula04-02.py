"""
A padaria Hortpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
Cada pãozinho custa R$ 0.12 e a broa custa R$ 1.50.
Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado).
Você foi contratado para fazer os cálculos para o dono.
Com base nesses fatos, faça um algoritmo para ver as quantidades de pães e de broas e depois calcular os dados solicitados.

"""

print()
print("😊 Olá sou um algoritmo para calcular quanto a Hortpão vendeu de pães e broas por dia 🍞")
print()
valor_pao = 0.12
valor_broa = 1.50
paes_vendidos = int(input("🍞 Quantos pães foram vendidos hoje? = "))
print()
print(f'🤑 Se liga! Você faturou R$ {paes_vendidos * valor_pao} vendendo pão hoje')
print()
broas_vendidas = int(input("🍞 Quantas broas foram vendidas hoje? = "))
print()
print(f'🤑 Se liga! Você faturou R$ {broas_vendidas * valor_broa} vendendo broa hoje')
print()
valor_total_paes = paes_vendidos * valor_pao
valor_total_broas = broas_vendidas * valor_broa
valor_total_vendido = valor_total_paes + valor_total_broas
dez_por_cento = 0.1
valor_com_desconto = valor_total_vendido * dez_por_cento
print(f'🍞 O valor total de pães e broas vendidas foi de R$ {valor_total_vendido} e os 10% arrecadados na poupança é de R${valor_com_desconto} 💰')
print()
