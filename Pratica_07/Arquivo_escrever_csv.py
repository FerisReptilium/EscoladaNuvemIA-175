# Arquivo: escrever_csv.py
import csv

def escrever_dados_csv():
    """
    Cria e escreve dados em um arquivo CSV com as colunas Nome, Idade e Cidade.
    """
    dados = [
        {'Nome': 'Ana', 'Idade': 25, 'Cidade': 'São Paulo'},
        {'Nome': 'Bruno', 'Idade': 32, 'Cidade': 'Rio de Janeiro'},
        {'Nome': 'Carla', 'Idade': 28, 'Cidade': 'Belo Horizonte'},
    ]

    nome_arquivo = 'pessoas.csv'
    
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            # Define as colunas do cabeçalho
            colunas = ['Nome', 'Idade', 'Cidade']
            writer = csv.DictWriter(arquivo_csv, fieldnames=colunas)
            
            writer.writeheader()  # Escreve o cabeçalho
            writer.writerows(dados)  # Escreve os dados
        
        print(f"Dados escritos com sucesso no arquivo '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro de I/O ao escrever no arquivo: {e}")

if __name__ == "__main__":
    escrever_dados_csv()