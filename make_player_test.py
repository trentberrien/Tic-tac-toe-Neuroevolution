# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 20:07:11 2021

@author: trber
"""

import numpy as np

data = np.loadtxt('run4gen1.csv', delimiter = ',')

gb_static = np.array([[0,0,0],
                      [0,0,0],
                      [0,0,0]])

game_input = np.reshape(gb_static, 9)

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

class Player:
    
    def __init__(self, name):
        self._name = name
        self._data = data[name - 1, 1:183]
        
    def update_players(self):
        self._data = data[self._name - 1, 1:183]
        
    def get_weights1(self):
        n = 9
        W = np.zeros([n, n])
        d = 19
        for j in range(n):
            W[j, :] = self._data[d:d+n]
            d += n
        return W
    
    def get_weights2(self):
        n = 9
        W = np.zeros([n, n])
        d = 100
        for j in range(n):
            W[j, :] = self._data[d:d+n]
            d += n
        return W
    
    def get_bias1(self):
        n = 9
        d = 1
        B = self._data[d:d+n]
        return B
    
    def get_bias2(self):
        n = 9
        d = 10
        B = self._data[d:d+n]
        return B
    
    def make_move(self):
        lay1a = (self.get_weights1() @ game_input) + self.get_bias1()
        lay1b = np.tanh(lay1a)
        lay2a = (self.get_weights2() @ lay1b) + self.get_bias2()
        lay2b = softmax(lay2a)
        
        for i in range(9):
            if game_input[i] != 0:
                lay2b[i] = -1 * 10**10

        return np.argmax(lay2b)
    
    
#Player1 = Player(5)
#Player2 = Player(10)

#print(Player1.make_move())
#print(Player2.make_move())