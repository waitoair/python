# comparativo while e for
x = 1
while (x < 6):
  print (x)
  x = x + 1

for i in range(1, 6, 1):
  print (i)

# --------------------------------------------------

# realize a sequencia de print com for e while:

# a) inteiros de 3 até 12, com 12 incluso de

# o 1 ali no final é o passo unitario, quer dizer que vai de 1 em 1
# no caso ele sempre vai de 1 em 1 se nao botar nada, entao ele pode ser ocultado.

for i in range(3, 13, 1):
  print (i)

# refazendo com while

x = 3
while (x <= 12):
  print (x)
  x += 1

# b) inteiros de 0 até 9, exlcuindo 9, com passo de 2

for i in range(0, 9, 2):
  print(i)

x = 0
while (x < 9):
  print(x)
  x += 2

i = 88
while (i >= 0):
  print(i)
  i -= 4

for i in range(88, -1, -4):
  print(i)

for i in range(10,20):
  for j in range(10, 20, 2):
    print('{} + {} = {}'.format(i, j, i + j))
