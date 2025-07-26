def calcular_media_aluno():
    # Lê as quatro notas
    N1, N2, N3, N4 = map(float, input().split())

    # Calcula a média ponderada
    media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / (2 + 3 + 4 + 1)

    print(f"Media: {media:.1f}")

    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else: # media >= 5.0 e media < 7.0
        print("Aluno em exame.")
        nota_exame = float(input())
        print(f"Nota do exame: {nota_exame:.1f}")

        media_final = (media + nota_exame) / 2

        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f"Media final: {media_final:.1f}")

# Chama a função para executar a calculadora de média
# calcular_media_aluno()