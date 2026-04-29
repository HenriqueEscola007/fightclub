import random

def personagem(nome):
    return f"Olá lutador, {nome}!"

def inicia_jogo(dificuldade):
    return modo

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
        dano_jogador = random.Random(1, 200)
        vida_inimigo = random.Random(100, 350)
        
    elif modo == "normal":
        dano_inimigo = 30
        vida_lutador = 90
        dano_jogador = random.Random(1, 100)
        vida_inimigo = random.Random(100, 300)
    elif modo == "dificil":
        dano_inimigo = 40
        vida_lutador = 80
        dano_jogador = random.Random(1, 80)
        vida_inimigo = random.Random(100, 400)
        
def movimento(acao):
    return 