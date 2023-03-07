from os import system, name
from time import sleep

class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
    
    def __str__(self):
        string = "   0   1   2\n"
        line_count = 0

        for line in self.board:
            string += f"{line_count}  {line[0]} | {line[1]} | {line[2]}\n"
            line_count += 1

        return string

def verify_valid_action(board, line, column):
        if board[line][column] == ' ':
            return True
        
        return False

def copy_board(board):
    copy = []
    copy.append(board[0].copy())
    copy.append(board[1].copy())
    copy.append(board[2].copy())

    return copy

def test_terminal_state(board):
        """ 
            Returns 0 if it's not a terminal state, 1 if 'O' wins, 2 if it's a tie and 3 if 'X' wins.
        """
        tied = True

        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if(board[0][0] == 'X'):
                return 3
            elif(board[0][0] == 'O'):
                return 1

        if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
            if board[2][0] == 'X':
                return 3
            elif board[2][0]=='O':
                return 1

        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                if board[i][0] == 'X':
                    return 3
                elif board[i][0] == 'O':
                    return 1

            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                if board[0][i] == 'X':
                    return 3
                elif board[0][i] == 'O':
                    return 1
        
        for i in range(3):
            if ' ' in board[i]:
                tied = False

        if tied:
            return 2

        return 0

def print_game_menu():
    clear_console()

    print("-- TIC-TAC-TOE --\n")
    print("[1] Play (Player x CPU)")
    print("[2] Play (CPU x CPU)")
    print("[3] Quit game")
    print()

def max_action(board):
  actions = []
  utility = test_terminal_state(board)

  if utility:
    return [utility, board]
  
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        board_copy = copy_board(board)
        board_copy[i][j] = 'X'
        
        actions.append([0, board_copy])
  
  for action in actions:
    min_response = min_action(action[1])
    action[0] = min_response[0]

  return max(actions)

def min_action(board):
  actions = []
  utility = test_terminal_state(board)
  
  if(utility):
    return [utility, board]
  
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        board_copy = copy_board(board)
        board_copy[i][j] = 'O'
        
        actions.append([0, board_copy])
  
  for action in actions:
    max_response = max_action(action[1])
    action[0] = max_response[0]

  return min(actions)

def print_player_turn(game, player):
    clear_console()
    print(game)
    print(f"Your turn. ({player})\n")

def player_turn(game, player):
    print_player_turn(game, player)
    
    while True:
        while True:
            line_input = int(input("What line do you want? "))
            
            if line_input not in [0, 1, 2]:
                print_player_turn(game, player)      
                print("Enter a valid line!")
            else:
                break
        
        while True:
            column_input = int(input("What column do you want? "))
            
            if column_input not in [0, 1, 2]:
                print_player_turn(game, player)      
                print("Enter a valid line!")
            else:
                break
        
        if not verify_valid_action(game.board, line_input, column_input):
            print_player_turn(game, player)
            print("This position is already taken, enter an empty board position.\n")
        else:
            break
    
    player_turn_board = copy_board(game.board)
    player_turn_board[int(line_input)][int(column_input)] = player

    return player_turn_board

def cpu_turn(game, player):
    print(f"CPU turn! ({player})")

    if player == 'X':
        cpu_action = max_action(game.board)
    else:
        cpu_action = min_action(game.board)

    board = cpu_action[1]

    return board

def tic_tac_toe(cpu_only = False):
    game = TicTacToe()
    x_turn = False
    players_turn = True
    game_over = False
    
    clear_console()
    print(game)

    while not game_over:
        if x_turn:
            if cpu_only or not players_turn:
                board = cpu_turn(game, 'X')
            else:
                board = player_turn(game, 'X')
        else:
            if cpu_only or not players_turn:
                board = cpu_turn(game, 'O')
            else:
                board = player_turn(game, 'O')

        game.board = copy_board(board)
        x_turn = not x_turn
        players_turn = not players_turn
        
        sleep(1)
        clear_console()
        print(game)

        game_status = test_terminal_state(game.board)

        if game_status == 1:
            game_over = True
            print("'O' Victory!")
            sleep(2)
        elif game_status == 3:
            game_over = True
            print("'X' Victory!")
            sleep(2)
        elif game_status == 2:
            game_over = True
            print("Game Tied!")
            sleep(2)
            
def clear_console():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def main_menu():
    print_game_menu()
    
    while True:
        user_input = input()

        if user_input == "1":
            tic_tac_toe(False)
            return False
        elif user_input == "2":
            tic_tac_toe(True)
            return False
        elif user_input == "3":
            return True
        else:
            print_game_menu()
            print("Invalid input. You should enter one of the menu options.")

def print_play_again():
    clear_console()
        
    print("Do you want to play again?\n")
    print("[1] Yes")
    print("[2] No")

def play_again():
    print_play_again()

    while True:
        user_input = input()

        if user_input == "1":
            return True
        elif user_input == "2":
            return False
        else:
            print_play_again()
            print("Invalid input. You should enter one of the menu options.")
    
def main():
    quit = False
    game = TicTacToe()

    while not quit:
        quit = main_menu()
        
        if not quit:
            sleep(2)
            
            quit = not play_again()

if __name__ == "__main__":
    main()