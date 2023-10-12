# Obtenha a quantidade de dinheiro em reais
valor_em_reais = float(input("Digite o valor em reais: "))

# Defina a taxa de câmbio (por exemplo, 1 real = 0,19 dólar)
taxa_de_cambio = 0.19

# Calcule o valor em dólares
valor_em_dolares = valor_em_reais * taxa_de_cambio

# Exiba o valor convertido
print(f"O valor em dólares é: ${valor_em_dolares:.2f}")
