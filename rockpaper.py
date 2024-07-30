import tkinter as tk
import random

def computer_choice():
    global comp_pick
    comp_pick = random.randint(1, 3)

player_score = 0
comp_score = 0

def display_tie():
    append_output("It's a Tie!\n")

def display_comp_win():
    global comp_score
    comp_score += 1
    append_output("Computer scores a point!\n")

def display_player_win():
    global player_score
    player_score += 1
    append_output("Player scores a point!\n")

def determine_winner():
    if player_score > comp_score:
        append_output('Congratulations, Player wins the game!\n')
    elif player_score == comp_score:
        append_output('The game is a tie!\n')
    else:
        append_output('Computer wins the game! Better luck next time.\n')

def initiate_game():
    global rounds_remaining, current_round
    rounds_remaining = int(rounds_input.get())
    current_round = 0
    rounds_input.delete(0, tk.END)
    append_output(f"Game initiated for {rounds_remaining} rounds.\n")
    proceed_to_next_round()

def generate_comment():
    comments = [
        "How about trying rock this time?",
        "Maybe paper will work?",
        "Let's see if you can beat me now!",
        "Feeling confident with scissors?",
        "Rock, Paper, or Scissors?",
        "Ready to lose again?"
    ]
    return random.choice(comments)

def proceed_to_next_round():
    global rounds_remaining, current_round
    if rounds_remaining > 0:
        rounds_remaining -= 1
        computer_choice()
        current_round += 1
        comment = generate_comment()
        append_output(f"Round {current_round}\n{comment}\n")
        user_input.config(state=tk.NORMAL)
        user_input.focus()
    else:
        determine_winner()
        append_output("Game Over. Would you like to play again? (yes/no):\n")
        user_input.config(state=tk.NORMAL)

def handle_input(event=None):
    user_choice = user_input.get()
    user_input.delete(0, tk.END)
    user_choice = user_choice.lower()
    
    if user_choice in ['yes', 'no']:
        if user_choice == 'yes':
            reset_game()
        else:
            append_output("Thank you for playing!\n")
            user_input.config(state=tk.DISABLED)
        return

    if user_choice not in ['rock', 'paper', 'scissors']:
        append_output("Invalid input! Please choose rock, paper, or scissors.\n")
        return

    user_input.config(state=tk.DISABLED)
    if user_choice == 'rock':
        if comp_pick == 1:
            append_output("Computer chose Rock 🗿\n")
            display_tie()
        elif comp_pick == 2:
            append_output("Computer chose Paper 📝\n")
            display_comp_win()
        else:
            append_output("Computer chose Scissors ✂️\n")
            display_player_win()
    elif user_choice == 'paper':
        if comp_pick == 1:
            append_output("Computer chose Rock 🗿\n")
            display_player_win()
        elif comp_pick == 2:
            append_output("Computer chose Paper 📝\n")
            display_tie()
        else:
            append_output("Computer chose Scissors ✂️\n")
            display_comp_win()
    else:  # scissors
        if comp_pick == 1:
            append_output("Computer chose Rock 🗿\n")
            display_comp_win()
        elif comp_pick == 2:
            append_output("Computer chose Paper 📝\n")
            display_player_win()
        else:
            append_output("Computer chose Scissors ✂️\n")
            display_tie()

    append_output(f"Player Score: {player_score}\n")
    append_output(f"Computer Score: {comp_score}\n")
    
    proceed_to_next_round()

def reset_game():
    global player_score, comp_score
    player_score = 0
    comp_score = 0
    append_output("Enter the number of rounds you want to play:\n")
    rounds_input.config(state=tk.NORMAL)
    rounds_input.focus()

# ~~GUI~~
def append_output(text):
    output_display.insert(tk.END, text)
    output_display.see(tk.END)

root = tk.Tk()
root.title("Rock Paper Scissors Game")
custom_font=("Arial", 14)
output_display = tk.Text(root, wrap=tk.WORD, height=20, width=50, font=custom_font)
output_display.pack(pady=10)
rounds_input = tk.Entry(root, width=50)
rounds_input.pack()
rounds_input.bind("<Return>", lambda event: initiate_game())
append_output("Enter the number of rounds you want to play:\n")

user_input = tk.Entry(root, width=50)
user_input.pack()
user_input.bind("<Return>", handle_input)
user_input.config(state=tk.DISABLED)

root.mainloop()