# Solicita a idade ao usuário
idade = int(input("Digite sua idade: "))

# Classifica a idade e imprime a categoria
if 0 <= idade <= 12:
    print("Você é uma Criança.")
elif 13 <= idade <= 17:
    print("Você é um Adolescente.")
elif 18 <= idade <= 59:
    print("Você é um Adulto.")
elif idade >= 60:
    print("Você é um Idoso.")
else:
    print("Idade inválida. Por favor, digite um número positivo.")