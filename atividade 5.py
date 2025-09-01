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


def soma(par,impar):
    soma = (par + impar) % 2
    return soma
import random
par = int(input("par: "))
impar = random(0, 10)


if soma == 0 :
    print("a maquina ganhou")

else:
    print("foi impate")

