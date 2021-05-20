# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:43:24 2021

@author: trber
"""

import numpy as np

import make_player_test as mp

import math

def win_check(current_board):

    boardflip = np.fliplr(current_board)

    if 3 in np.abs(current_board.sum(axis=0)) or 3 in np.abs(current_board.sum(axis=1)) or np.abs(np.trace(current_board)) == 3 or np.abs(np.trace(boardflip)) == 3:
        #print('winner winner')
        return(True)
    else:
        return(False)
   
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
        else:
            print('a tie')
            #tie = True
            
    for i in range(5):
        make_move_p(1, p1)
        print(gameBoard)
        if win_check(gameBoard) == True:
            print('p1 wins')
            return(p1._name)
            break
        make_move_p(-1, p2)
        print(gameBoard)
        if win_check(gameBoard) == True:
            print('p2 wins')
            return(p2._name)
            break
    if win_check(gameBoard) == False:
        x = np.random.uniform(0,1)
        if x > .5:
            print('p1 wins on tie')
            return(p1._name)
        else:
            print('p2 wins on tie')
            return(p2._name)
        
def play_game_hvb(p1, gen, starter):
    
    gameBoard = np.zeros([3,3])
    mp.data = np.loadtxt('run4gen'+ str(gen) +'.csv', delimiter = ',')
    
    p1.update_players()
    
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
        else:
            print('a tie')
            
    def make_move_h(player):
        moveMade = False
        
        if 0 in gameBoard:
            while moveMade == False:
                movex, movey = input("coulumn row: ").split()
                if gameBoard[int(movey)-1,int(movex)-1] == 0:
                    gameBoard[int(movey)-1,int(movex)-1]=player
                    moveMade = True
        else:
            print('a tie')
            
    for i in range(5):
        make_move_p(1, p1)
        print(gameBoard)
        if win_check(gameBoard) == True:
            print('p1 wins')
            break
        make_move_h(-1)
        print(gameBoard)
        if win_check(gameBoard) == True:
            print('p2 wins')
            break
        
def play_game_rvb(p1, gen, starter):
    
    gameBoard = np.zeros([3,3])
    mp.data = np.loadtxt('run4gen'+ str(gen) +'.csv', delimiter = ',')
    
    p1.update_players()
    
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
            
    def make_move_r(player):
        game_inputAbs = np.reshape(gameBoard, 9)
        A = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])
        B = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
        
        if 0 in gameBoard:
            c = 9 - np.count_nonzero(game_inputAbs == 1) - np.count_nonzero(game_inputAbs == -1)
            x = np.random.uniform(0,c)
            x = math.floor(x)
            a = 0
            for i in range(9):
                if game_inputAbs[i] == 0:
                    if a == x:
                        movex = B[i]
                        movey = A[i]
                        gameBoard[int(movey)-1,int(movex)-1]=player
                        break
                    else:
                        a += 1
        #else:
            #print('a tie')
     
    if starter == 1:
        for i in range(5):
            make_move_p(1, p1)
            #print(gameBoard)
            if win_check(gameBoard) == True:
                #print('p1 wins')
                return(2)
                break
            make_move_r(-1)
            #print(gameBoard)
            if win_check(gameBoard) == True:
               #print('p2 wins')
               return(0)
               break
    else:
        for i in range(5):
            make_move_r(1)
            #print(gameBoard)
            if win_check(gameBoard) == True:
                #print('p1 wins')
                return(0)
                break
            make_move_p(-1, p1)
            #print(gameBoard)
            if win_check(gameBoard) == True:
               #print('p2 wins')
               return(2)
               break
    if win_check(gameBoard) == False:
        return(1)

#Player1 = mp.Player(1)
#play_game_rvb(Player1, 1, 2)
