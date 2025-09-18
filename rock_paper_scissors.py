"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types "quit".
"""

import os
import random
import tkinter as tk
from tkinter import messagebox

# Set environment variables for Tcl/Tk to fix potential path issues
os.environ['TCL_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\User\AppData\Local\Programs\Python\Python313\tcl\tk8.6'a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""


import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

class RPSGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.player_score = 0
        self.computer_score = 0
        self.tie_count = 0

        self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors:")
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock", width=10, command=lambda: self.play('rock'))
        self.rock_button.grid(row=0, column=0, padx=5)
        self.paper_button = tk.Button(self.button_frame, text="Paper", width=10, command=lambda: self.play('paper'))
        self.paper_button.grid(row=0, column=1, padx=5)
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=10, command=lambda: self.play('scissors'))
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Score - You: 0, Computer: 0, Ties: 0")
        self.score_label.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def play(self, player_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        self.result_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}")

        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        elif result == "It's a tie!":
            self.tie_count += 1

        self.score_label.config(text=f"Score - You: {self.player_score}, Computer: {self.computer_score}, Ties: {self.tie_count}")


if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()
