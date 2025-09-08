tabuada = []

for x in range(1, 10):
    linha = []
    for y in range(1, 10):
      linha.append(x * y)
tabuada.append(linha)

for tabuada in tabuada:
    print(tabuada)