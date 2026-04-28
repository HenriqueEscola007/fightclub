def personagem(nome):
    return f"Olá lutador, {nome}!"
nome = input("Qual será o nome do seu personagem?\n")
print(personagem(nome))
print("Bem vindo ao\nFIGHT CLUB")
escolha = input("  START\n  QUIT\n")
while escolha == "START":
    if escolha == "QUIT":
        break
    print("Começando")