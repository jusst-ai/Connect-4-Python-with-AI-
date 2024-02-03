import random


POSSIBLE_LETTERS = "ABCDEFG"


rows = 6
cols = 7


def gameboard():
  """
    List outline of the connect 4 gameboard
    ()--> (List)
  """
  game_board = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
     ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
  return game_board
 
def print_game_board(game_board):
  
    print("\n     A   B   C   D   E   F   G  ", end="")
 
    for x in range(6):
        print("\n   +---+---+---+---+---+---+---+")
        print(x, " |", end="")
 
        for y in range(7):
            if game_board[x][y] == "O":
                print("", game_board[x][y], end=" |")
            elif game_board[x][y] == "X":
                print("", game_board[x][y], end=" |")
            else:
                print(" ", game_board[x][y], end=" |")
 
    print("\n   +---+---+---+---+---+---+---+")
 
 
 
def valid_input(game_board):
    """
    Gets a valid input from the user and checks if that position is on the board
    (list) -> (str)
    """
 
    while True:
        position = input("Enter a space: ")
        amount = 0
        if len(position) == 1 and position[0] in POSSIBLE_LETTERS:
          x = POSSIBLE_LETTERS.index(position[0])
          for y in range(rows-1, -1, -1):
            if game_board[y][x] == "":
              game_board[y][x] = "X"
              return (game_board)
            amount += 1
          if amount == 6:
            print("Column already full")
        else:
            print("Invalid entry")
 
 
 
def computer_turn(game_board):
   """
  (list) ->(list)
  Makes a move for the computer and checks if the move is a valid move
   """
   if checkvertical(game_board):
      return
   elif checkhorizontal(game_board):
      return
   elif check_diagonal(game_board):
      return
   elif check_diagonal2(game_board):
      return
   else:
      random_position(game_board)
     
def checkvertical(game_board):
  """
  (list) --> (bool)
  Looks over the board and sees if there are 3 pieces in a row for the other player vertically. If they are the computer blocks the player
  """
 
  for j in range(cols):
    for i in range(rows-1, -1, -1):
      if game_board[i][j] != "" and game_board[i][j] == game_board[i-1][j] == game_board[i-2][j] and i - 3 >= 0 and game_board[i-3][j] == "":
        game_board[i-3][j] = "O"
        return (True)
  return (False)


def checkhorizontal(game_board):
  """
  (list) --> (bool)
  Looks over the board and sees if there are 3 pieces in a row for the other player horizontally. If they are the computer blocks the player
   """
 
  for i in range(rows):
    for j in range(cols):
      if game_board[i][j] == "" and 1 <= j <= 5 and game_board[i][j-1] == "X" and game_board[i][j+1] == "X" and (i == 5 or game_board[i+1][j] != ""):
        game_board[i][j] = "O"
        return (True)
     
      elif game_board[i][j] == "" and j <= 3 and game_board[i][j+1] != "" and game_board[i][j+1] == game_board[i][j+2] == game_board[i][j+3] and (i == 5 or game_board[i+1][j] != ""):
        game_board[i][j] = "O"
        return (True)
     
      elif game_board[i][j] == "X" and j <= 4 and game_board[i][j+1] == "X" and game_board[i][j+2] == "" and (i == 5 or game_board[i+1][j+2] != ""):
        game_board[i][j+2] = "O"
        return (True)
  return (False)


def check_diagonal(game_board):
  """
  (list) --> (bool)
  Looks over the board and sees if there are 3 pieces in a row for the other player in a diagonal. If they are the computer blocks the player
  """
  # Check diagonally (top-left to bottom-right)
 
  for i in range(rows):
    for j in range(cols):
      if game_board[i][j] == "" and 1 <= i <= 4 and 1 <= j <= 5 and game_board[i+1][j+1] == "X" and game_board[i-1][j-1] == "X" and game_board[i+1][j] != "":
        game_board[i][j] = "O"
        return (True)
 
      elif game_board[i][j] == "" and i <= 2 and j <= 3 and game_board[i+1][j+1] != "" and game_board[i+1][j+1] == game_board[i+2][j+2] == game_board[i+3][j+3] and game_board[i+1][j] != "":
        game_board[i][j] = "O"
        return (True)
     
      elif game_board[i][j] == "X" and i <= 3 and j <= 4 and game_board[i+1][j+1] == "X" and game_board[i+2][j+2] == "" and (i+2 == 5 or game_board[i+3][j+2] != ""):
        game_board[i+2][j+2] = "O"
        return (True)
  return (False)
 
def check_diagonal2(game_board):
  """
  (list) --> (bool)
  Looks over the board and sees if there are 3 pieces in a row for the other player on the diagonal(top right to bottom left). If they are the computer blocks the player
   """
  # Check diagonally (top-right to bottom left)
 
  for i in range(rows):
    for j in range(cols):
      if 1 <= i <= 4 and 1 <= j <= 5  and game_board[i][j] == "" and game_board[i+1][j-1] == "X" and game_board[i-1][j+1] == "X" and game_board[i+1][j] != "":
        game_board[i][j] = "O"
        return (True)
 
      elif i <= 2 and j >= 3 and game_board[i][j] == "" and game_board[i+1][j-1] != "" and game_board[i+1][j-1] == game_board[i+2][j-2] == game_board[i+3][j-3] and game_board[i+1][j] != "":
        game_board[i][j] = "O"
        return (True)
     
      elif i <= 3 and j >= 2 and game_board[i][j] == "X" and game_board[i+1][j-1] == "X" and game_board[i+2][j-2] == "" and ((i+2 == 5) or game_board[i+3][j-2] != ""):
        game_board[i+2][j-2] = "O"
        return (True)
  return (False)
 
def random_position(game_board):
  """
  (list) --> (list)
  If their is no move where the opponent wins, it will randomly pick a spot to place the piece.
   """
  # If their is no move where the opponent wins, it will randomly pick a spot to place the piece


  while True:
    col = random.choice(POSSIBLE_LETTERS)
    x = POSSIBLE_LETTERS.index(col)
    for y in range(5, -1, -1):
      if game_board[y][x] == "":
        game_board[y][x] = "O"
        return 


def check_winner(game_board):
  """
  (bool)-->(Bool)
  Check for winner by checking horizontally, vertically, diagonally and if any of them are true it will print the winner 
  """
  player_win, ai_win = check_win_horizontal(game_board)


  if player_win:
     print ("\nYou won!")
     return True
 
  elif ai_win:
     print ("\nYou lost!")
     return True


  player_win, ai_win = check_win_vertical(game_board)
 
  if player_win:
     print ("\nYou won!")
     return True
 
  elif ai_win:
     print ("\nYou lost")
     return True
 
  player_win, ai_win = check_win_diagonal(game_board)


  if player_win:
     print ("\nYou won!")
     return True
 
  elif ai_win:
     print ("\nYou lost!")
     return True
 
  count = sum([sub_list.count("") for sub_list in game_board]) # The sum adds the count of "" within each list in the gameboard list


  if count == 0:
    print ("\nTie game!")
    return True
 
  return False


def check_win_horizontal(game_board):
  """
  (Bool)-->(Bool)
  THis function checks if ther are 4 X's or O's in a horizontal line.
  Returns true if check is successful
  """
  player_win = False
  ai_win = False
  for x in range(6):
    for y in range(4):
       if game_board[x][y] == game_board[x][y + 1] == game_board[x][y + 2] \
          == game_board[x][y + 3] and game_board[x][y] == "X":
          player_win = True
          return (player_win, ai_win)
       
       elif game_board[x][y] == game_board[x][y + 1] == game_board[x][y + 2] \
          == game_board[x][y + 3] and game_board[x][y] == "O":
          ai_win = True
          return (player_win, ai_win)
         
  return (player_win, ai_win)


def check_win_vertical(game_board):
  """
  (Bool)-->(Bool)
  THis function checks if ther are 4 X's or O's in a vertical line.
  Returns true if check is successful
  """
  
  player_win = False
  ai_win = False
  for x in range(3):
    for y in range(7):
       if game_board[x][y] == game_board[x + 1][y] == game_board[x + 2][y] \
        == game_board[x + 3][y] and game_board[x][y] == "X":
        player_win = True
        return (player_win, ai_win)
       
       elif game_board[x][y] == game_board[x + 1][y] == game_board[x + 2][y] \
        == game_board[x + 3][y] and game_board[x][y] == "O":
        ai_win = True
        return (player_win, ai_win)
       
  return (player_win, ai_win)


def check_win_diagonal(game_board):
  """
  (Bool)-->(Bool)
  THis function checks if ther are 4 X's or O's in a diagonal line.
  Returns true if check is successful
  """
  player_win = False
  ai_win = False


  # Check win top-left to bottom right


  for x in range(3):
    for y in range(4):
       if game_board[x][y] == game_board[x + 1][y + 1] == game_board[x + 2][y + 2] \
        == game_board[x + 3][y + 3] and game_board[x][y] == "X":
          player_win = True
          return (player_win, ai_win)
       
       elif game_board[x][y] == game_board[x + 1][y + 1] == game_board[x + 2][y + 2] \
        == game_board[x + 3][y + 3] and game_board[x][y] == "O":
          ai_win = True
          return (player_win, ai_win)
       
  # Check win top right to bottom left
 
  for x in range(3):
    for y in range(4):
       if game_board[x][y + 3] == game_board[x + 1][y + 2] == game_board[x + 2][y + 1]\
          == game_board[x + 3][y] and game_board[x][y + 3] == "X":
          player_win = True
          return (player_win, ai_win)
       
       elif game_board[x][y + 3] == game_board[x + 1][y + 2] == game_board[x + 2][y + 1]\
          == game_board[x + 3][y] and game_board[x][y + 3] == "O":
          ai_win = True
          return (player_win, ai_win)
       
  return (player_win, ai_win)
 


if __name__ == "__main__":
  game_board = gameboard()
  print("Welcome to Connect Four")
  print("To play the game enter any one of the columns which you want your piece to be dropped in. Letter must be capitalized")
  print("-----------------------")
 
  while True:
    print_game_board(game_board)
 
    if check_winner(game_board):
      break
 
    valid_input(game_board)


    if check_winner(game_board):
      print_game_board(game_board)
      break
       
    computer_turn(game_board)
       