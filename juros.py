capitalInicial = float(input("Digite o seu capital inicial: "))
taxaJuros = float(input("Digite a taxa de juros:"))
aplicaçãoTempo = float(input("Digite o tempo de aplicação:"))

juros = capitalInicial * taxaJuros * aplicaçãoTempo
print(f"O seu juros simples é {juros}")