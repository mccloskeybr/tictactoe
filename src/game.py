
class TicTacToe:

    board =\
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    _xTurn = None

    def __init__(self):
        pass

    # Empties the board
    def newGame(self):

        self._xTurn = True
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = 0

    # Plays a move then switches the turn
    # Returns True if successfully played move
    def playMove(self, x, y):

        if self.board[y][x] is 0:

            if self._xTurn is True:
                self.board[y][x] = 1

            else:
                self.board[y][x] = -1

            self._xTurn = not self._xTurn

            return True

        return False

    # Prints the game board
    def printBoard(self):

        for i in range(len(self.board)):
            str = ""
            for j in range(len(self.board[i])):
                if self.board[i][j] is 0:
                    str += "   "
                elif self.board[i][j] is 1:
                    str += " X "
                else:
                    str += " O "

                if j < 2:
                    str += "|"

            print(str)

            if i < 2:
                print("--- --- ---")

# End TicTacToe

# Checks for a win
# If X has won, return 1
# If O has won, return -1
# If tie, return 0
# If no one has won, return None
def checkForWin(board):

    # Horizontal wins

    if board[0][0] is board[0][1] and board[0][0] is board[0][2] and board[0][0] is not 0:
        return board[0][0]
    if board[1][0] is board[1][1] and board[1][0] is board[1][2] and board[1][0] is not 0:
        return board[1][0]
    if board[2][0] is board[2][1] and board[2][0] is board[2][2] and board[2][0] is not 0:
        return board[2][0]

    # Vertical wins

    if board[0][0] is board[1][0] and board[0][0] is board[2][0] and board[0][0] is not 0:
        return board[0][0]
    if board[0][1] is board[1][1] and board[0][1] is board[2][1] and board[0][1] is not 0:
        return board[0][1]
    if board[0][2] is board[1][2] and board[0][2] is board[2][2] and board[0][2] is not 0:
        return board[0][2]

    # Diagonal wins

    if board[0][0] is board[1][1] and board[0][0] is board[2][2] and board[0][0] is not 0:
        return board[0][0]
    if board[0][2] is board[1][1] and board[0][2] is board[2][0] and board[0][2] is not 0:
        return board[0][2]

    # Check for tie

    full = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is 0:
                full = False

    if full is True:
        return 0

    return None