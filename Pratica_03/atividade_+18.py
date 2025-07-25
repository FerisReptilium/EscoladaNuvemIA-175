import datetime

# A data de referência é fixada para consistência, conforme sua preferência.
DATA_REFERENCIA = datetime.date(2025, 7, 24)
IDADE_MAIORIDADE = 18

def calcular_idade_completa(data_nascimento):
    """
    Calcula a idade de uma pessoa em anos, meses e dias até a DATA_REFERENCIA.
    Também calcula os anos, meses e dias restantes para atingir a maioridade.

    Args:
        data_nascimento (datetime.date): A data de nascimento da pessoa.

    Returns:
        tuple: (idade_anos, anos_para_maioridade, meses_para_maioridade, dias_para_maioridade)
               Se já for maior de idade, os valores 'para_maioridade' serão 0.
    """
    # Calcula a idade atual em anos
    idade_anos = DATA_REFERENCIA.year - data_nascimento.year
    if (DATA_REFERENCIA.month < data_nascimento.month) or \
       (DATA_REFERENCIA.month == data_nascimento.month and DATA_REFERENCIA.day < data_nascimento.day):
        idade_anos -= 1

    # Verifica se já atingiu a maioridade
    if idade_anos >= IDADE_MAIORIDADE:
        return idade_anos, 0, 0, 0  # Já é maior de idade

    # Se ainda não é maior de idade, calcula o tempo restante
    data_18_anos = datetime.date(data_nascimento.year + IDADE_MAIORIDADE, data_nascimento.month, data_nascimento.day)

    # Calcular a diferença em anos, meses e dias de forma mais limpa
    anos_restantes = data_18_anos.year - DATA_REFERENCIA.year
    meses_restantes = data_18_anos.month - DATA_REFERENCIA.month
    dias_restantes = data_18_anos.day - DATA_REFERENCIA.day

    # Ajustar dias e meses se negativos
    if dias_restantes < 0:
        # Calcular o número de dias no mês anterior à DATA_REFERENCIA
        dias_no_mes_anterior = (DATA_REFERENCIA.replace(day=1) - datetime.timedelta(days=1)).day
        dias_restantes += dias_no_mes_anterior
        meses_restantes -= 1

    if meses_restantes < 0:
        meses_restantes += 12
        anos_restantes -= 1
    
    return idade_anos, anos_restantes, meses_restantes, dias_restantes

def obter_data_nascimento_valida():
    """
    Solicita a data de nascimento ao usuário, valida e retorna um objeto datetime.date.
    """
    while True:
        try:
            print("\n--- Digite a Data de Nascimento ---")
            dia = int(input("Dia (DD): "))
            mes = int(input("Mês (MM): "))
            ano = int(input("Ano (AAAA): "))

            data_nascimento = datetime.date(ano, mes, dia)

            if data_nascimento > DATA_REFERENCIA:
                print("⚠️ Erro: A data de nascimento não pode ser no futuro. Tente novamente.")
            elif data_nascimento.year < (DATA_REFERENCIA.year - 120): # Limite razoável para a vida humana
                print("⚠️ Erro: Ano de nascimento muito antigo. Verifique a data. Tente novamente.")
            else:
                return data_nascimento
        except ValueError:
            print("⚠️ Erro: Entrada inválida. Por favor, digite números inteiros válidos para dia, mês e ano.")
        except OverflowError:
            print("⚠️ Erro: O ano digitado é muito grande ou muito pequeno. Tente um ano mais razoável.")
        except Exception as e:
            print(f"⚠️ Ocorreu um erro inesperado: {e}. Tente novamente.")

def exibir_status_maioridade(idade_atual, anos_restantes, meses_restantes, dias_restantes):
    """
    Exibe a mensagem apropriada sobre a maioridade.
    """
    print("\n--- Resultado da Verificação ---")
    if idade_atual >= IDADE_MAIORIDADE:
        print(f"🎉 Parabéns! Com {idade_atual} anos, você atingiu a maioridade. Seja bem-vindo(a)!")
    else:
        print(f"👶 Você tem {idade_atual} ano(s). Ainda não atingiu a maioridade.")
        if anos_restantes > 0:
            print(f"➡️ Faltam {anos_restantes} ano(s), {meses_restantes} mês(es) e {dias_restantes} dia(s) para a maioridade.")
        elif meses_restantes > 0:
            print(f"➡️ Faltam {meses_restantes} mês(es) e {dias_restantes} dia(s) para a maioridade.")
        else:
            print(f"➡️ Faltam apenas {dias_restantes} dia(s) para a maioridade! Quase lá!")
    print("---------------------------------\n")

def main():
    """
    Função principal que orquestra o fluxo do programa.
    """
    print("✨ Bem-vindo ao Verificador de Maioridade! ✨")
    print(f"Usaremos a data de {DATA_REFERENCIA.day}/{DATA_REFERENCIA.month}/{DATA_REFERENCIA.year} como referência.")

    while True:
        data_nascimento = obter_data_nascimento_valida()
        
        idade_atual, anos_restantes, meses_restantes, dias_restantes = calcular_idade_completa(data_nascimento)
        
        exibir_status_maioridade(idade_atual, anos_restantes, meses_restantes, dias_restantes)
        
        continuar = input("Deseja verificar outra pessoa? (s/N): ").lower()
        if continuar != 's':
            print("👋 Obrigado por usar o verificador! Até a próxima.")
            break

if __name__ == "__main__":
    main()