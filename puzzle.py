from random import choice
from os import system

def CreatePuzzle():
    puzzle = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,0]
    ]
    return puzzle

def FindEmpty(puzzle):
    for x in range(4):
        for y in range(4):
            if puzzle[x][y] == 0:
                return x,y

def MovePuzzle(puzzle, direction):
    x,y = FindEmpty(puzzle)
    if direction == 'up' and x+1 <= 3:
        puzzle[x+1][y], puzzle[x][y] = puzzle[x][y], puzzle[x+1][y]
    elif direction == 'down' and x-1 >= 0:
        puzzle[x-1][y], puzzle[x][y] = puzzle[x][y], puzzle[x-1][y]
    elif direction == 'left' and y+1 <= 3:
        puzzle[x][y+1], puzzle[x][y] = puzzle[x][y], puzzle[x][y+1]
    elif direction == 'right'and y-1 >= 0:
        puzzle[x][y-1], puzzle[x][y] = puzzle[x][y], puzzle[x][y-1]
    elif direction == "cheat":
        puzzle = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 0, 15]
        ]
    return puzzle
    
def ShufflePuzzle(puzzle):
    for move in range(100):
        direction = choice(["up","down","left","right"])
        puzzle = MovePuzzle(puzzle,direction)
    return puzzle

def DisplayPuzzle(puzzle):
    display_puzzle = [[str(tile) if tile != 0 else " " for tile in row] for row in puzzle] # Vymění 0 za " " pro lepší UI
    for row in display_puzzle:
        print(" ".join(tile.rjust(2) for tile in row))

def GetMoveInput():
    while True:
        direction = input("\nEnter your move (up, down, left, right): ").strip().lower()
        if direction in ["up", "down", "left", "right", "cheat"]:
            return direction
        else:
            print("[ERROR] Invalid move: 'up', 'down', 'left', 'right'.")

def ClearScreen():
    system("cls")




def main():
    puzzle = CreatePuzzle()
    puzzle = ShufflePuzzle(puzzle)
    correct_puzzle = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 0]]
    print("\nWelcome to the 15-Puzzle Game!")
    print("The goal is to arrange the numbers in order, with the empty space (0) in the bottom-right corner.")

    while puzzle != correct_puzzle:
        ClearScreen()
        DisplayPuzzle(puzzle)
        direction = GetMoveInput()
        puzzle = MovePuzzle(puzzle,direction)
    
    ClearScreen()
    DisplayPuzzle(puzzle)
    print("\nCongratulations, you won!")
    