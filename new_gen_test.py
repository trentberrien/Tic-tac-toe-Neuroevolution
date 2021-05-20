import numpy as np

import make_player_test as mp

#winners = np.array([1,3,4,5,7,11,13,14,16,17,20,21,22,24,26,27])

def new_gen(old_gen, win_array):

    a = np.zeros([16,182])
    
    mut_prob = .5
    
    mut_mag = .25
    
    mp.data = mp.data = np.loadtxt('run4gen'+ str(old_gen) +'.csv', delimiter = ',')

    for i, x in enumerate(win_array):
        a[i,1:] = mp.Player(int(x))._data
        a[i,0] = i+1
    
    b = np.zeros([32,182])
    
    for i in range(32):
        b[i,0] = i+1
    
    for i in range(16):
        #b[i,1] = a[i,1]
        #b[i+16,1] = a[i,1]
        b[i,1:20] = a[i,1:20]
        b[i+16,1:20] = a[i,1:20]
        for j in range(20,182): #2:182
            if np.random.uniform(0,1) < mut_prob:
                b[i,j] = a[i,j] + np.random.uniform(-mut_mag,mut_mag)
                b[i+16,j] = a[i,j] + np.random.uniform(-mut_mag,mut_mag)
            else:
               b[i,j] = a[i,j]
               b[i+16,j] = a[i,j]
                
    np.savetxt('run4gen'+str(old_gen + 1)+'.csv', b , delimiter = ',')
    #print(b)

#new_gen(1, winners)