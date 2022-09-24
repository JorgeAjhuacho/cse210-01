"""
Tic Tac Toe
Author: Jorge Ajhuacho
"""

def main():
    print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9")
    first_player = "x"
    board_cell = cells_of_board()
    while not (winner(board_cell)):
        print_board(board_cell)
        new_move(first_player,board_cell)
        first_player = next_player(first_player)
    print_board(board_cell)
    print("Good game. Thanks for playing!")



def cells_of_board():
    board_cells=[]
    for cell in range(9):
        board_cells.append(cell +1)
    return board_cells

def print_board(board_cell):
    print()
    print(f"{board_cell[0]}|{board_cell[1]}|{board_cell[2]}")
    print("-+-+-")
    print(f"{board_cell[3]}|{board_cell[4]}|{board_cell[5]}")
    print("-+-+-")
    print(f"{board_cell[6]}|{board_cell[7]}|{board_cell[8]}")
    print()

def new_move(player, board_cell):
    number = int(input(f"{player}'s turn to choose a square (1-9): "))
    board_cell[number - 1] = player

def next_player(actual_player):
    if actual_player =="" or actual_player == "o":
       return "x"
    elif actual_player == "x":
        return "o"

def winner(board_cell):
    return(board_cell[0]==board_cell[1] == board_cell[2] or
          board_cell[3] == board_cell[4] == board_cell[5] or
          board_cell[6] == board_cell[7] == board_cell[8] or
          board_cell[0] == board_cell[3] == board_cell[6] or
          board_cell[1] == board_cell[4] == board_cell [7] or
          board_cell[2] == board_cell[5] == board_cell[8] or
          board_cell[0] == board_cell[4] == board_cell[8] or
          board_cell[2] == board_cell[4] == board_cell[6])

if __name__ == "__main__":
    main()