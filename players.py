'''
players.py
Thura Aung
2nd May 2020
'''
import random
import math

class Player():
    def __init__(self,marker):
        self.marker = marker
    def makeMove(self,game):
        pass

class HumanPlayer(Player):
    def __init__(self,marker):
        super().__init__(marker)
    def makeMove(self,game):
        free_pos = False
        while not free_pos:
            position = int(input(self.marker + "\'s turn. Input the move(0-9):"))
            try:
                if position not in game.avaliablePos():
                    raise ValueError
                else:
                    free_pos = True
            except ValueError:
                print("This is invalid. Try again.")
        return position 

class RandomComputerPlayer(Player): #for easy mode
    def __init__(self,marker):
        super().__init__(marker)
    def makeMove(self,game):
        position = random.choice(game.avaliablePos())
        return position

class IntelligentComputerPlayer(Player): #for hard mode
    def __init__(self,marker):
        super().__init__(marker)
    def makeMove(self,game):
        if len(game.avaliablePos()) == 9:
            position = random.choice(game.avaliablePos())
        else:
            position = self.minimax(game,self.marker)['pos']
        return position
       
    def minimax(self,state,player):
        max_player = self.marker
        other_player = 'O' if player == 'X' else 'X'
        if state.current_winner == other_player:
            return {
                'pos' : None,
                'score' : 1*(state.numOfemptyPos() + 1) if other_player == max_player else (-1)*(state.numOfemptyPos() + 1)
            } #score is the utility 
        elif not state.emptyPos():
            return {
                'pos': None,
                'score' : 0
            }
        if player == max_player:
            best = {
                'pos' : None,
                'score' : -math.inf # each score should maximize
            }
        else:
            best = {
                'pos' : None,
                'score' : math.inf
            }
        for possible_moves in state.avaliablePos():
            state.checkMove(possible_moves,player)
            simulate_scores = self.minimax(state,other_player)
            
            state.board[possible_moves] = ' '
            state.current_winner = None
            simulate_scores['pos'] = possible_moves

            if player == max_player:
                if simulate_scores['score'] > best['score']:
                    best = simulate_scores
            elif simulate_scores['score'] < best['score']:
                    best = simulate_scores
            else:
                pass
        return best

        