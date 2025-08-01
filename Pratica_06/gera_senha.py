import random
import string

def gerar_senha(tamanho):
    """
    Gera uma senha aleatória com base no tamanho fornecido.

    Args:
        tamanho (int): O número de caracteres da senha.

    Returns:
        str: A senha gerada.
    """
    # Combina letras, números e caracteres especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha escolhendo aleatoriamente os caracteres
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Bloco try-except para lidar com a entrada do usuário
try:
    tamanho_senha_str = input("Informe o tamanho da senha: ")
    
    # Tenta converter a entrada para um número inteiro
    tamanho_senha = int(tamanho_senha_str)
    
    # Verifica se o tamanho é positivo
    if tamanho_senha <= 0:
        print("Erro: O tamanho da senha deve ser um número positivo.")
    else:
        # Chama a função e imprime a senha
        senha_gerada = gerar_senha(tamanho_senha)
        print(f"Senha gerada: {senha_gerada}")
        
except ValueError:
    # Captura o erro se a entrada não for um número
    print(f"Erro: '{tamanho_senha_str}' não é um número válido. Por favor, digite um número inteiro.")



