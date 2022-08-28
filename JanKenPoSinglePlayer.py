import random
keep = 1
placar1, placar2 = 0, 0
user2 = random.randint(1, 3)    
print("Digite Seu Nome Para Começar")
jogador1 = input()
while (keep == 1) :
    print("Escolha Seu Movimento")
    print("1-Pedra | 2-Papel | 3-Tesoura")
    user1 = int(input())
    jogador2 = "CPU"
    print("")
    if user1 == 1:
        player1 = ("Pedra")
    else:
        if user1 == 2:
            player1 = ("Papel")
        else:
            player1 = ("Tesoura")
    if user2 == 1:
        player2 = ("Pedra")
    else:
        if user2 == 2:
            player2 = ("Papel")
        else:
            player2 = ("Tesoura")
    if player1 == player2:
        winner = "Ninguem"
        looser = "Ninguem"
        victory = "Ninguem"
    else:
        if player1 == "Pedra" and player2 == "Papel":
            winner = player2
            looser = player1
            victory = jogador2
        if player1 == "Pedra" and player2 == "Tesoura":
            winner = player1
            looser = player2
            victory = jogador1
        if player1 == "Papel" and player2 == "Tesoura":
            winner = player2
            looser = player1
            victory = jogador2
        if player1 == "Papel" and player2 == "Pedra":
            winner = player1
            looser = player2
            victory = jogador1
        if player1 == "Tesoura" and player2 == "Pedra":
            winner = player2
            looser = player1
            victory = jogador2
        if player1 == "Tesoura" and player2 == "Papel":
            winner = player2
            looser = player1
            victory = jogador2
    print(jogador1, "escolheu", player1)
    print("")
    print(jogador2, "escolheu", player2)
    print("")
    print(winner, "Ganha de", looser)
    print("")
    print(victory, "Ganhou")
    print("")
    print("Placar Parcial")
    if (victory == jogador1) :
        placar1 += 1
    else:
        if (victory == jogador2) :
            placar2 +=1
        else:
            print("Ninguem Pontuou")
    print(jogador1,"=", placar1,  "x", jogador2, "=",placar2)
    print("")
    print("Deseja Continuar Jogando?")
    print("1-Sim | 2-Nao")
    keep = int(input())
    print("")
print("Placar Final")
print(jogador1, " = ", placar1, "x",jogador2, " = ", placar2)
print("")
print("- Fim de Jogo -")
