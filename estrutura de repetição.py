# demonstração for/range...
print("digite um valor maximo desejado:")
numero = int(input())

print("segue, os numeros desejados:")
# o numero sempre começa no 0 por isso o 1,numero + 1
for x in range (1,numero + 1):
    print(x)

# demonstração for/range 2...
print("digite o nome desejado:")
nome = input()

print("segue, os numeros desejados:")
for x in nome:
    print(x)

    # demonstração for/range...
print("digite o maximo desejado:")
numero = int(input())
x = 1
print("segue, os numeros desejados")
while x <= numero:
    print(x)
    x = x + 1
    # não foi impresso o numero desejado

    # demonstração for/range...
print("digite o maximo desejado:")
numero = int(input())
x = 2
print("segue, os numeros desejados")
while x <= numero:
    print(x)
    x = x + 2
    # não foi impresso o numero desejado