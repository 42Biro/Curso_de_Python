# Concatenação de String f-string
# input ("texto que mostra na tela") -> Função utilizada para:...
# -> Capturar informações da tela, sempre retornará do tipo string, não importa se o usuário informar um número

"""
nome = "Alexsander" 
sobrenome = "Vieira"
idade = 28
print(nome, sobrenome, idade)
print("Bem vindo", nome, sobrenome, "sua idade é de", idade)
print(f"Bem vindo {nome} {sobrenome} sua idade é de {idade})

#----------------------------------------------------------------


print(f"Seja bem-vindo {nome} daqui há 10 anos você terá {idade + 10})

#----------------------------------------------------------------
"""
print()
nome = input("🗒️ Qual o seu nome? = ")
print()
sobre_nome = input("🗒️  Qual o seu sobrenome? = ")
print()
print(f"✨ Olá {nome} {sobre_nome} seja bem-vinde! ✨")
print()
idade = int(input("🎂 Quantos anos você tem? = "))
print()
print(f"😊 Legal! Sabia que daqui há 10 anos você vai ter {idade + 10}anos? ")
print()
emprego = input("🗒️ Você trabalha com o que? (Insira seu cargo) ")
print()
salario = float(input("💰 Quanto você ganha? = "))
print()
print(f"🤨 Se liga {nome} {sobre_nome}, você tá ganhando em média {salario / 20} por dia aos {idade} anos 💰")
print()
novo_salario = float(input("🗒️ Quanto você gostaria de ganhar de aumento? = "))
print()
print(f"📅 Se ano que vem você ainda for um {emprego}, e conseguir o aumento que deseja, vai estar faturando R$ {salario + novo_salario} e vai estar com {idade + 1} anos")
