class gameplay:
    def __init__(self, gp):
        gp = __import__("clsmain").mainclass
    def process(self):
        try:
            while True:
                gp.user_input = int(input("1: PVP OR 2:PLAY WITH COM")
                    if (type(user_input) is not int):
                        raise TypeError("Enter 1 To Play With Human Or 2 To Play With Computer")
                    elif (user_input < 1 or > 2):
                        raise ValueError("Enter 1 To Play With Human Or 2 To Play With A Computer")
                    elif (user_input == 1):
                        gp.p_turn = 2
                    if (gp.p_turn % 2) == 0:


