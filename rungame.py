from clsstart import start_game
from clsmain import mainclass
from clsinitiate import initiate
from clsgameplay import playgame
main_game_instance = mainclass(None, None, None, None, None, None, None, None)
start_instance = start_game(main_game_instance, None, None)  # Replace None with actual values
start_instance.startgame()
initiate_game = initiate(main_game_instance, None, None)
play = playgame(main_game_instance, None, None)
play.process()
play.play_game()
