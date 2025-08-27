print("digite quando você tem para pagar a divida")
int(input())
x = input
y = x + 1500

if y == 0:
    print("a divida foi paga")
elif y > 1500:
    print("a divida foi paga seu troco e",y)
elif y < 1500:
    print("ainda falta:",y)    
else:
    print("???")