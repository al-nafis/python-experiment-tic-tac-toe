from board import Board, BoardInput
from player import Player


class Game:

    def __init__(self) -> None:    
        self.__p1: Player = Player(id=1, icon=BoardInput.X)
        self.__p2: Player = Player(id=2, icon=BoardInput.O)
        self.__board: Board = Board()

    def start(self):
        winner_found = False
        game_tied = False
        while not winner_found and not game_tied:
            # Player 1's turn
            self.__play_a_turn(self.__p1)
            winner_found = self.__board.check_winner()[0]
            game_tied = self.__board.check_tie()
            if winner_found or game_tied:
                break
            # Player 2's turn
            self.__play_a_turn(self.__p2)
            winner_found = self.__board.check_winner()[0]
            game_tied = self.__board.check_tie()
            print("winner: " + str(winner_found))
            print("game tied: " + str(game_tied))
            
        print("\n")
        print("Game Over!")
        print("\n")
        self.__board.display()
        print("\n")
        if winner_found:
            winner = 1 if self.__board.check_winner()[1] == self.__p1.icon else 2
            print("Player {} wins. Congratulations!".format(winner))
        else:
            print("Game tied!")



    def __play_a_turn(self, player: Player):
        is_valid = False
        while not is_valid:
            print("\n")
            self.__board.display()
            print("\n")
            print("Enter coordinate to place your sign. for instance, A1, B2, C3, B1 etc")
            entry = input("Player {}: ".format(player.id))
            is_valid = self.__board.play(player.icon, entry)
            if not is_valid:
                print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Invalid Input. Either you have entered the wrong coordinate or it is already used. Please try again
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                """)
