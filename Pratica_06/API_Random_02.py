import requests

def gerar_perfil_usuario():
    """
    Gera e exibe um perfil de usuário aleatório da API Random User Generator.
    """
    # URL da API
    url_api = "https://randomuser.me/api/"

    try:
       
        response = requests.get(url_api)
        
        
        if response.status_code == 200:
            
            dados_usuario = response.json()
            
            # Extrai as informações relevantes do dicionário
            usuario = dados_usuario['results'][0]
            
            # Nome completo
            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            
            # Email
            email = usuario['email']
            
            # País
            pais = usuario['location']['country']
            
            # Exibe os resultados
            print("--- Perfil de Usuário Aleatório ---")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"País: {pais}")
            print("-----------------------------------")
            
        else:
            print(f"Erro ao acessar a API. Código de status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de conexão: {e}")

# Executa a função para gerar o perfil
gerar_perfil_usuario()