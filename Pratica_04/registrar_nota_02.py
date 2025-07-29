# 1. Cria uma lista vazia para guardar as notas
notas = []

print("Digite as notas (0 a 10). Para terminar, digite 'fim'.")

# 2. Inicia o loop para pedir as notas
while True:
    entrada = input("Nota: ")

    # 3. Se a entrada for 'fim', para o loop
    if entrada == 'fim':
        break

    # 4. Tenta converter a entrada para número
    try:
        nota = float(entrada)
    except ValueError:
        print("-> Inválido. Digite um número ou 'fim'.")
        continue # Volta para o começo do loop

    # 5. Verifica se a nota está entre 0 e 10
    if 0 <= nota <= 10:
        notas.append(nota) # Adiciona a nota na lista
        print(f"-> Nota {nota} adicionada.")
    else:
        print("-> Nota fora do intervalo (0-10). Tente de novo.")

# 6. Depois do loop, calcula e mostra a média
print("\n--- Fim ---")

if notas: # Jeito simples de verificar se a lista não está vazia
    media = sum(notas) / len(notas)
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota foi registrada.")