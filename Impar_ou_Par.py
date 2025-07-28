import random

def jogar():
    while True:
        print("Bem-vindo ao jogo de ímpar ou par")
        mensagem_escolha = "Para jogar, escolha 'par' ou 'ímpar': "
        escolha = input(mensagem_escolha).strip().lower()
        while escolha not in ('par', 'ímpar'):
            print("Escolha inválida. Por favor, digite 'par' ou 'ímpar'")
            escolha = input(mensagem_escolha).strip().lower()

        jogador = int(input("Escolha um número entre 0 e 10: "))
        while jogador < 0 or jogador > 10:
            print("Número inválido. Por favor, escolha um número entre 0 e 10.")
            jogador = int(input("Escolha um número entre 0 e 10: "))

        computador = random.randint(0, 10)
        soma = jogador + computador
        print(f"Você escolheu {jogador} e o computador escolheu {computador}")
        print(f"A soma é: {soma}")

        resultado = 'par' if soma % 2 == 0 else 'ímpar'
        if resultado == escolha:
            print(f"Você venceu! A soma é {resultado}.")
        else:
            print(f"Você perdeu! A soma é {resultado}.")
        continuar = input("Deseja jogar novamente? (sim/não): ")
        if continuar != 'sim':
            print("Até logo!")
            break
    

jogar()