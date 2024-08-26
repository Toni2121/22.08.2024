def check_validity(str1: str) -> int:
    if str1.lower() == "rock":
        return 2
    elif str1.lower() == "scissors":
        return 1
    elif str1.lower() == "paper":
        return 0
    else:
        raise ValueError("illegal choice")


def check_winner(player1_choice: int, player2_choice: int) -> int:
    if player1_choice not in [0, 1, 2] or player2_choice not in [0, 1, 2]:
        raise ValueError("illegal game option")

    if player1_choice == player2_choice:
        return 0
    elif (player1_choice - player2_choice) % 3 == 1:
        return 1
    else:
        return 2

def play_game():
    player1_choice = input("player 1 - enter your choice (rock, paper, scissors): ")
    player2_choice = input("player 2 - enter your choice (rock, paper, scissors): ")
    player1_choice = check_validity(player1_choice)
    player2_choice = check_validity(player2_choice)
    result = check_winner(player1_choice, player2_choice)
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
