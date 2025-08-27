# demonstrção e funções
def apresentação():
    print("meu nome é(myname).") 
    print("minha altuta é(myhigh)metros.")
    print("minha idade de é (myage).")
    return
def conferir(x):
    if x >= 1:
        print("você e mair de idade")
    else:
        print("ops, nenor de idade não pode")
        return
myname = str(input("digite seu nome"))
myhigh = float(input("digite sua altura"))
myage = int(input("digite sua idaede"))

apresentação()
conferir(myage)