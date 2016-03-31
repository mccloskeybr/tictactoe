from copy import deepcopy
from src import game
import sys

class AI:

    def __init__(self):
        pass

    def decideMove(self, tictactoe):

        board = tictactoe.board

        prob = []
        x = []
        y = []

        print (" > Thinking...")
        for i in range(len(board)):
            for j in range(len(board[i])):

                sys.stdout.write(". ")

                if board[i][j] is 0:
                    x.append(j)
                    y.append(i)

                    newBoard = deepcopy(board)
                    newBoard[i][j] = 1
                    prob.append(AI()._decideMove(newBoard, False))

        max = 0
        for i in range(len(prob)):
            if prob[i] > prob[max]:
                max = i

        print("")

        # Prints probability
        # print(prob)

        tictactoe.playMove(x[max], y[max])


    # Recursively fill a tree
    def _decideMove(self, board, isX):

        x = game.checkForWin(board)
        if x is not None:
            return float(x)

        avg = 0.0
        numEmptySpaces = 0.0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] is 0):
                    numEmptySpaces += 1
                    newBoard = deepcopy(board)
                    if isX is True:
                        newBoard[i][j] = 1
                        isX = False
                    else:
                        newBoard[i][j] = -1
                        isX = True

                    avg += AI()._decideMove(newBoard, isX)

        avg /= numEmptySpaces

        return avg

# End AI
