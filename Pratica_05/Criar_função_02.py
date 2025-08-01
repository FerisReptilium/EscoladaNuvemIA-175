def eh_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    
    A função ignora espaços, pontuações e acentuações para a verificação.
    
    Args:
        texto (str): A string a ser verificada.
    
    Returns:
        bool: True se for um palíndromo, False caso contrário.
    """
    import unidecode
    
    # Converte o texto para minúsculas e remove acentuações
    texto_limpo = unidecode.unidecode(texto).lower()
    
    # Filtra apenas letras e números
    caracteres_limpos = [char for char in texto_limpo if char.isalnum()]
    
    # Junta os caracteres para formar a string final
    string_limpa = "".join(caracteres_limpos)
    
    # Compara a string limpa com sua versão invertida
    return string_limpa == string_limpa[::-1]

# Exemplos de uso:
# Exemplo 1: "A base do teto desaba"
if eh_palindromo("A base do teto desaba"):
    print("Sim")
else:
    print("Não")

# Exemplo 2: "Socorram-me, subi no onibus em marrocos"
if eh_palindromo("Socorram-me, subi no onibus em marrocos"):
    print("Sim")
else:
    print("Não")

# Exemplo 3: "Olá, mundo"
if eh_palindromo("Olá, mundo"):
    print("Sim")
else:
    print("Não")