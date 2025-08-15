import requests

def consultar_cep(cep):
    """
    Consulta a API ViaCEP para obter informações de endereço.
    
    Args:
        cep (str): O CEP a ser consultado (apenas números).
        
    Returns:
        dict or None: Um dicionário com os dados do endereço se a consulta for bem-sucedida,
                      ou None se ocorrer um erro ou o CEP não for encontrado.
    """
    
    url_api = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        
        response = requests.get(url_api)
        
        
        if response.status_code == 200:
            dados = response.json()
            
            # A API retorna um campo 'erro' se o CEP não for encontrado
            if 'erro' not in dados:
                return dados
            else:
                print("CEP não encontrado.")
                return None
        else:
            print(f"Erro ao acessar a API. Código de status: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de conexão: {e}")
        return None

# --- Programa principal ---

if __name__ == "__main__":
    cep_input = input("Digite o CEP (somente números): ")
    
    # Valida o formato do CEP
    if len(cep_input) == 8 and cep_input.isdigit():
        dados_endereco = consultar_cep(cep_input)
        
        if dados_endereco:
            print("\n--- Informações do Endereço ---")
            print(f"CEP: {dados_endereco.get('cep', 'N/A')}")
            print(f"Logradouro: {dados_endereco.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados_endereco.get('bairro', 'N/A')}")
            print(f"Cidade: {dados_endereco.get('localidade', 'N/A')}")
            print(f"Estado: {dados_endereco.get('uf', 'N/A')}")
            print("-------------------------------")
    else:
        print("Formato de CEP inválido. Por favor, digite 8 dígitos numéricos.")