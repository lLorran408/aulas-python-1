print("vou montar a marmita com 5 elemantos")
marmita = ["feijão", "arros", "elgumes", "salada", "carme"]
print("eis a nossa recomendação", marmita)

resposta = input("quer montar uma marmita diferente(s/n)?")
if resposta == "s":
    for x in range(len(marmita)):
       print(f"digite o (x+1)o. item do cardapi:")
       marmita(x) = input()
    print("a marmita montada foi ", marmita)
    print("o três primeiros itens foram", marmita[0:3])
    print("o ultimo item da marmita foi", marmita[-1])
else:
  print("ok você decide...")