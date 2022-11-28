class Board:

    def __init__(self):
        self.rows = [0, 0, 0]
        self.cols = [0, 0, 0]
        self.dig = 0
        self.antiDig = 0
        self.board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]

    def displayBoard(self):

        for i in range(0,3):
            for j in range(0,3):
                print(self.board[i][j], end="\t")
            print("\n")
    