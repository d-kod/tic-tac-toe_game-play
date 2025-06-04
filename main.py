import numpy as np

board = np.zeros((3, 3), dtype=str)
board.fill("") # Initialize the board with empty strings

#player symbols
player1 = "X"
player2 = "O"

#game state variables
game_running = True
winner = None
move_count = 0

#players
players = [player1, player2]
current_player_index = 0

# Start with player1
current_player = players[current_player_index]  

#scores
score_x = 0
score_o = 0
games_played = 0

#display words


#function to switch players
def switch_player():
    global current_player
    if current_player == player1 :
        current_player = player2 
    else:
        current_player = player1

#display the current board
def display_board():
 for i, row in enumerate(board):
        #convert numbers to strings for display
    formatted_cells = []
    for cell in row:
            formatted_cells.append(cell if cell else " ")
    
    # Join cells with " | " separators
    row_display = " | ".join(formatted_cells)
    print(row_display)
    
    # Add horizontal line after first 2 rows
    if i < 2:
        print("-" * 9)


#player input handling
def get_player_move(current_player):
    while True:
        try:
            print(f"\nPlayer {current_player}'s turn")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Check if coordinates are within bounds
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Error: Coordinates must be between 0 and 2")
                continue
                
            # Check if cell is empty
            if board[row][col] != "":
                print("Error: That cell is already occupied!")
                continue
                
            return (row, col)
            
        except ValueError:
            print("Error: Please enter numbers only!")

#make a move on the board
def make_move(row, col):
    global move_count
    board[row][col] = current_player
    move_count += 1    
    
#check for a win condtition
def check_winner():
    global winner
    #last player to make a move is the current player
    last_player = current_player[current_player_index] 
    #check rows
    for row in board:
            if all( cell == current_player for cell in row) and all (cell != "" for cell in row):
               winner = last_player
               
               return True

    #check columns
    for col in range(3):
        if all(board[row][col] == current_player for row in range(3)) and all(board[row][col] != "" for row in range(3)):
            winner = last_player
            
            return True
    #check diagonals
    #diagonal
    if all( np.diag(board) == current_player) and all(np.diag(board) != ""):
           winner = last_player

           return True    
    #anti-diagonal
    if all( np.diag(np.fliplr(board)) == current_player) and all(np.diag(np.fliplr(board)) != ""):
           winner = last_player
        
           return True
        
    


#check for a draw condition
def check_draw():
    return move_count == 9 and winner is None
    

#reset the game state
def reset_game():
    #everything is reset to the initial state
    global board, move_count, winner, game_running, games_played, score_x, score_o
    global current_player, current_player_index
    board = np.zeros((3, 3), dtype=str)
    board.fill("")  # Reset the board to empty strings
    move_count = 0
    winner = None
    game_running = True
    games_played = 0
    score_x = 0
    score_o = 0
    current_player = player1
    current_player_index = 0  # Reset to player1

#replay the game
def replay_game():
    #only the board, game state and move_count are reset but the scores and games player are retained
    global board, move_count, winner, game_running
    global current_player, current_player_index
    board = np.zeros((3, 3), dtype=str)
    board.fill("")  # Reset the board to empty strings
    move_count = 0
    winner = None
    game_running = True
    current_player = player1
    current_player_index = 0  # Reset to player1
    print("Starting a new game...")
    main_gameplay()  # Start the main game loop again

#ask the player if they want to play again
def ask_replay():
    global game_running, score_x, score_o, games_played
    while True:
        #ask the player if they want to play again
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay == "yes":
            replay_game()
            return True
        elif replay == "no":
            print(f"Final Scores: Player X: {score_x}, Player O: {score_o}, Games Played: {games_played}")
            print("Thanks for playing! Goodbye!")
            game_running = False
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")  

#Main game loop 
def main_gameplay():
    global game_running, score_x, score_o, games_played
    print("Tic Tac Toe Game ")
    print("Board positions are referenced by row and column (0-2)") 
    print("Player1 goes first")
    print(f"Game running: {game_running}")


    while game_running == True:
        #display the board
        display_board()

        #get player move
        row,col = get_player_move(current_player)

        #make the move
        make_move(row,col)
        #display the updated board 
        display_board()
        print(f"Player {current_player} made a move at ({row}, {col})")

        #check for a winner
        if (check_winner()):
            display_board()
            print(f" 🎉 Player {winner} wins! 🎉 ")
            if winner == player1:
                score_x += 1
                games_played += 1 
                game_running = False
                
                break
            else:
                score_o += 1
                games_played += 1
                game_running = False 
                
                break
                       
        #check for a draw
        elif check_draw():
            display_board()
            print("It's a draw! 🤝 ")
            game_running = False 
            games_played += 1
            break
            
            
            
 
        #check if the game should continue
        else:
            #switch players
            switch_player()

    #ask if the player wants to replay or reset the game
    ask_replay()
    
        

           

#start the game
if __name__ == "__main__":
    main_gameplay()
   




