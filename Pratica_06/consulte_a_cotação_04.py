import requests
import datetime

def consultar_cotacao(codigo_moeda):
    """
    Consulta a cotação de uma moeda em relação ao Real Brasileiro (BRL)
    utilizando a AwesomeAPI.

    Args:
        codigo_moeda (str): O código da moeda a ser consultada (ex: 'USD', 'EUR').

    Returns:
        dict or None: Um dicionário com os dados da cotação se a consulta for bem-sucedida,
                      ou None se o ocorrer um erro.
    """
    # A URL da API para a última cotação é montada com o código da moeda
    url_api = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
    
    try:
        response = requests.get(url_api)
        response.raise_for_status()  # Lança uma exceção para códigos de status HTTP 4xx/5xx

        dados = response.json()
        
        # A chave no dicionário JSON é a junção dos códigos das moedas (ex: 'USDBRL')
        chave_cotacao = f"{codigo_moeda}BRL"
        
        if chave_cotacao in dados:
            return dados[chave_cotacao]
        else:
            print(f"Erro: Não foi possível encontrar a cotação para '{codigo_moeda}'.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de conexão: {e}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Erro ao acessar a API: {e}")
        print(f"Verifique se o código da moeda '{codigo_moeda}' está correto.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

# --- Programa principal ---

if __name__ == "__main__":
    moeda_input = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()

    if len(moeda_input) == 3 and moeda_input.isalpha():
        dados_cotacao = consultar_cotacao(moeda_input)
        
        if dados_cotacao:
            # Converte o timestamp UNIX para um objeto datetime
            timestamp = int(dados_cotacao.get('timestamp'))
            data_hora_atualizacao = datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

            print("\n--- Cotação da Moeda ---")
            print(f"Moeda: {dados_cotacao.get('name', 'N/A')}")
            print(f"Valor atual (Compra): R$ {float(dados_cotacao.get('bid', 0)):.4f}")
            print(f"Valor Máximo (dia): R$ {float(dados_cotacao.get('high', 0)):.4f}")
            print(f"Valor Mínimo (dia): R$ {float(dados_cotacao.get('low', 0)):.4f}")
            print(f"Última Atualização: {data_hora_atualizacao}")
            print("------------------------")
    else:
        print("Entrada inválida. Por favor, digite um código de moeda de 3 letras (ex: USD).")