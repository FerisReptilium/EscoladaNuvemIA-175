def converter_temperatura_simplificado():
    """
    Função simplificada para converter temperaturas entre Celsius, Fahrenheit e Kelvin.
    O usuário informa a temperatura, a unidade de origem e a unidade de destino.
    Assume entradas válidas para simplificação.
    """
    temperatura = float(input("Digite a temperatura: "))
    unidade_origem = input("Unidade de origem (C, F ou K): ").upper()
    unidade_destino = input("Unidade para qual deseja converter (C, F ou K): ").upper()

    # Se a unidade de origem for igual à de destino, apenas imprime e retorna
    if unidade_origem == unidade_destino:
        print(f"Temperatura: {temperatura:.2f}{unidade_origem}")
        return

    # Converte a temperatura de origem para Celsius como intermediário
    if unidade_origem == 'F':
        celsius = (temperatura - 32) * 5 / 9
    elif unidade_origem == 'K':
        celsius = temperatura - 273.15
    else:  # Assume que a unidade_origem é 'C'
        celsius = temperatura

    # Converte de Celsius para a unidade de destino e imprime
    if unidade_destino == 'F':
        resultado = (celsius * 9 / 5) + 32
        print(f"Temperatura convertida: {resultado:.2f}F")
    elif unidade_destino == 'K':
        resultado = celsius + 273.15
        print(f"Temperatura convertida: {resultado:.2f}K")
    else:  # Assume que a unidade_destino é 'C'
        print(f"Temperatura convertida: {celsius:.2f}C")

# --- Para rodar o programa, a função é chamada aqui ---
converter_temperatura_simplificado()