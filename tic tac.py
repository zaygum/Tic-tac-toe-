import os
def startup():
    print("First one to select will have  marker set  as X and the second Player will have marker set to O By default")

def displayboard(board):
    print(str(board[0]) + ' ' + '|' + ' ' + str(board[1]) + ' ' + '|' + str(board[2]) + ' ')
    print('--' + '' + '|' + '' + '---' + '|' + '-- ')
    print(str(board[3]) + ' ' + '|' + ' ' + str(board[4]) + ' ' + '|' + str(board[5]) + ' ')
    print('--' + '' + '|' + '' + '---' + '|' + '-- ')
    print(str(board[6]) + ' ' + '|' + ' ' + str(board[7]) + ' ' + '|' + str(board[8]) + ' ')



def check(board, marker, selection):
    if board[0] == board[1] == board[2] == marker.upper():
        return marker
    elif board[3] == board[4] == board[5] == marker.upper():
        return marker
    elif board[6] == board[7] == board[8] == marker.upper():
        return marker
    else:
        return 'N'

def getmarker(marker):
    if marker=='x':
        marker='o'
        return  marker
    else:
        marker='x'
        return marker

def updateselection(board,marker,selection):
    if selection not in board:
        print("This selection  has been already marked  ,Please Try another")
        return 0
    else:
        indx = board.index(selection)
        board[indx] = marker.upper()
        return 1
def restartgame():
    os.system('cls')



if __name__ == '__main__':
    count=0
    marker='x'
    startup()
    board = [str(x) for x in range(1, 10)]
    while count<=9:
         displayboard(board)
         selection = input("Please make a selection from the board above :")
         result= updateselection(board, marker, selection)
         if result==1:
             wincheck=check(board, marker, selection)
             if wincheck =='N':
                 marker = getmarker(marker)
                 count = count + 1
             else:
                 print("Game Over !! " + marker.upper() + "  Wins!!" )
                 break
         else:
             check(board, marker, selection)
             count = count + 1
    if count==9:
        print("Board Full,Its a Tie")
    else:
        restartgame()





