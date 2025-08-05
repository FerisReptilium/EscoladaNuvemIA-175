# Arquivo: processar_logs.py
import pandas as pd
import os

def processar_logs_treinamento(nome_arquivo: str):
    """
    Lê um arquivo CSV de logs de treinamento e calcula a média
    e o desvio padrão do tempo de execução.
    """
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    try:
        df = pd.read_csv(nome_arquivo)

        if 'tempo_execucao' not in df.columns:
            print("Erro: O arquivo não contém a coluna 'tempo_execucao'.")
            return
            
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        
        print("-" * 40)
        print("Análise de tempo de execução:")
        print("-" * 40)
        print(f"Média do tempo de execução: {media_tempo:.2f} segundos.")
        print(f"Desvio Padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos.")
        print("-" * 40)
        
    except Exception as e:
        print(f"Erro inesperado ao processar o arquivo: {e}")

if __name__ == "__main__":
    # Exemplo de arquivo de log, salve como 'log_treinamento.csv'
    # tempo_execucao
    # 15.5
    # 22.1
    # 18.0
    # 19.4
    # 25.8
    
    nome_arquivo = input("Digite o nome do arquivo de log (ex: log_treinamento.csv): ")
    processar_logs_treinamento(nome_arquivo)