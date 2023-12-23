import random
class initiate:
    def __init__(self,gam,initialize, ranvalue, level):
        gam.initialize = __import__("clsmain").mainclass
        gam.ran_value = gam.ranvalue
        gam.level = level
    def generaterandom(self, gam):
        while True:
            try:
                gam.level = str(input("Enter Game Level E For Easy, H For Hard, S For Super:"))
                if (type(gam.level) is not str):
                    raise ValueError
                elif (gam.level == "s"):
                    print("Game Level::SuperHard")
                    gam.ran_value = random.randint(1,50)
                    gam.game_start = 1
                    break
                elif (gam.level == "h"):
                    print("Game Level::Hard")
                    gam.ran_value = random.randint(1, 30)
                    gam.game_start = 1
                    break
                elif (gam.level == "e"):
                    print("Game Level::Easy")
                    gam.ran_value == random.randint(1, 10)
                    gam.game_start = 1
                    break
            except ValueError:
                print(f"You entered {gam.level} Please iEnter Valid Level, E For Easy, H For Hard, S For Super")

