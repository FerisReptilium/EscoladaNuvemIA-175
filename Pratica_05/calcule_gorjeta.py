def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:

  valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
  return valor_gorjeta


total_conta = float(input("Insira o valor total da conta: "))
porcentagem = float(input("Insira o valor total da gorjeta (%): "))
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R$ {total_conta:.2f}, a gorjeta de {porcentagem:.1f}% é R$ {gorjeta:.2f}")