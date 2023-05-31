# Tic-Toc-Toe Game

board = [' '] * 9
current_player = 'X'
game_over = False

def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    # Check if the game is a draw
    if ' ' not in board:
        return 'Draw'
    # No winner yet
    return None

def play_game():
    global current_player, game_over
    print("Tick-Tock Game")
    print_board()
    while not game_over:
        position = input(f"{current_player}, choose a position (1-9): ")
        position = int(position) - 1
        if position < 0 or position > 8 or board[position] != ' ':
            print("Invalid move. Try again.")
            continue
        board[position] = current_player
        print_board()
        winner = check_winner()
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

play_game()
