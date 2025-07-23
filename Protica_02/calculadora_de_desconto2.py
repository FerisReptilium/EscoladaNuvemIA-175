nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Calculo do valor do desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)

# Calculo do preço final
preco_final = preco_original - valor_desconto

# Exibir todos os detalhes
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Porcentagem de Desconto: {porcentagem_desconto}%")
print("-" * 30) # Linha separadora
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")