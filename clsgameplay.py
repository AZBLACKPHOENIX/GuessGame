import os
from clsinitiate import initiate

class playgame:
    def __init__(self, user_input, p_turns, gs):
        self.gp = __import__("clsmain").mainclass
        self.gp.user_input = user_input
        self.gp.p_turns = p_turns
        self.gp.game_start = gs

    def process(self):
        while True:
            try:
                self.gp.user_input = input("1 Play With Human:\n2 Play With Computer:")
                if not isinstance(self.gp.user_input, str):
                    raise ValueError
                if self.gp.user_input == "1" or self.gp.user_input == "2":
                    self.gp.game_play = 0
                    self.gp.p_turns = 1
                    break
                else:
                    raise ValueError("Invalid input. Please enter 1 or 2.")
            except ValueError as e:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Incorrect Input: {e}")

    def play_game(self):
        initiate_instance = initiate(None, None, None)
        initiate_instance.generaterandom()
        level = initiate_instance.level
        hidden_number = initiate_instance.ranvalue

        while True:
            try:
                if self.gp.user_input == "1" and self.gp.p_turns == 1:
                    if level == "s":
                        print("Enter 0 To Exit The Game")
                        print("Game Level::---SUPER HARD---")
                        print("Guess a number between 1-50")
                        player_number = int(input("Player 1:"))
                        if player_number == hidden_number:
                            print(f"Player 1 WON!! Hidden Number Is: {hidden_number}")
                            break
                        elif player_number == "":
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif player_number == 0:
                            os.system("cls" if os.name == 'nt' else 'clear')
                            print("GAME DEVELOPED BY WISE LUCKY MDHLOVU")
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        self.gp.p_turns = 2
                    elif level == "h":
                        print("Enter 0 To Exit The Game")
                        print("Game Level::---HARD---")
                        print("Guess a number between 1-20")
                        player_number = int(input("Player 1:"))
                        if player_number == hidden_number:
                            print(f"Player 1 WON!! Hidden Number Is: {hidden_number}")
                            break
                        elif player_number == "":
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif player_number == 0:
                            os.system("cls" if os.name == 'nt' else 'clear')
                            print("GAME DEVELOPED BY WISE LUCKY MDHLOVU")
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        self.gp.p_turns = 2
                    elif level == "e":
                        print("Enter 0 To Exit The Game")
                        print("Game Level::---EASY---")
                        print("Guess a number between 1-10")
                        player_number = int(input("Player 1:"))
                        if player_number == hidden_number:
                            print(f"Player 1 WON!! Hidden Number Is: {hidden_number}")
                            break
                        elif player_number == "":
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif player_number == 0:
                            os.system("cls" if os.name == 'nt' else 'clear')
                            print("GAME DEVELOPED BY WISE LUCKY MDHLOVU")
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        self.gp.p_turns = 2
                elif self.gp.user_input == "1" and self.gp.p_turns == 2:
                    if level == "s":
                        print("Enter 0 To Exit The Game")
                        print("Game Level::---SUPER HARD---")
                        print("Guess a number between 1-50")
                        player_number = int(input("Player 2: "))
                        self.gp.p_turns = 1
                        if player_number == hidden_number:
                            print(f"Player 2 WON!! Hidden Number Is: {hidden_number}")
                            break
                        if player_number == hidden_number:
                            os.system('cls' if name=='nt' else 'clear')
                        elif player_number == 0:
                            os.system('cls' if name == 'int' else 'clear')
                            print("GAME DEVOLOPED BY WISE LUCKY MDHLOVU")
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        print("Enter A Number")
                    elif level == "h":
                        print("Enter 0 To Exit The Game")
                        print("Game Level::---HARD---")
                        print("Guess a number between 1-20")
                        player_number = int(input("Player 2:"))
                        if player_number == hidden_number:
                            print(f"Player 2 WON!! Hidden Number Is: {hidden_number}")
                            break
                        elif player_number == "":
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif player_number == 0:
                            os.system("cls" if os.name == 'nt' else 'clear')
                            print("GAME DEVELOPED BY WISE LUCKY MDHLOVU")
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        self.gp.p_turns = 1
                    elif level == "e":
                        print("Enter 0 To Exit The Game")
                        print("Game Level::---EASY---")
                        print("Guess a number between 1-10")
                        player_number = int(input("Player 2:"))
                        if player_number == hidden_number:
                            print(f"Player 2 WON!! Hidden Number Is: {hidden_number}")
                            break
                        elif player_number == "":
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif player_number == 0:
                            os.system("cls" if os.name == 'nt' else 'clear')
                            print("GAME DEVELOPED BY WISE LUCKY MDHLOVU")
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        self.gp.p_turns = 1

            except ValueError:
                print("Please Enter A Number")

