import os
class start_game:
    def __init__(start, startgame,st, p_t):
        start = __import__("clsmain").mainclass
        start.start_game = startgame
        start.p_turn = p_t
        startgame = 0
    def startgame(start):
        os.system('cls' if os.name == 'int' else 'clear')
        start.st = input("Press Enter To Start Game")
        if (start.st == ""):
            print("Starting Game")
        else:
            print("Game Did Not Start")
