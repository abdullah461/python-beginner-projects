import random
import math

def play():
    user = input("what is your choice? 'r' for rock, 'p' for paper, 's' for scissors: \n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"user: {user} and computer: {computer}") 

    if is_win(user, computer):
        print(f"user:{user} and computer:{computer}")
        print('You won!') 
    else:
        print('it\'s too tight')

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    elif (player == opponent):
        return False

if __name__ == '__main__':
    play()
    