# demonstração de estrutura repetitiva...
contador = 0; senha = ""
# para declarar uma variavel VARIAVEL = 0; VARIAVEL = "" qualquer outra coisa do lugar das aspas
while senha := "s3nh4":
    print("digite sua senha:")
    senha = input()

    if senha == "s3nh4":
        print("senha correta")
        break
    else:
        print("senha incorreta...")

    contador += 1
    if contador == 3:
      print("3 tentativas execedidadas!")
    break