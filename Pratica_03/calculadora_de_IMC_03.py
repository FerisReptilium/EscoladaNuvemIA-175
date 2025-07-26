# Solicita o peso ao usuário (em kg)
peso = float(input("Digite seu peso em kg (ex: 70.5): "))

# Solicita a altura ao usuário (em metros)
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# Calcula o IMC
# Fórmula: IMC = peso / (altura * altura)
imc = peso / (altura ** 2)

# Classifica o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Imprime o IMC e a classificação
print(f"Seu IMC é: {imc:.2f}") # Formata o IMC com 2 casas decimais
print(f"Classificação: {classificacao}")