from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias, baseada no ano de nascimento.
    
    A função considera uma data de nascimento aproximada no primeiro dia do ano.
    
    Args:
        ano_nascimento (int): O ano de nascimento da pessoa.
    
    Returns:
        int: A idade aproximada em dias.
    """
    hoje = date.today()
    data_nascimento_aproximada = date(ano_nascimento, 1, 1)
    diferenca = hoje - data_nascimento_aproximada
    return diferenca.days

# --- Entrada do usuário ---
try:
    ano = int(input("Em que ano você nasceu? "))
    
    # --- Saída para o usuário ---
    dias_vividos = calcular_idade_em_dias(ano)
    print(f"Você tem aproximadamente {dias_vividos} dias de vida.")

except ValueError:
    print("Entrada inválida. Por favor, digite um ano válido (somente números inteiros).")