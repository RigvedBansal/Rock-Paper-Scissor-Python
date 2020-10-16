from random import shuffle
def player_input():
    userinput = ''
    options = ['r','p','s']
    while userinput not in options:
        userinput = input("Enter your move(rock,paper or scissors): ")
    return  userinput
#player1move = player_input()
def ai_input():
    options = ['r','p','s']
    shuffle(options)
    return options[0]
#aimove = ai_input()

while True:
    playermove = player_input()
    aimove = ai_input()
    print(playermove)
    print(aimove)
    if aimove == 'r' and playermove == 'p':
        print("Player wins!!!!  ")
    elif aimove == 'p' and playermove == 'r':
        print("AI wins!!!  ")
    elif aimove == 'p' and playermove == 's':
        print("Player Wins!!!  ")
    elif aimove == 's' and playermove == 'p':
        print("AI wins!!!  ")
    elif aimove == 's' and playermove == 'r':
        print("Player wins")
    elif aimove == 'r' and playermove == 's':
        print("AI wins!!!  ")
    else:
        print("Draw")
    
    choice = input("If you want to play again type YES otherwise type NO: ").lower()
    if choice[0] == 'y':
        continue
    elif choice[0] == 'n':
        print("QUITING....")
        break