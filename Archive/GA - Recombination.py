## types of recombination ##

import numpy as np
import random


ch_parent1 = np.random.randint(2,size=10)
ch_parent2 = np.random.randint(2,size=10)

# one-point
chromLen = len(ch_parent1)
CrossPoint = np.random.randint(1, high= chromLen-1)


child1 = np.concatenate((ch_parent1[0:CrossPoint],
                         ch_parent2[CrossPoint:len(ch_parent2)]),axis =0) 

child2 = np.concatenate((ch_parent2[0:CrossPoint],
                         ch_parent1[CrossPoint:len(ch_parent1)]),axis =0) 



# n-point
n = 2
chromLen = len(ch_parent1)
nCrossPoint = random.sample(range(1, chromLen-1 ) , 2) # n cross point
nPoint = sorted(nCrossPoint)

child3 = np.concatenate((ch_parent1[0:nPoint[0]], ch_parent2[nPoint[0]:nPoint[1]], ch_parent1[nPoint[1]:chromLen]),axis=0)

child4 = np.concatenate((ch_parent2[0:nPoint[0]], ch_parent1[nPoint[0]:nPoint[1]], ch_parent2[nPoint[1]:chromLen]),axis=0)


# uniform crossover
treshold = 0.5
child5 = np.random.randint(0,1,size = 10)
chromLen = len(child5)

for i in range(chromLen):
    r = random.random()
    print("r:", r)
    if r > treshold:
        print(i, ": pranet1")
        child5[i] = ch_parent1[i]
    else:
        print(i, ": pranet2")
        child5[i] = ch_parent2[i]














