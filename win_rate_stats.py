# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:56:59 2021

@author: trber
"""

import numpy as np

import make_player_test as mp

from random import shuffle

current_gen = 1

match_pairs = np.zeros([16,2])

def win_check(current_board):

    boardflip = np.fliplr(current_board)

    if 3 in np.abs(current_board.sum(axis=0)) or 3 in np.abs(current_board.sum(axis=1)) or np.abs(np.trace(current_board)) == 3 or np.abs(np.trace(boardflip)) == 3:
        #print('winner winner')
        return(True)
    else:
        return(False)

def make_pairs():
    peeps  = [i for i in range(1,33)]
    shuffle(peeps)
    for i in range(16):
        match_pairs[i, 0] = peeps[i]
        match_pairs[i, 1] = peeps[i+16]
    return(match_pairs)    
        
def play_game(p1, p2, gen):
    
    gameBoard = np.zeros([3,3])
    mp.data = np.loadtxt('run1gen'+ str(gen) +'.csv', delimiter = ',')
    
    p1.update_players()
    p2.update_players()
    
    def make_move_p(player, identity):
        game_inputAbs = np.reshape(gameBoard, 9)
        mp.game_input = game_inputAbs * player
        
        A = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])
        B = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
        
        if 0 in gameBoard:
            movex = B[identity.make_move()]
            movey = A[identity.make_move()]
            gameBoard[int(movey)-1,int(movex)-1]=player
            game_inputAbs = np.reshape(gameBoard, 9)
        #else:
            #print('a tie')
            
    for i in range(5):
        make_move_p(1, p1)
        #print(gameBoard)
        if win_check(gameBoard) == True:
            #print('p1 wins')
            return(1)
            break
        make_move_p(-1, p2)
        #print(gameBoard)
        if win_check(gameBoard) == True:
            #print('p2 wins')
            return(-1)
            break
    if win_check(gameBoard) == False:
        return(2)

def step_gen():
    make_pairs()
    global current_gen
    x = np.zeros(16)
    for i in range(16):
        p1 = mp.Player(int(match_pairs[i,0]))
        p2 = mp.Player(int(match_pairs[i,1]))
        x[i] = play_game(p1, p2, current_gen)
    wins = np.count_nonzero(x == 1)
    loss = np.count_nonzero(x == -1)
    ties = np.count_nonzero(x == 2)
    a = np.array([wins, loss, ties])
    return(a)

def run_win_rate(firstgen, lastgen):
    global current_gen
    current_gen = firstgen
    b = np.zeros([lastgen-firstgen+1,4])
    for i in range(firstgen,lastgen+1):
        b[i-firstgen,0] = i
        b[i-firstgen,1:4] = step_gen()
        current_gen += 1
        print(current_gen)
    return(b)

#b = np.zeros([20,4])

#current_gen = 1

#for i in range(1,21):
    #b[i-1,0] = i
    #b[i-1,1:4] = step_gen()
    #current_gen += 1

#print(b)

#print(run_win_rate(1990,2000))
np.savetxt('win_rate_stats_t3_gen2500-3500.csv', run_win_rate(2500,3500) , delimiter = ',')
        
        