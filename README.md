# Challenge project - Build a minigame console app with GitHub Copilot

Starter and Final code for the Challenge project: "Challenge project - Build a minigame console app with GitHub Copilot". To check the solution, change the branch to **Solution**.

# Rock Paper Scissors Game

This is a simple command-line implementation of the classic game "Rock Paper Scissors" written in Python. The game allows you to play against the computer and keeps track of your score.


## Game Rules

The winner of each round is determined by the following rules:

- Rock beats Scissors
- Scissors beat Paper
- Paper beats Rock

If both you and the computer choose the same move, it's a tie.


## How to Play

1. Make sure you have Python installed on your system.

2. Clone this repository or download the `app.py` file.

3. Open a terminal or command prompt and navigate to the directory where the `app.py` file is located.

4. Run the following command to start the game: python app.py

5. You will be prompted to enter your move. Type one of the following options:
- `rock`
- `paper`
- `scissors`

6. The computer will randomly choose its move, and the winner of the round will be determined based on the following rules:
- Rock beats Scissors
- Scissors beat Paper
- Paper beats Rock

7. After each round, you will be informed whether you won, lost, or tied with the computer.

8. You will be asked if you want to play again. Enter `yes` to continue playing or `no` to quit the game.

9. If you choose to quit, the game will display the final results, including the number of rounds played, your wins, and the computer's wins.


## Code Structure

The code is organized into several functions:

- `get_player_move()`: Prompts the player to enter their move and validates the input.
- `get_computer_move()`: Generates a random move for the computer.
- `determine_winner()`: Determines the winner of a round based on the player's and computer's moves.
- `update_scores()`: Updates the player's and computer's scores based on the winner of a round.
- `play_game()`: Handles the main game loop, including player input, computer move generation, winner determination, score updates, and game termination.

The game uses constants (`ROCK`, `PAPER`, `SCISSORS`) to represent the possible moves and a dictionary (`WINNING_COMBINATIONS`) to define the winning combinations.


---
Enjoy playing Rock Paper Scissors!