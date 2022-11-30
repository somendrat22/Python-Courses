class MainImpl:

    def __init__(self, board, user1, user2):
        self.board = board
        self.user1 = user1
        self.user2 = user2
    
    def placeCharacters(self, row, col, gameCharacter):
        self.board.board[row][col] = gameCharacter
        val = 0
        if gameCharacter == 'X':
            val = -1
        else:
            val = 1

        self.board.rows[row] += val
        self.board.cols[col] += val

        if row == col: # This condition for dig
            self.board.dig += val
        
        if row + col == 2: # This condition for antiDig 
            self.board.antiDig += val

        
        if(self.board.rows[row] == 3 or self.board.cols[col] == 3 or self.board.antiDig == 3 or self.board.dig == 3):
            return 1 # Winning condition 

        return -1 # Nobody Win Lets continuue 