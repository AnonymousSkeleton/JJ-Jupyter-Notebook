from veritas_lib import *
my = input("Choose: Rock, Paper, or Scissors: ")
print("You chose: " + my)
comp = get_computer_rps()
print("Computer chooses: " + comp)
winner = who_is_winner(my, comp)
print(winner)

