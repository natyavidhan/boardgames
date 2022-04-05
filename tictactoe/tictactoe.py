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


def playerx():
    playerx = input("PX:")
    ActivePlayer = True
    if playerx not in moves:
        tictactoe_main()
    if playerx == moves[0]:
        table[0] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[1]:
        table[1] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[2]:
        table[2] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[3]:
        table[3] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[4]:
        table[4] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[5]:
        table[5] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[6]:
        table[6] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[7]:
        table[7] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[8]:
        table[8] = "X"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playerx == moves[10]:
        cs = 'cls'
        os.system(cs)
        tictactoe_main()

    while not ActivePlayer:
        playery()

    
def playery():
    playery = input("PY:")
    ActivePlayer = True
    if playery not in moves:
        tictactoe_main()
    if playery == moves[0]:
        table[0] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[1]:
        table[1] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[2]:
        table[2] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[3]:
        table[3] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[4]:
        table[4] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[5]:
        table[5] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[5]:
        table[5] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[6]:
        table[6] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[7]:
        table[7] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[8]:
        table[8] = "Y"
        ActivePlayer = False
        cs = 'cls'
        os.system(cs)
        tictactoe_main()
    if playery == moves[10]:
        cs = 'cls'
        os.system(cs)
        tictactoe_main()

    while not ActivePlayer:
        playerx()


def tictactoe_main():
    tictactoe_game()
    playery()


tictactoe_main()
