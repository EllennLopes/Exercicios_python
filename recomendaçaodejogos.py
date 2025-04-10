def recomendacao(dificuldade, jogadores):
    if dificuldade == "dificil":
        print("Você pode gostar de Dark Souls, ou Battletoads")
    elif dificuldade == "médio":
        print("Você pode gostar de The Legend of Zelda, ou Hollow Knight")
    else:
        print("Você pode gostar de Minecraft, ou Stardew Valley")
    
    if jogadores == "multiplayer":
        print("Você pode gostar de Ludo, ou Uno")
    else:
        print("Você pode gostar de The Witcher, ou Skyrim")

def main():
    while True:
        dificuldade = input("dificil, fácil ou médio? ")
        jogadores = input("multiplayer ou singleplayer? ")
        recomendacao(dificuldade, jogadores)
        continuar = input("deseja outra recomendação? (sim/não) ")
        if continuar != "sim":
            break
main()