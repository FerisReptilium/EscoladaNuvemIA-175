# This is a simple Python script that greets the user with their name and age
nome_usuario = "Feris"
idade_atual = 25
def saudacao():
    print(f"Olá, {nome_usuario}! Você tem {idade_atual} anos.")
    print("Bem-vindo ao nosso programa!")
saudacao()                                          

# exemplos de funções:
def calcular_area_quadrado(lado):
    return lado * lado

def calcular_area_retangulo(base, altura):
    return base * altura
# This script checks if a number is even or odd
def verificar_se_par():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
        else:
            print(f"O número {numero} é ÍMPAR.")
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")