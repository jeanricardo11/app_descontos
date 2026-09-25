"""""""""""""""""""""""""""""""""""""""""""""""""""
             ***  APP DESCONTO ****
Sistema de Descontos Progressivos para Loja Online
"""""""""""""""""""""""""""""""""""""""""""""""""""

# Apresenta o App ao Usuario
print("Bem Vindo ao Sistema de Descontos !")

# Solicita o valor da compra ao usuário
valor_compra = float(input("Digite o valor da compra (R$): "))

# Define o desconto baseado no valor da compra
match valor_compra:
    case v if v < 200:
        desconto_percentual = 5
    case v if v < 300:
        desconto_percentual = 10
    case _:
        desconto_percentual = 15

# Calcula o valor do desconto
valor_desconto = valor_compra * (desconto_percentual / 100)

# Calcula o valor final a pagar500
valor_final = valor_compra - valor_desconto

# Exibe os resultados

print(f"Você recebeu um desconto de {desconto_percentual}%, no valor de: R$ {valor_desconto:.2f} ")
print(f"Com esse desconto sua compra ficará no valor de: R$ {valor_final:.2f} !")


