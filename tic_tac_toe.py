#Tic Tac Toe
import random

def drawboard(board):
    #This function prints out the board
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")

def inputPlayerLetter():
     #This function lets the player decide what letter they choose
     letter = ""
     while not (letter == "X" or letter == "O"):
         print("Do you want to be X or O?")
         letter = input().upper()

     if letter == "X":
        return ["X","O"]
     if letter == "O":
        return ["O","X"]


def whoGoesFirst():
    #This function randomly decides who goes first
    if random.randint(0,1) == 0:
        return "Computer"
    else:
        return "Player"

def playAgain():
    #This function asks the player whether they want to play another game
    print("Do you want to play another game?(Yes or No)")
    return input().lower().startswith("y")

def makeMove(board, letter, move):
    #This code makes a move on the board
    board[move] = letter

def isWinner(bo, le):
    #Given a board and a player's letter, this function checks whether a player has won
    #The function returns true if a player has won
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or #across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or #across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or #down the left
            (bo[8] == le and bo[5] == le and bo[2] == le) or #down the centre
            (bo[9] == le and bo[6] == le and bo[3] == le) or #down the riight
            (bo[7] == le and bo[5] == le and bo[3] == le) or #diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) #diagonal

def getBoardCopy(board):
    #this function is to duplicate the board list and return the duplicate
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    #This function returns true if the space position played is free on the board
    #returns true if passed move is free on the passed board
    return board[move] == " "

def getPlayerMove(board):
    #This function lets the player type in their move
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("What is your next move?(1-9)")
        move = input()
    return int(move)
    
def chooseRandomMoveFromList(board, movesList):
    #This code returns a move from the possible move list passed into the code
    #returns None if there is no valid move
    possiblemove = []
    for i in movesList:
        if isSpaceFree(board,i):
            possiblemove.append(i)
            #This section checks if the board number is free
            #if the board number is empty, the number is added to the possible move list

    if len(possiblemove) != 0:
        return random.choice(possiblemove)
    else:
        return None



def getComputerMove(board, computerLetter):
    #
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    for i in range(1,10):
        copy = getBoardCopy(board)
        
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy,computerLetter):
                return i

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    
#Try to take one of the corners, if they are free
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

#Try to take the centre if it's free
    if isSpaceFree(board, 5):
        return 5
    #take from one of the sides
    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    #Return True if every space on the board has been taken. Otherwise False
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

#Start of the game
print ("Welcome to Tic Tac Toe")

while True:
    #Reset the board
    theBoard = [" "] * 10

    playerLetter, computerLetter = inputPlayerLetter()

    turn = whoGoesFirst()
    print ("The " + turn + " will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "Player":
            drawboard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawboard(theBoard)
                print ("Hooray! You have won the game")
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawboard(theBoard)
                    print ("The game is tied")
                    break
                    #gameIsPlaying = False
                else:
                    turn = "Computer"

        else:
            #Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawboard(theBoard)
                print("The computer has beaten you! You lose")
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawboard(theBoard)
                    print("The game is a tie")
                    break
                else:
                    turn = "Player"
    if not playAgain():
        break
                        
        



    

    
    
                    
                                    

          
    
     
