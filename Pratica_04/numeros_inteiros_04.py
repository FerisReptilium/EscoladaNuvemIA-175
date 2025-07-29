# 1. Inicia os contadores para pares e ímpares em zero.
numeros_pares = 0
numeros_impares = 0

print("--- Contador de Números Pares e Ímpares ---")
print("Digite números inteiros um por um. Para encerrar, digite 'fim'.\n")

# 2. Inicia um loop infinito para solicitar os números.
while True:
    entrada_usuario = input("Digite um número ou 'fim': ")

    # 3. Verifica se o usuário quer encerrar o programa.
    if entrada_usuario.lower() == 'fim':
        break # Interrompe o loop e vai para a parte final do código.

    # 4. Tenta converter a entrada para um número inteiro.
    try:
        numero = int(entrada_usuario)

        # 5. Se a conversão funcionou, verifica se é par ou ímpar.
        # O operador '%' calcula o resto de uma divisão.
        if numero % 2 == 0:
            print(f"-> O número {numero} é PAR.")
            numeros_pares += 1 # Adiciona +1 ao contador de pares.
        else:
            print(f"-> O número {numero} é ÍMPAR.")
            numeros_impares += 1 # Adiciona +1 ao contador de ímpares.

    except ValueError:
        # 6. Se a conversão para inteiro falhou, informa o erro.
        print(f"-> Erro: '{entrada_usuario}' não é um número inteiro. Tente novamente.")


# 7. Após o loop terminar, exibe o resumo final.
print("\n--- Programa Finalizado ---")
print(f"Total de números PARES inseridos: {numeros_pares}")
print(f"Total de números ÍMPARES inseridos: {numeros_impares}")