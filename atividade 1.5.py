# atividade 4
p1 = 0; p2 = 1; x = 0
while x <= 2000:
    x = p1 + p2
    p1 = p2
    p2 = x
    if x >= 2000:
        break
    print(x,end=" ")
    