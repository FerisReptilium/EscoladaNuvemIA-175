# Arquivo: gerenciar_json.py
import json
import os

def gerenciar_dados_json():
    """
    Escreve dados em um arquivo JSON e depois lê o mesmo arquivo.
    """
    dados_pessoa = {
        "nome": "João",
        "idade": 30,
        "cidade": "Porto Alegre"
    }

    nome_arquivo = 'dados_pessoa.json'

    # 1. Escrevendo os dados no arquivo JSON
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados_pessoa, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados escritos com sucesso no arquivo '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo JSON: {e}")
        return
    
    print("-" * 40)

    # 2. Lendo os dados do arquivo JSON
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_lidos = json.load(arquivo_json)
        
        print("Dados lidos do arquivo 'dados_pessoa.json':")
        print(f"Nome: {dados_lidos['nome']}")
        print(f"Idade: {dados_lidos['idade']}")
        print(f"Cidade: {dados_lidos['cidade']}")
        
    except IOError as e:
        print(f"Erro ao ler o arquivo JSON: {e}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o arquivo JSON: {e}")

if __name__ == "__main__":
    gerenciar_dados_json()