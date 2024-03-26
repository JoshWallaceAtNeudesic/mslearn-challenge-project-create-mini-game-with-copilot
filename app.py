import random

# Define constants for move options
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

# Define the winning combinations
WINNING_COMBINATIONS = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER
}

def get_player_move():
    while True:
        player_move = input("Enter your move (rock/paper/scissors): ").lower()
        if player_move in WINNING_COMBINATIONS:
            return player_move
        print("Invalid move. Please enter rock, paper, or scissors.")

def get_computer_move():
    return random.choice(list(WINNING_COMBINATIONS.keys()))

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    elif WINNING_COMBINATIONS[player_move] == computer_move:
        return "player"
    else:
        return "computer"

def update_scores(winner, player_score, computer_score):
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1
    return player_score, computer_score

def play_game():
    player_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        player_move = get_player_move()
        computer_move = get_computer_move()
        print(f"Computer move: {computer_move}")

        winner = determine_winner(player_move, computer_move)
        player_score, computer_score = update_scores(winner, player_score, computer_score)
        rounds_played += 1

        if winner == "tie":
            print("It's a tie!")
        else:
            print(f"{winner.capitalize()} wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Please enter yes or no: ").lower()

        if play_again == "no":
            break

    print("\nFinal results:")
    print(f"Rounds played: {rounds_played}")
    print(f"Player wins: {player_score}")
    print(f"Computer wins: {computer_score}")

# Start the game
play_game()