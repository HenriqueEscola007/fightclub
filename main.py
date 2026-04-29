def personagem(nome):
    return f"Olá lutador, {nome}!"

nome = input("Qual será o nome do seu personagem?\n")
print(personagem(nome))
print("Bem vindo ao\nFIGHT CLUB")

escolha = int(input("1 - START\n2 - QUIT\n"))
if escolha == 2:
    print("Tchau")
else :
    print("Começando")
    modo = str(input("escolha o nivel da jogabilidade\nFACIL\nNORMAL\nDIFICIL\n"))
    
    if modo == "facil":
        dano_inimigo = 20
        vida_lutador = 100
    elif modo == "normal":
        dano_inimigo = 30
        vida_lutador = 90
    elif modo == "dificil":
        dano_inimigo = 40
        vida_lutador = 80
