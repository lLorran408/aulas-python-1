print("eis a tecla numerica original")
tabuada = [[1,2,3],
           [4,5,6],
           [7,8,9]]
multiplicador = int(input("digite o multiplicador: "))

for x in range(0, 3):
    for y in range(0, 3):
      tabuada[x][y] = tabuada[x][y] * multiplicador
print("eis o multiplicador", multiplicador)
print("confira o ressultado das operações")
for resltado in tabuada:
    print(resltado)