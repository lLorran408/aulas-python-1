print("eis, os meus maior sonho...")
sonho = ["1. me divertir na disney",
         "2. me banhar na praia de sepetiba",
         "3. tirar as ferias em paris",
         "4. fazer compras no westshopping"
         "5. ver as piramedes dp egito"]
for x in sonho:
    print(x)
print("opa , não qero sepetiba")
del(sonho[1])
print("e nem westshopping...")
del(sonho[3])
print("conferindo os sonhos...")
for x in sonho:
    print(x)