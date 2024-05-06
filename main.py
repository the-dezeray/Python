from lang import Lang
from tic_tac_toe import TicTacToe
import Players
from terminal import Terminal
Lang.prompt_default_lang()
# ! to be refactored !!
n_player1 = input(f"{Lang.get_string(text_id="enter_name1",lang="en")}")
n_player2 = input(f"{Lang.get_string(text_id="enter_name2",lang="en")}")

players_teams = Players.team_selection(n_player1, n_player2)
Terminal.clear()
player1 = Players.Player(n_player1,players_teams[n_player1])
player2 = Players.Player(n_player2,players_teams[n_player2])

game_1 = TicTacToe()
game_1.draw_board(player1,player2)
