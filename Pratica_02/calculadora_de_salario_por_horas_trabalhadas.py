print("Digite o número do funcionário:")
numero_funcionario = int(input())

# Quantidade de horas trabalhadas (inteiro)
print("Digite a quantidade de horas trabalhadas:")
horas_trabalhadas = int(input())

# Valor recebido por hora (flutuante, com duas casas decimais)
print("Digite o valor que o funcionário recebe por hora (ex: 15.50):")
valor_por_hora = float(input())

# 2. Calcular o salário do funcionário
salario = horas_trabalhadas * valor_por_hora

# 3. Exibir o resultado formatado corretamente
print("-" * 30) # Linha separadora
print(f"Número do Funcionário: {numero_funcionario}")
print(f"Salário: R$ {salario:.2f}") # Formata o salário com duas casas decimais