nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Calculo a média
media = (nota1 + nota2 + nota3) / 3

# Arredondar a média para duas casas decimais
media_arredondada = round(media, 2)

# Exibir todas as notas e o resultado final
print(f"Nota 1: {nota1:.1f}") # Formata com uma casa decimal para manter o 7.5
print(f"Nota 2: {nota2:.1f}") # Formata com uma casa decimal para manter o 8.0
print(f"Nota 3: {nota3:.1f}") # Formata com uma casa decimal para manter o 6.5
print("-" * 30) # Linha separadora
print(f"Média Final: {media_arredondada:.2f}")