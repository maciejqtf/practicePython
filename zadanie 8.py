#8 Make a two-player Rock-Paper-Scissors game.


while True:
    game_dict = {"Rock" : 1, "Paper" : 2, "Scissors" :3}
    player1 = input("Player 1, Type 1 for Rock, 2 for Paper or 3 for scissors")
    player2 = input("Player 2,Type 1 for Rock, 2 for Paper or 3 for scissors")

    if (player1 == "1") & (player2 == "2"):
        print("Player 2 wins. Paper beats Rock")
        break
    elif (player1 == "1") & (player2 == "3"):
        print("Player 1 wins. Rock beats Scissors")
        break
    elif player1 == "1" == player2:
        print("It's a tie, try again!")1
    if (player1 == "2") & (player2 == "1"):
        print("Player 1 wins. Paper beats Rock")
        break
    elif (player1 == "2") & (player2 == "3"):
        print("Player 2 wins. Scissors beat Paper")
        break
    elif player1 == "2" == player2:
        print("It's a tie, try again!")
    if (player1 == "3") & (player2 == "1"):
        print("Player 2 wins. Rock beats Scissors")
        break
    elif (player1 == "3") & (player2 == "2"):
        print("Player 1 wins. Scissors beats Paper")
        break
    elif player1 == "3" == player2:
        print("It's a tie! Try again")
