# le dois valores inteiros e compara ambos
x = int(input("digite um valor inteiro: "))
y = int(input("digite um segundo valor inteiro: "))

if (x > y):
  print('O primeiro valor é maior que o segundo!')

# par ou impar
x = int(input("Digite um valor inteiro: "))
if (x % 2 == 0):
  print("O numero é par!")
else:
  print("O numero é impar!")

x = 10
y = 1
z = 5.5

print(x > y or z == y)
print(x != y and not (z == y))
print(x < y or z == y and z == 5.4)

# --------------------------------------------------
a + b > c and b - c >= 0
# -------------------------------------------------
print(1 / (2 + 3) + (1 + 4) / 2)
# --------------------------------------------------

x = 2
y = 5
z = 0

valor = int(input("Digite 1, 2 ou 3: "))

if (valor ==1):
  print(x * valor)
else:
  if (valor == 2):
    print(y * valor)
  else:
    if (valor == 3):
      print(z * valor)
    else:
      print("Voce digitou um valor invalido!")
