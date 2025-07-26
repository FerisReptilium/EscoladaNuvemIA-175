def calcular_comissao_detalhada_simples():
    """
    Calcula o total a receber de um vendedor, com mensagens detalhadas para o usuário.
    Não inclui tratamento de erros avançado, assumindo entradas válidas.
    """
    print("Olá! Vamos calcular o total que um vendedor vai receber neste mês.")
    print("-" * 50) # Linha divisória para melhor visualização

    # Solicita o nome do vendedor com uma mensagem clara
    nome_vendedor = input("Por favor, digite o PRIMEIRO NOME do vendedor: ")

    # Solicita o salário fixo com detalhes
    # IMPORTANTE: A entrada DEVE ser um número (ex: 1500.00). Se for texto, o programa dará erro.
    salario_fixo = float(input(f"Qual é o SALÁRIO FIXO de {nome_vendedor} (em R$)? Ex: 1500.00: "))

    # Solicita o total de vendas com detalhes
    # IMPORTANTE: A entrada DEVE ser um número (ex: 2500.50). Se for texto, o programa dará erro.
    total_vendas = float(input(f"E qual foi o VALOR TOTAL DAS VENDAS de {nome_vendedor} neste mês (em R$)? Ex: 2500.50: "))

    # Calcula a comissão do vendedor (15% sobre o total de vendas)
    comissao = total_vendas * 0.15

    # Calcula o total que o vendedor deverá receber no final do mês
    total_a_receber = salario_fixo + comissao

    print("\n" + "-" * 50) # Outra linha divisória para o resultado
    print(f"RESUMO DO PAGAMENTO PARA {nome_vendedor.upper()}:") # Nome em maiúsculas para destaque
    print(f"  Salário Fixo: R$ {salario_fixo:.2f}")
    print(f"  Comissão (15% sobre vendas de R$ {total_vendas:.2f}): R$ {comissao:.2f}")
    print(f"  ----------------------------------------")
    print(f"  TOTAL A RECEBER: R$ {total_a_receber:.2f}")
    print("-" * 50)
    print("Cálculo finalizado! Tenha um ótimo dia.")

# --- Chama a função para executar o programa ---
calcular_comissao_detalhada_simples()