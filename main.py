from os import system, name

# board
# display board
# input 
# handling chances of each player
# check winner
   # columns
   # rows
   # diagonal
   # check draw
# update board values 


# global variables
board = ["-" , "-" , "-" ,
         "-" , "-" , "-" ,
          "-" , "-" , "-"]
player = "X"
game_still_running = True
winner = None
i = 1
valid = True


# clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# displaying the game board
def display_board():
    print(board[0], "|" , board[1] , "|" ,board[2], " "*15 , 1, "|" , 2 , "|" ,3)
    print(board[3], "|" , board[4] , "|" ,board[5], " "*15 , 4, "|" , 5 , "|" ,6)
    print(board[6], "|" , board[7] , "|" ,board[8], " "*15 , 7, "|" , 8 , "|" ,9)

# function to handlle turns of players
def handle_turns():
    global i 
    global player

    if i == 1:
        player = "O"
        i = 2

    else:
        player = "X"
        i = 1

    return player

#checks rows for set of 3
def check_rows():
    # checking if all values in a row is same and also not equal to "-"
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # if the value of any row is true then
    if row1 :
        return board[0]

    elif row2 :
        return board[3]

    elif row3 :
        return board[6]
    

#checks columns for set of 3
def check_column():
    # checking if all values in a column is same and also not equal to "-"
    column1 = board[0]==board[3]==board[6] != "-"
    column2 = board[1]==board[4]==board[7] != "-"
    column3 = board[2]==board[5]==board[8] != "-"

    # if the value of any column is true then
    if column1 :
        return board[0]

    elif column2 :
        return board[1]

    elif column3 :
        return board[2]

    
#checks diagonal for set of 3
def check_diagonal():
    # checking if all values in a diagonals is same and also not equal to "-"
    diagonal1 = board[0]==board[4]==board[8] != "-"
    diagonal2 = board[2]==board[4]==board[6] != "-" 

    # if the value of any diagonal is true then
    if diagonal1 :
        return board[0]

    elif diagonal2 :
        return board[2]

# checks if the game is tie
def check_tie():
    global game_still_running

    if "-" not in board:
        return True

#checks for winner
def check_winner(player):
    global game_still_running
    global winner

    # checking the return value from check_rows() fucntion
    if check_rows() == "X" or check_rows() == "O":
        winner = player

    # checking the return value from check_column() fucntion
    elif check_column() == "X" or check_column() == "O":
        winner = player

    # checking the return value from check_diagonal( fucntion
    elif check_diagonal() == "X" or check_diagonal() == "O":
        winner = player

    # checking True or False as return of check_tie() function
    elif check_tie():
        clear()
        print("its a tie")
        game_still_running = False
        display_board()

    # if a winner is decided than announcing it and ending game
    if winner == "X" or winner == "O":
        clear()
        print("Player" , "'"+str(winner)+"'", "has won")
        game_still_running = False
        display_board()
    

def update_values(chance,player):
    global valid

    if board[chance] == "-":
        board[chance] = player
        valid = True

    else:
        print("Place occupied")
        valid = False

# starting game
def play_game():
    global player
    try:
        while game_still_running:
            try:
                clear()
                display_board()
                print("Player" , player , "chance: ")
                chance = int(input("Enter a number between 1-9: ")) - 1

                while chance not in [0,1,2,3,4,5,6,7,8] and valid == True:
                    print("Invalid Input")
                    chance = int(input("Enter a number between 1-9: ")) - 1

                update_values(chance,player)
                check_winner(player)

                if valid == True:
                    player = handle_turns()
            except ValueError:
                print("Invalid input")
    except KeyboardInterrupt:
        clear()
        print("\nThank you for trying this game\n")
        
# starting game
play_game()