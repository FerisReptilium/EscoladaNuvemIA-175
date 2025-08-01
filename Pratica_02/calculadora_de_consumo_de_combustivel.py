distancia_percorrida = 300  # em km
combustivel_gasto = 25      # em litros

# Calculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Arredondar o consumo médio para duas casas decimais
consumo_medio_arredondado = round(consumo_medio, 2)

# Exibir todos os dados da viagem e o resultado final
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print("-" * 30) # Linha separadora
print(f"Consumo Médio: {consumo_medio_arredondado:.2f} km/l")