def calcular_comissao_humanizado():
    """
    Calcula o total a receber de um vendedor, incluindo salário fixo e 15% de comissão sobre vendas.
    Interage com o usuário de forma mais amigável.
    """
    print("Olá! Vamos calcular o total que um vendedor vai receber neste mês.")
    print("-" * 50) # Apenas uma linha divisória para melhorar a visualização

    # Solicita o nome do vendedor de forma mais amigável
    nome_vendedor = input("Por favor, digite o primeiro nome do vendedor: ")

    # Tenta obter o salário fixo, com tratamento para entradas inválidas
    while True:
        try:
            salario_fixo = float(input(f"Qual é o salário fixo de {nome_vendedor} (em R$)? Ex: 1500.00: "))
            if salario_fixo < 0:
                print("O salário fixo não pode ser negativo. Tente novamente.")
            else:
                break # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o salário.")

    # Tenta obter o total de vendas, com tratamento para entradas inválidas
    while True:
        try:
            total_vendas = float(input(f"E qual foi o valor total das vendas de {nome_vendedor} neste mês (em R$)? Ex: 2500.50: "))
            if total_vendas < 0:
                print("O total de vendas não pode ser negativo. Tente novamente.")
            else:
                break # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o total de vendas.")

    # Calcula a comissão do vendedor (15% sobre o total de vendas)
    comissao = total_vendas * 0.15

    # Calcula o total que o vendedor deverá receber no final do mês
    total_a_receber = salario_fixo + comissao

    print("\n" + "-" * 50) # Outra linha divisória
    print(f"Olá, {nome_vendedor}! Aqui está o resumo do seu pagamento:")
    print(f"  Salário Fixo: R$ {salario_fixo:.2f}")
    print(f"  Comissão (15% sobre R$ {total_vendas:.2f}): R$ {comissao:.2f}")
    print(f"  ----------------------------------------")
    print(f"  Total a Receber: R$ {total_a_receber:.2f}")
    print("-" * 50)
    print("Pagamento calculado com sucesso! Tenha um ótimo dia.")

# --- Chama a função para executar o programa humanizado ---
calcular_comissao_humanizado()