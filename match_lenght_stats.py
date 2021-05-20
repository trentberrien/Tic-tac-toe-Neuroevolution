# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:27:17 2021

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
    mp.data = np.loadtxt('run4gen'+ str(gen) +'.csv', delimiter = ',')
    
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
            #print('a tie, serus?')
            
    for i in range(5):
        make_move_p(1, p1)
        #print(gameBoard)
        if win_check(gameBoard) == True:
            #print('p1 wins lol')
            return(2*i+1)
            break
        make_move_p(-1, p2)
        #print(gameBoard)
        if win_check(gameBoard) == True:
            #print('p2 wins lol')
            return(2*i+2)
            break
    if win_check(gameBoard) == False:
        return(10)

def step_gen():
    make_pairs()
    global current_gen
    x = np.zeros(16)
    for i in range(16):
        p1 = mp.Player(int(match_pairs[i,0]))
        p2 = mp.Player(int(match_pairs[i,1]))
        x[i] = play_game(p1, p2, current_gen)
    len5 = np.count_nonzero(x == 5)
    len6 = np.count_nonzero(x == 6)
    len7 = np.count_nonzero(x == 7)
    len8 = np.count_nonzero(x == 8)
    len9 = np.count_nonzero(x == 9)
    len10 = np.count_nonzero(x == 10)
    
    #a = np.array([len5*5, len6*6, len7*7, len8*8, len9*9])
    #c = np.sum(a)
    #c /= 16
    c = np.array([len5, len6, len7, len8, len9, len10])
    return(c)

def run_match_len(firstgen, lastgen):
    global current_gen
    current_gen = firstgen
    b = np.zeros([lastgen-firstgen+1,7]) #,2])
    for i in range(firstgen,lastgen+1):
        b[i-firstgen,0] = i
        b[i-firstgen,1:] = step_gen() #get rid of :
        current_gen += 1
        print(current_gen)
    return(b)

np.savetxt('match_len_stats_4_gen1-1000_noavg.csv', run_match_len(1,1000) , delimiter = ',')