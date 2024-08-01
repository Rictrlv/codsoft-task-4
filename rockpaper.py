import tkinter as tk
import random

def generateComputerChoice():
    options = ['Rock', 'Paper', 'Scissors']
    return random.choice(options)


def decideWinner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return "It's a Draw!"
    elif (playerChoice == 'Rock' and computerChoice == 'Scissors') or \
         (playerChoice == 'Scissors' and computerChoice == 'Paper') or \
         (playerChoice == 'Paper' and computerChoice == 'Rock'):
        return "You WIN!"
    else:
        return "Computer WINS!"


def initiateGame(playerChoice):
    computerChoice = generateComputerChoice()
    outcome = decideWinner(playerChoice, computerChoice)
    displayResult.config(text=f"Your choice: {playerChoice}\nComputer's choice: {computerChoice}\n\n{outcome}")
    replayButton.config(state=tk.NORMAL)


def restartGame():
    displayResult.config(text="Choose your move!")
    replayButton.config(state=tk.DISABLED)


gameWindow = tk.Tk()
gameWindow.title("Rock-Paper-Scissors Game")


instructions = tk.Label(gameWindow, text="Select Rock, Paper, or Scissors:")
instructions.pack(pady=10)


displayResult = tk.Label(gameWindow, text="Choose your move!", font=("Arial", 14))
displayResult.pack(pady=20)


rockBtn = tk.Button(gameWindow, text="Rock", command=lambda: initiateGame('Rock'), width=10)
rockBtn.pack(side=tk.LEFT, padx=10)

paperBtn = tk.Button(gameWindow, text="Paper", command=lambda: initiateGame('Paper'), width=10)
paperBtn.pack(side=tk.LEFT, padx=10)

scissorsBtn = tk.Button(gameWindow, text="Scissors", command=lambda: initiateGame('Scissors'), width=10)
scissorsBtn.pack(side=tk.LEFT, padx=10)


replayButton = tk.Button(gameWindow, text="Play Again", command=restartGame, width=10, state=tk.DISABLED)
replayButton.pack(pady=20)


gameWindow.mainloop()
