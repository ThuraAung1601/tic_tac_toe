import math
import time
import random
from tic_tat_toe import TicTatToe
from players import HumanPlayer,RandomComputerPlayer,IntelligentComputerPlayer
def play(game,X,O,playing = True):
    if playing:
        game.printBoardNums()
    #show the board format

    marker = random.choice(('X','O'))
    while game.emptyPos():
        if marker == 'O':
            position = O.makeMove(game)
        else:
            position = X.makeMove(game)
        if game.checkMove(position,marker):
            if playing:
                print(marker + " make a move to {}".format(position))
                game.printBoard()
            if game.current_winner:
                if playing:
                    print(marker + " win !")
                next = input("Next match ? y/n: ")
                if next == 'y' or next == 'Y':
                    return True
                else:
                    return False
            marker = 'O' if marker == 'X' else 'X'
        time.sleep(.8)
    if playing:
        print('It\'s a draw')
        next = input("Next match ? y/n: ")
        if next == 'y' or next == 'Y':
            return True
        else:
            return False
if __name__ == "__main__":
    bol = True
    while bol:
        ask = input("Choose game mode (E for Easy and H for Hard) :")
        if ask == 'E':
            X = RandomComputerPlayer('X')
        else:
            X = IntelligentComputerPlayer('X')
        O = HumanPlayer('O')
        game = TicTatToe()
        bol = play(game,X,O,playing=True)
