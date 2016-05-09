#http://www.codeskulptor.org/#user41_IdhtbXlc7g_14.py

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def my_trail(board, player):
    '''empty_lis = []
    for hang in range(board.get_dim()):
            for lie in range(board.get_dim()):
                if board[hang][lie] == provided.EMPTY:
                    empty_lis.append((hang,lie))'''
    empty_lis = board.get_empty_squares()
    while len(empty_lis) != 0:
        row, column = random.choice(empty_lis)
        empty_lis.remove((row,column))
#       board[row][column] = provided.player
        board.move(row, column, player)
        player = provided.switch_player(player)
        if board.check_win() != None:

            return board.clone()
    return




def mc_update_scores(scores, board, player):
    #print player
    #print board.check_win()
    if board.check_win() == player:
        for r in range(len(scores)):
            for c in range(len(scores[0])):
                #print player
                if board.square(r,c) == player:
                    #print player
                    scores[r][c] += SCORE_CURRENT
                elif board.square(r,c) == provided.EMPTY:
                    continue
                else:
                    scores[r][c] -= SCORE_OTHER
    elif board.check_win() == provided.switch_player(player):
        for r in range(len(scores)):
            for c in range(len(scores[0])):
                if board.square(r,c) == player:
                    scores[r][c] -= SCORE_CURRENT
                elif board.square(r,c) == provided.EMPTY:
                    continue
                else:
                    scores[r][c] += SCORE_OTHER
    return

def get_best_move(board, scores):
    empty_lis = board.get_empty_squares()
    if empty_lis != None:
        score_lis = [scores[a][b] for a,b in empty_lis]
        if len(score_lis) == 0:
            return
        max_score = max(score_lis)
        dic = {}
        for a,b in empty_lis:
            dic[scores[a][b]] = (a,b)

        return dic[max_score]

def mc_move(board, player, trails):
    scores = [[0 for _ in range(board.get_dim())]
              for _ in range(board.get_dim())]
    if board.check_win() == None:
        while trails != 0:
            my_trail(board.clone(), player)
            #print board.clone()
            mc_update_scores(scores,
                             my_trail(board.clone(), player),
                             player)
            trails -= 1
            #print scores
        if get_best_move(board, scores) != None:
            print scores
            row,col = get_best_move(board, scores)
            return (row,col)
        else:
            return (0,0)

print provided.EMPTY
print provided.PLAYERX
print provided.PLAYERO
print provided.DRAW


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(4, provided.PLAYERX, mc_move, NTRIALS, False)
