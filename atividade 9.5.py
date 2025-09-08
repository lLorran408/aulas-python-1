numero = []
player = []
print(numero, player)
y = 0
substituição = "s"
while substituição == "s":
  for x in range(0, 11):
    numero = input("digite a camisa: ")
    jogador = input("digite o numero do jogador: ")
    player.append(jogador)
print(numero, player)

saida = input("digite o numero de saida: ")
numero = input("digite o nome da entrada: ")
jogador = input("digite o nome do jogador")

for x in range(0, 11):
    if numero[x] == saida:
        numero[x] = numero
        player[x] = jogador
    else:
        print("nao ha jogadores... ")
y = y + 1
if y == 3:
  substituição = input("deseja substituir mais (s/n): ")

print(numero, player)