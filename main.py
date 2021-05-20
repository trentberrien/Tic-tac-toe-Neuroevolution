# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:14:58 2021

@author: trber
"""

import numpy as np

import make_player_test as mp

import new_gen_test as ng

import play_games_main as pg

from random import shuffle

import math

x = True

current_gen = 600

winner_array = np.ones([16])

match_pairs = np.zeros([16,2])

def make_pairs():
    peeps  = [i for i in range(1,33)]
    shuffle(peeps)
    for i in range(16):
        match_pairs[i, 0] = peeps[i]
        match_pairs[i, 1] = peeps[i+16]
    return(match_pairs)

def step_gen():
    global current_gen
    make_pairs()
    for i in range(16):
        p1 = mp.Player(int(match_pairs[i,0]))
        p2 = mp.Player(int(match_pairs[i,1]))
        winner_array[i] = pg.play_game(p1, p2, current_gen)
    print(winner_array)
    ng.new_gen(current_gen, winner_array)
    current_gen += 1
    
def step_gen_r():
    n = 5
    global current_gen
    peeps  = [i for i in range(1,33)]
    shuffle(peeps)
    fit_array = np.zeros([32,2])
    fitness = 0
    for i in range(32):
        fitness = 0
        p1 = mp.Player(int(peeps[i]))
        for j in range(n):
            fitness += pg.play_game_rvb(p1, current_gen,math.floor(np.random.uniform(0,2)))
        fit_array[i,1] = fitness
        fit_array[i,0] = p1._name
        
    #avg= np.average(fit_array[:,1])
    fitlog = fit_array[:,1]
    med = np.median(fit_array[:,1])
    a = 0
    
    for i in range(32):
        if fit_array[i, 1] == med:
            fit_array[i, 1] += .0001 * i
            
    med = np.median(fit_array[:,1])
    
    for i in range(32):
        if fit_array[i, 1] > med:
            winner_array[a] = fit_array[i,0]
            a += 1
            if a > 15:
                break
    
    #print(winner_array)
    ng.new_gen(current_gen, winner_array)
    current_gen += 1
    return(fitlog)

while x == True:
    print('Current Gen is: '+ str(current_gen))
    opt = int(input('Options:\n 1: Play game \n 2: Create New Gen \n 3: Run Select # of Gens \n 4: Exit \n 5: Play bot \nSelect: '))
    if opt == 1:
        made = False
        while made == False:
            p1, p2, gen = input('p1, p2, gen: ').split()
            if int(p1) < 33 and int(p1) > 0 and int(p2) < 33 and int(p2) > 0 and int(gen) <= current_gen and int(gen) >= 1:
                pg.play_game(mp.Player(int(p1)), mp.Player(int(p2)), gen)
                made = True
            if int(p1) >= 33 or int(p1) <= 0:
                print('p1 must be # from 1 to 32')
            if int(p2) >= 33 or int(p2) <= 0:
                print('p2 must be # from 1 to 32')
            if int(gen) > current_gen or int(gen) < 1:
                print('gen must be between 1 and the current gen ('+str(current_gen)+')')
    if opt == 2:

        step_gen_r()
        
    if opt == 3:
        start_gen = current_gen
        wien = input('how many? ')
        pat = np.zeros([int(wien),33])
        for i in range(int(wien)):
            pat[i,1:] = step_gen_r()
            pat[i,0] = current_gen
            print(current_gen)
            
        np.savetxt('run4gen'+str(start_gen)+'-'+str(current_gen-1)+'.csv', pat , delimiter = ',')
        
    if opt == 4:
        print('goodbye :)')
        break
    
    if opt == 5:
        made = False
        while made == False:
            p1, gen = input('p1, gen: ').split()
            if int(p1) < 33 and int(p1) > 0 and int(gen) <= current_gen and int(gen) >= 1:
                pg.play_game_hvb(mp.Player(int(p1)), gen, 1)
                made = True
            if int(p1) >= 33 or int(p1) <= 0:
                print('p1 must be # from 1 to 32')
            if int(gen) > current_gen or int(gen) < 1:
                print('gen must be between 1 and the current gen ('+str(current_gen)+')')
    
    else:
        print('pick again')
            