# Testes com while e break

contador = 1

while contador <= 10:
    print(contador)
    contador = contador + 1
    if contador == 6:
        print('Gotcha!')
        continue
    print('Pin')

# Outro exemplo
print()
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result

# Exemplo com else
print()
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
