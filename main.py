def personagem(nome):
    return f"Olá lutador, {nome}!"

nome = input("Qual será o nome do seu personagem?\n")
print(personagem(nome))
print("Bem vindo ao\nFIGHT CLUB")

while True:
    escolha = int(input("1 - START\n  2 - QUIT\n"))
    if escolha == 2:
        break
    else :
        print("Começando")
        input("escolha o nivel da jogabilidade\nFACIL\nNORMAL\nDIFICIL\n")