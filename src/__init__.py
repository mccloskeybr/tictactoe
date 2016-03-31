from src import game, ai
import os, subprocess

###

tictactoe = game.TicTacToe()
bot = ai.AI()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def userMakeMove():
    x = raw_input(" > What is the x position? (0-2) > ")
    y = raw_input(" > What is the y position? (0-2) > ")

    while tictactoe.playMove(int(x), int(y)) is False:
        x = raw_input(" > What is the x position? (0-2) > ")
        y = raw_input(" > What is the y position? (0-2) > ")

while True:

    tictactoe.newGame()

    while True:

        bot.decideMove(tictactoe)
        tictactoe.printBoard()

        if game.checkForWin(tictactoe.board) is not None:
            break

        userMakeMove()

        if game.checkForWin(tictactoe.board) is not None:
            break

    if game.checkForWin(tictactoe.board) is 0:
        print("\n > Tie!\n > New game...\n")
    else:
        print("\n > Someone won the game!\n > New game...\n")