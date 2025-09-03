print("vou almoçar em um restaltrante a quilo")

original = ["arroz","feijão","batata","alface","frango"]
print("es, a minha comida", original)
derivada = original[:]
print("meu amigo irá comer também:", derivada)

print("vou alterar as opções de sem ele ver...")
original.remove("arroz")
original.remove("feijão")
original.remove("alface")
original.remove("picanha")
original.remove("linguiça")
print("amiguimho, me mostre o que você vai comer?")
print("claro olá uma conferida", derivada)