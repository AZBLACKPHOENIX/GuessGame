class start_game:
    def __init__(start, startgame,st, p_t):
        start.startgame = __import__("clsmain").mainclass
        start.st = startgame.game_game
        start.p_t = startgame = startgame.p_turns
    def startgame(start):
        start.st = input("Press Enter To Start Game")
        if (start.st == ""):
            start.p_t = 1
            print("Starting Game")
        else:
            print("Game Did Not Start")
