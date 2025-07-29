# 1. Começa a repetição infinita
while True:
    senha = input("Crie uma senha (ou 'sair' para parar): ")

    # 2. Verifica se o usuário quer parar
    if senha == 'sair':
        print("Até logo!")
        break

    # 3. Teste de Tamanho (mínimo 8 caracteres)
    if len(senha) < 8:
        print("-> Senha fraca. Precisa ter no mínimo 8 caracteres.")
        continue # Volta para o começo do loop

    # 4. Teste de Número (precisa ter pelo menos um)
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break 
    if not tem_numero:
        print("-> Senha fraca. Precisa ter pelo menos um número.")
        continue # Volta para o começo

    # 5. Teste de Letra Maiúscula (precisa ter pelo menos uma)
    tem_maiuscula = False
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
            break
    if not tem_maiuscula:
        print("-> Senha fraca. Precisa ter pelo menos uma letra maiúscula.")
        continue # Volta para o começo

    # 6. Teste de Caractere Especial (precisa ter pelo menos um)
    tem_especial = False
    for caractere in senha:
        # .isalnum() verifica se o caractere é letra OU número.
        # Se NÃO for nenhum dos dois, é um caractere especial.
        if not caractere.isalnum():
            tem_especial = True
            break
    if not tem_especial:
        print("-> Senha fraca. Precisa ter um caractere especial (ex: !@#$).")
        continue # Volta para o começo

    # 7. Se passou em TODOS os testes, a senha é forte!
    print("✅ Senha forte e segura! Senha aceita.")
    break # Para o loop, pois a senha é válida