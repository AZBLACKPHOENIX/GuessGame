import random
import os

class initiate:
    def __init__(self, initialize, ranvalue, level):
        self.ranvalue = ranvalue
        self.level = level

    def generaterandom(self):
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.level = str(input("Enter Game Level E For Easy, H For Hard, S For Super:"))
                if not isinstance(self.level, str):
                    raise ValueError
                elif self.level.lower() == "s":  # Convert to lowercase for case-insensitive comparison
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.ranvalue = random.randint(1, 50)
                    self.game_start = 1
                    break
                elif self.level.lower() == "h":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.ranvalue = random.randint(1, 30)
                    self.game_start = 1
                    break
                elif self.level.lower() == "e":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.ranvalue = random.randint(1, 10)
                    self.gamestart = 1
                    break
            except Exception as e:
                print(f"You entered {self.level} Please enter a valid level, E for Easy, H for Hard, S for Super")
