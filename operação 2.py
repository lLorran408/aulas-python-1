# opraração
print("o que você vao fazer de amanha de manha?")
print("dormir / estudar")
manha = input()
print("jogar / teinar")
tarde = input()

if not manha or not tarde:
    print("você precisa diser o que vai fazer")
else:
  if manha == "dormir" or tarde == "jogar":
    print("você estadesperdiçando seu dia")
  elif manha == "estudar" or tarde == "treinar":
     print("você esta se aperfeiçoando")           
  else:
     print("não continue esta ação...")
print("tanha um bom dia")