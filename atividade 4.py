# atividade 
def adiçao(x,y):
    w = x + y
    return w
def subtraçao(x,y):
    return x - y
print("digite dois valores internos...")
n1 = int(input("x: "))
n2 = int(input("y: "))
OP = input("qualquer operação(+ ou -)")
if OP == "+":
    z = adiçao(n1, n2)
    print("resultado da soma", z)
elif OP == "-":
    z = subtraçao(n1, n2)
    print("resultado", z)
else:
    print("operação digitada inesistente!")