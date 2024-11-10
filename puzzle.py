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

    




puzzle = CreatePuzzle()
puzzle = ShufflePuzzle(puzzle)
correct_puzzle = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 0]]


while puzzle != correct_puzzle:
    system("cls")
    DisplayPuzzle(puzzle)
    direction = input("Enter move (up, down, left, right): ").strip().lower()
    puzzle = MovePuzzle(puzzle,direction)
    
    
print("Congratulations, you won!")