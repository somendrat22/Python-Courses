from Board.Board import Board
from User.User import User
from MainImpl.MainImpl import MainImpl
import random

user1Name = input("Please Enter Name For User1 : ")
user2Name = input("Please Ebter Name For User2 : ")
mainBoard = Board()


user1 = User(user1Name, "O");
user2 = User(user2Name, "X");


tossNum = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

firstMoveUser = "" 
secondMoveUser = ""

if tossNum%2 == 1: # It means user2 won the toss. So user1 will be the first one to take the move 
    firstMoveUser = user2
    secondMoveUser = user1
else:
    firstMoveUser = user1
    secondMoveUser = user2

moves = 0

mainImpl = MainImpl(mainBoard, firstMoveUser, secondMoveUser)
won = False
while moves < 9:
    currUser = ""
    if moves%2 == 0:
        currUser = firstMoveUser
    else:
        currUser = secondMoveUser
    
    mainBoard.displayBoard()
    row = int(input("{} please enter the row value where you want to place your {} : ".format(currUser.name, currUser.gameCharacter)))
    col = int(input("{} please enter the col value where you want to place your {} : ".format(currUser.name, currUser.gameCharacter)))

    if row >= 3 or row < 0 or col >= 3 or col < 0:
        print("{} you are entering values out of the box. Please think accordingly".format(currUser.name))
        continue
    
    if mainImpl.board.board[row][col] !=  '_': 
        print("{} cell with {} & {} is already used. Please consider some different cell".format(currUser.name, row, col))
        continue

    res = mainImpl.placeCharacters(row, col, currUser.gameCharacter)

    if res == 1:
        print("Congratulations !! {} you won the game".format(currUser.name))
        mainBoard.displayBoard()
        won = True
        break
    
    moves += 1
    
if won == False:
    print("Its a tie")
    mainBoard.displayBoard()
