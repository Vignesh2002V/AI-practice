import random

# Define the game board as a list of lists
board = [['-' for _ in range(3)] for _ in range(3)]

# Define the possible winning combinations
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def print_board():
    for row in board:
        print(row)

def check_win(player):
    for win in wins:
        if all(board[i // 3][i % 3] == player for i in win):
            return True
    return False

def user_play():
    while True:
        try:
            x, y = map(int, input("Your turn. Enter the row and column (0-2) of your play: ").split())
            if board[x][y] == '-':
                board[x][y] = 'X'
                break
            else:
                print("This cell is already filled. Please choose another cell.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except IndexError:
            print("Invalid input. Please enter valid numbers.")

def ai_play():
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if board[x][y] == '-':
            board[x][y] = 'O'
            break

def game():
    while True:
        print_board()
        user_play()
        if check_win('X'):
            print("You win!")
            break
        ai_play()
        if check_win('O'):
            print("PC wins!")
            break
    print_board()

game()
