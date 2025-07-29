# Passo 1: Começar um loop que só para quando o cálculo der certo.
while True:
    
    # Passo 2: Tentar pedir os números ao usuário.
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        # Se o usuário digitar letras, este bloco é executado.
        print("\n[ERRO] Você digitou algo que não é um número. Por favor, use apenas números.")
        print("Vamos tentar de novo.\n")
        continue # Volta para o início do loop.

    # Passo 3: Pedir a operação ao usuário.
    operacao = input("Qual operação você quer fazer? (+, -, *, /): ")

    # Passo 4: Fazer o cálculo de acordo com a operação.
    resultado = 0 # Cria a variável de resultado.
    
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        # Verifica se o segundo número é zero ANTES de dividir.
        if num2 == 0:
            print("\n[ERRO] Divisão por zero não é possível.")
            print("Vamos tentar de novo.\n")
            continue # Volta para o início do loop.
        else:
            resultado = num1 / num2
    else:
        # Se o símbolo não for nenhum dos válidos.
        print("\n[ERRO] Operação inválida! Use apenas +, -, * ou /.")
        print("Vamos tentar de novo.\n")
        continue # Volta para o início do loop.

    # Passo 5: Se tudo deu certo, mostrar o resultado e sair.
    print(f"\nO resultado é: {resultado}")
    break # Encerra o loop e o programa.