def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[0 for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        player_choice = input(f"Player {players[current_player]}: Enter row,col (e.g. 1,2) -> ")
        row, col = map(int, player_choice.split(','))
        if board[row][col] != 0:
            print("Invalid move, try again.")
            continue
        board[row][col] = players[current_player]
        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            return
        current_player = (current_player + 1) % 2

        if all(all(row) for row in board):
            print_board(board)
            print("Game over: Tie!")
            return

if __name__ == "__main__":
    tic_tac_toe()