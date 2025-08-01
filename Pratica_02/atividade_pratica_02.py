valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# Conversão para dólar
valor_dolar = valor_reais / taxa_dolar
valor_dolar_arredondado = round(valor_dolar, 2) # Arredonda para 2 casas decimais

# Conversão para euro
valor_euro = valor_reais / taxa_euro
valor_euro_arredondado = round(valor_euro, 2) # Arredonda para 2 casas decimais

# resultados
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Taxa do dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do euro: R$ {taxa_euro:.2f}")
print("-" * 30) # Linha separadora
print(f"Valor convertido em dólar: US$ {valor_dolar_arredondado:.2f}")
print(f"Valor convertido em euro: € {valor_euro_arredondado:.2f}")