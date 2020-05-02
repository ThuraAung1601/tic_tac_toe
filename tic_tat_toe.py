'''
tic_tac_toe.py
Thura Aung
2nd May 2020
'''
class TicTatToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def printBoardNums():
        for row in [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def checkMove(self,position,marker):
        if self.board[position] == ' ':
            self.board[position] = marker
            if self.checkwin(position,marker):
                self.current_winner = marker
            return True
        return False

    def checkwin(self,position,marker):
        row_ind = position//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == marker for s in row]):
            return True
        col_ind = position % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == marker for s in column]):
            return True
        if position % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == marker for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == marker for s in diagonal2]):
                return True
        return False

    def emptyPos(self):
        return ' ' in self.board
    def numOfemptyPos(self):
        return self.board.count(" ")
    def avaliablePos(self):
        return [ i for i, x in enumerate(self.board) if x == " "]
