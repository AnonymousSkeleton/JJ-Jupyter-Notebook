import random
def get_computer_rps():
    rps = ['rock', 'paper', 'scissors']
    return(random.choice(rps))
def who_is_winner(your_choice, computer_choice):
    if your_choice == 'rock' and computer_choice == 'paper':
        return ("Computer wins!")
    elif your_choice == 'rock' and computer_choice == 'scissors':
        return ("You win!")
    elif your_choice == 'rock' and computer_choice == 'rock':
        return ("Tie!")
    elif your_choice == 'scissors' and computer_choice == 'rock':
        return ("Computer wins!")
    elif your_choice == 'scissors' and computer_choice == 'paper':
        return ("You win!")
    elif your_choice == 'scissors' and computer_choice == 'scissors':
        return ("Tie!")
    elif your_choice == 'paper' and computer_choice == 'scissors':
        return ("Computer wins!")
    elif your_choice == 'paper' and computer_choice == 'rock':
        return ("You win!")
    elif your_choice == 'paper' and computer_choice == 'paper':
        return ("Tie!")
        