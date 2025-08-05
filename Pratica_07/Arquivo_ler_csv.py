# Arquivo: ler_csv.py
import csv
import os

def ler_dados_csv():
    """
    Lê um arquivo CSV chamado 'pessoas.csv' e exibe os dados na tela.
    """
    nome_arquivo = 'pessoas.csv'

    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Execute o script 'escrever_csv.py' primeiro.")
        return

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            reader = csv.DictReader(arquivo_csv)
            
            print("-" * 40)
            print("Conteúdo do arquivo 'pessoas.csv':")
            print("-" * 40)
            
            for linha in reader:
                print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
            
            print("-" * 40)
            
    except IOError as e:
        print(f"Erro de I/O ao ler o arquivo: {e}")

if __name__ == "__main__":
    ler_dados_csv()