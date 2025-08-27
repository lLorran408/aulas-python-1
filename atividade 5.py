print("digite sua idade")
idade = int(input())
a = "pepa,"
b = "dora,"
c = "luna."
d = "carros do ano,"
e = "copa de clubes,"
f = "placas de video."

if idade >= 18:
    print(d, e, f)
elif idade < 18:
    print(a, b, c)
else:
    print("erro de digitação")

    # jogo de par ou impar
    print("vamos jogar impa ou par, você e par")
    par = 2
    impar = 1 or 3

if par == 3 or 5:
    print("a maquina ganhou")
elif impar == 2 or 4:
    print("você ganhou parabens")
else:
    print("foi impate")

