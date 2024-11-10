def CreatePuzzle():
    puzzle = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,0]
    ]
    return puzzle

def DisplayPuzzle(puzzle):
    display_puzzle = [[str(tile) if tile != 0 else " " for tile in row] for row in puzzle] # Vymění 0 za " " pro lepší UI
    for row in display_puzzle:
        print(" ".join(tile.rjust(2) for tile in row))

puzzle = CreatePuzzle()
DisplayPuzzle(puzzle)