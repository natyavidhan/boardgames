import os

moves = ['Top Left',
         'Top Middle',
         'Top Right',
         'Mid Left',
         'Mid Middle',
         'Mid Right',
         'Bot Left',
         'Bot Middle',
         'Bot Right',
         'Exit',
         'cls']


playerd = ['Y','X']


table = ['_','_','_',
         '_','_','_',
         '_','_','_']


def release():
    cmd = "exit"
    os.system(cmd)


def tictactoe_game():
    print("")
    print(" " + " _" + " _" + " _")
    print(" " + "|" + table[0] + "|" + table[1] + "|" + table[2] + "|")
    print(" " + "|" + table[3] + "|" + table[4] + "|" + table[5] + "|")
    print(" " + "|" + table[6] + "|" + table[7] + "|" + table[8] + "|")
    print("")

def moving(num, player):
    table[int(num)] = player
    cs = 'cls'
    os.system(cs)
    tictactoe_game()

def player1():
    ActivePlayer=True
    while ActivePlayer:
        playerx = input("PX:")
        for i in range(9):
            if playerx == moves[i]:
                moving(i, "X")
                ActivePlayer = False
        if playerx == moves[10]:
            cs = 'cls'
            os.system(cs)

def player2():
    ActivePlayer = True
    while ActivePlayer:
        playery = input("PY:")
        for i in range(9):
            if playery == moves[i]:
                moving(i, "Y")
                ActivePlayer = False
        if playery == moves[10]:
            cs = 'cls'
            os.system(cs)
            tictactoe_game()

def tictactoe_main():
    tictactoe_game()
    while True:
        player2()
        player1()


tictactoe_main()
