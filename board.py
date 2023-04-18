from enum import Enum
from typing import Type

class BoardInput(Enum):
    X = "X"
    O = "O"

class Board:
    def __init__(self) -> None:
        self.__empty = "-"
        self.__board = [
            [" ","1","2","3"],
            ["A",self.__empty,self.__empty,self.__empty],
            ["B",self.__empty,self.__empty,self.__empty],
            ["C",self.__empty,self.__empty,self.__empty]]
        
        self.__accepted_input = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        
        self.__winning_combinations = [
            ["a1","b1","c1"],
            ["a2","b2","c2"],
            ["a3","b3","c3"],
            ["a1","a2","a3"],
            ["b1","b2","b3"],
            ["c1","c2","c3"],
            ["a1","b2","c3"],
            ["a3","b2","c1"]
        ]

    def display(self):
        for list in self.__board:
            print("  ".join(list))

    def play(self, icon: Type[BoardInput], coordinate: str) -> bool:
        if coordinate in self.__accepted_input:
            x,y = self.__getCoordinate(coordinate.lower())
            if self.__board[x][y] == "-":
                self.__board[x][y] = icon.value
                return True
            else:
                # invalid input
                return False
        else:
            # invalid input
            return False

    def check_winner(self):
        if self.__check_winning_match(BoardInput.O):
            return True, BoardInput.O
        elif self.__check_winning_match(BoardInput.X):
            return True, BoardInput.X
        else:
            return False, None
        
    def check_tie(self) -> bool:
        for coordinate in self.__accepted_input:
            x, y = self.__getCoordinate(coordinate)
            if self.__board[x][y] == self.__empty:
                return False
        return True
        
    def __getCoordinate(self, coordinate: str):
        if coordinate[:1] == "a":
            x = 1
        elif coordinate[:1] == "b":
            x = 2
        else:
            x = 3
        return x, int(coordinate[1:])
    
    def __check_winning_match(self, icon: BoardInput):
        for combination in self.__winning_combinations:
            match = True
            for coordinate in combination:
                x, y =  self.__getCoordinate(coordinate)
                if self.__board[x][y] != icon.value:
                    match = False
                    break
            if match:
                return True
        return False
