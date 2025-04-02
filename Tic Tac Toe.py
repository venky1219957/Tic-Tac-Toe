# Tic Tac Toe in Python

# Function to print the board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", " ".join(board[i]), "|")
    print("-------------")

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Check diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Check reverse diagonal
        return True
    
    return False

# Function to check if the board is full
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize an empty board
    current_player = "X"
    
    while True:
        print_board(board)
        
        # Get player move
        move = input(f"Player {current_player}, enter your move (row col): ").split()
        row, col = int(move[0]), int(move[1])
        
        # Validate the move
        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move! Try again.")
            continue
        
        # Make the move
        board[row][col] = current_player
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
if _name_ == "_main_":
    play_game()
