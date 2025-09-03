# demostração de metodo em lista
inss = ["Maria", "manoel" ,"josé", "Isabel"]
print("eis a fila do inss;" , inss)
novo = input("insira mais uma pessoa: ")
inss.append(novo)
print("conferindo nova lista", inss)

print("vou tirar uma pessoa da lista...")
especial = inss.pop()

print("agora vou colocá-lo na frente de todos")
inss.insert(0, especial)
print("confirindo a lista", inss)
print("Maria não gostou e reclamou...")
inss.remove("Maria")
print("agora Maria saiu pê da vida", inss)
print("para não ter mais reclamaçõe vamos a lista:", inss)
inss.sort()
print("...em ordem alfabetica", inss)

print("onde esta nava pessoa chamada", especial)
print("ela agora na posição", inss.index(especial)+1)