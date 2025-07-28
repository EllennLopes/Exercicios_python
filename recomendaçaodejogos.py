import random

def recomendaçao(dificuldade, jogadores):
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

def recomendaçao_aleatoria():
    dificuldades = ["dificil", "médio", "fácil"]
    jogadores = ["multiplayer", "singleplayer"]

    dificuldade = random.choice(dificuldades)
    jogador = random.choice(jogadores)

    print("Recomendação aleatória!")
    recomendaçao(dificuldade, jogador)

def validar_opçao(pergunta, opçoes):
    while True:
        resposta = input(pergunta).lower()
        if resposta in opçoes:
            return resposta
        else:
            print ("Opção inválida. Escolha uma das seguintes opções:", ", ".join(opçoes))

def main():
        while True:
            tipo_recomendacao = validar_opçao(
            "Você quer uma recomendação aleatória ou personalizada? (aleatória/personalizada): ",
            ["aleatória", "personalizada"]
        )

            if tipo_recomendacao == "aleatória":
                recomendaçao_aleatoria()
            else:
                dificuldade = validar_opçao("Escolha a dificuldade (dificil, fácil ou médio): ", ["dificil", "fácil", "médio"])
                jogadores = validar_opçao("Escolha o modo de jogo (multiplayer ou singleplayer): ", ["multiplayer", "singleplayer"])
                recomendaçao(dificuldade, jogadores)

            continuar = validar_opçao("Deseja outra recomendação? (sim/não): ", ["sim", "não"])
            if continuar != "sim":
                break
main ()
        
