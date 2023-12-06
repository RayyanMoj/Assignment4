
continuegame = True
winner = None
player = "X"

options = [1,2,3,4,5,6,7,8,9]
board = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
rows = 3
columns = 3

def tic_tac_draw():#prints tic tac toe game board
    for x in range(rows):
        print("\n|", end="")
        for y in range(columns):
            print("", board[x][y], end= " |")

    print("\n")


def editboard(board):

    num = int(input("Enter a value from 1-9, the numbers follow the grind pattern"))

    num -= 1
    if(num == 0 and board[0][0] == "-"):
        board[0][0] = player
    if (num == 1 and board[0][1] == "-"):
        board[0][1] = player
    if (num == 2 and board[0][2] == "-"):
        board[0][2] = player
    if (num == 3 and board[1][0] == "-"):
        board[1][0] = player
    if (num == 4 and board[1][1] == "-"):
        board[1][1] = player
    if (num == 5 and board[1][2] == "-"):
        board[1][2] = player
    if (num == 6 and board[2][0] == "-"):
        board[2][0] = player
    if (num == 7 and board[2][1] == "-"):
        board[2][1] = player
    if (num == 8 and board[2][2] == "-"):
        board[2][2] = player


def checkacross(board):
    global winner
    if board[0][0] == board[0][1] == board[0][2]:
        winner = board[0][0]
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        winner = board[1][0]
        return True
    elif board[2][0] == board[2][1] == board[2][2]:
        winner = board[2][0]
        return True
def checkdown(board):
    global winner
    if board[0][0] == board[1][0] == board[2][0]:
        winner = board[0][0]
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        winner = board[0][1]
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        winner = board[0][2]
        return True

def checkdiagonal(board):
    global winner
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return True

def checkTie(board):
    for row in board:
        for cell in row:
            if cell == "-":
                return False
    return True


def switchplayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def checkcwinner():
    global winner
    if checkacross(board) or checkdiagonal(board) or checkdown(board):

        print(f"The winner is {winner}")

while continuegame:
    tic_tac_draw()
    editboard(board)
    if checkcwinner():
        print(f"The winner is {winner}")
        continuegame = False
        break

    if checkTie(board):
        print("its a tie!")
        break
    switchplayer()

