def calcular_preco_com_desconto(preco_original, percentual_desconto):
    """
    Calcula o preço final de um produto após a aplicação de um desconto.

    Args:
        preco_original (float): O preço original do produto.
        percentual_desconto (float): O percentual de desconto a ser aplicado.

    Returns:
        float: O preço final do produto com o desconto aplicado.
    """
    # Calcula o valor do desconto
    valor_desconto = preco_original * (percentual_desconto / 100)
    
    # Calcula o preço final
    preco_final = preco_original - valor_desconto
    
    return preco_final

# Coleta a entrada do usuário
try:
    preco = float(input("Digite o preço original do produto: "))
    desconto = float(input("Digite o percentual de desconto: "))

    # Chama a função e armazena o resultado
    preco_final_calculado = calcular_preco_com_desconto(preco, desconto)

    # Exibe o preço final formatado com duas casas decimais
    print(f"O preço final com o desconto é de R$ {preco_final_calculado:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")