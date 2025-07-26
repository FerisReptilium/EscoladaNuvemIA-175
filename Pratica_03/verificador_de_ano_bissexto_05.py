def verificar_ano_bissexto():
    ano = int(input("Digite o ano para verificar: "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} NÃO é bissexto.")

# Chama a função para executar o verificador
verificar_ano_bissexto()
