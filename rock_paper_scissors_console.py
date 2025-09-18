"""
Console-based Rock Paper Scissors game where the player inputs their choice
and plays against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types "quit".
"""

import random

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

def play_rock_paper_scissors():
    player_score = 0
    computer_score = 0
    tie_count = 0
    
    print("Welcome to Rock Paper Scissors!")
    print("Type 'rock', 'paper', 'scissors', or 'quit' to exit")
    print("-" * 50)
    
    while True:
        # Get player choice
        player_choice = input("\nYour choice (rock/paper/scissors/quit): ").lower().strip()
        
        # Check if player wants to quit
        if player_choice == 'quit':
            print("\nThanks for playing!")
            print(f"Final Score - You: {player_score}, Computer: {computer_score}, Ties: {tie_count}")
            break
        
        # Validate player choice
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        # Get computer choice and determine winner
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        
        # Display results
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)
        
        # Update scores
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        elif result == "It's a tie!":
            tie_count += 1
        
        # Display current score
        print(f"Score - You: {player_score}, Computer: {computer_score}, Ties: {tie_count}")
        print("-" * 50)

if __name__ == "__main__":
    play_rock_paper_scissors()