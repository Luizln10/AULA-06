nota = float(input("Digite uma nota de 0 a 100:"))

if nota >= 90:
  print("A")
elif nota >= 80 and nota <= 89:
  print("B")
elif nota >= 70 and nota <= 79:
  print("C")
elif nota >= 60 and nota <= 69:
  print("D")
else:
  print("F")