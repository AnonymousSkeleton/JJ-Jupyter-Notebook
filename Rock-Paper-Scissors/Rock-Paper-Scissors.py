from veritas_lib import get_computer_rps
from veritas_lib import who_is_winner

your_choice = input("What is your choice? [rock, paper, or scissors]")

computer_choice = get_computer_rps()

winner = who_is_winner(your_choice, computer_choice)
print(winner)