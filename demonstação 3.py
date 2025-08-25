# demonnstração do uso de estudo repetitiva...
numero = 1
while numero >= 0:
    print("digite um numero negativo para sair:")
    numero = int(input())
    #caso o break estaja aqui o testo e todo abaixo não sera exibido.
    continue
    print("este testo não sera exibido mas...")
else:
    print("o numero digitado foi ", numero)