# lista de tarefas
tarefas = ["1 limpar a casa",
           "2 molhar as plantas",
           "3 lavar a lousa",
           "4 passear com cachorro",
           "5 arrumr o quintal"]
print(tarefas)
print(" vc ja limpou a casa (s/n)")
resposta = input()
resposta2 = input()
if resposta == "s":
    tarefas.remove("1 limpar a casa")
    print("1 tarefa retirada da lista")
    print(tarefas)
else:
    print("ainde a tarefas a serem feitas", tarefas)
if resposta2 == "s":
    tarefas.remove("2 molhar as plantas")
    print("1 tarefa retirada da lista")
    print(tarefas)
else:
    print("ainde a tarefas a serem feitas", tarefas)
