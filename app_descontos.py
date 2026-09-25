"""""""""""""""""""""""""""""""""""""""""""""""""""""
             ***  APP DESCONTO ****
Sistema de Descontos Progressivos para Loja Online
"""""""""""""""""""""""""""""""""""""""""""""""""""""
#Apresenta o App ao Usuario
print ("Bem Vindo ao Sistema de Descontos !")
# Solicita o valor da compra ao usuário
valor_compra = float(input("Digite o valor da compra(R$):"))

# Define o desconto baseado no valor da compra
if valor_compra < 200:
    desconto_percentual = 5
elif valor_compra < 300:
    desconto_percentual = 10
else:
    desconto_percentual = 15

# Calcula o valor do desconto
valor_desconto = valor_compra * (desconto_percentual / 100)

# Calcula o valor final a pagar
valor_final = valor_compra - valor_desconto

# Exibe os resultados

print("Você recebeu")
print(f"Desconto ({desconto_percentual}%): R$ {valor_desconto:.2f} de desconto")
print(f"Com esse desconto sua compra ficará nop valor de: R$ {valor_final:.2f} !")

