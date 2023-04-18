
from game import Game


class App:
    def initiate(self):
        game = None
        print("\n")
        print("Welcome to Tic Tac Toe")

        while True:
            print(
"""
Menu
1. Start
2. Exit
"""
            )
            print("Enter 1 or 2")
            entry = input("Command: ")
            if entry == "1":
                game = Game()
                game.start()
            elif entry == "2":
                print("\n")
                print("Thank you for playing!")
                break
            else:
                print("\n")
                print("Invalid Entry")

