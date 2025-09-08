print("eis a teclado numerico do terminal: ")
teclado = [[1,2,3],
           [4,5,6],
           [7,8,9]]
senha  = []
print("digite a sua senha de 4 digitos")
for x in range(0, 4):
    senha.append(int(input(f"digite o digito [x+1]: ")))
for x in range(0, 3):
    for y in range(0, 3):
        for z in range(0, 4):
            if teclado[x][y] == senha[z]:
                teclado[x][y] = 0
print("eis a senha digitada: ", senha)
print("confira as teclas adicionadas ")
for lista in teclado:
    print(lista)