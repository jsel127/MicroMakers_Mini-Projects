import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return {"player": player_choice, "computer": computer_choice}

def check_winner(player, computer):
    if (player == computer):
        string_game_results("a tie", player, computer)
    elif (player == "rock"): 
        if (computer == "paper"):
            return string_game_results("your loss", player, computer)
        else: 
            return string_game_results("your win", player, computer);
    elif (player == "paper"):
        if (computer == "scissors"):
            return string_game_results("your loss", player, computer)
        else: 
            return string_game_results("your win", player, computer);
    elif (player == "scissors"):
        if (computer == "rock"):
            return string_game_results("your loss", player, computer)
        else: 
            return string_game_results("your win", player, computer);

def string_game_results(result, player, computer):
    return f"It was {result} (player: {player}, computer: {computer})"

# runs game
choices = get_choices()
result = check_winner(choices["player"], choices["computer"])
print(result)