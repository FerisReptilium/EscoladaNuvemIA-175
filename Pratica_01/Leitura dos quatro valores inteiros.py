# Este programa lê quatro valores inteiros (A, B, C, D)
# e calcula a diferença do produto de A e B pelo produto de C e D.

# Solicita e lê o valor de A, exibindo uma mensagem ao usuário
A = int(input("Digite o valor de A: "))

# Solicita e lê o valor de B
B = int(input("Digite o valor de B: "))

# Solicita e lê o valor de C
C = int(input("Digite o valor de C: "))

# Solicita e lê o valor de D
D = int(input("Digite o valor de D: "))

# Calcula a diferença conforme a fórmula: DIFERENCA = (A * B - C * D)
DIFERENCA = (A * B - C * D)

# Imprime o resultado no formato especificado
print("DIFERENCA =", DIFERENCA)
