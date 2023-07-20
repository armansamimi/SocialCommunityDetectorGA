## types of mutation ##
import numpy as np
parent1 = np.random.randint(2, size=10)

# bit-flipping
chromLen = len(parent1)
randomIndex = np.random.randint(1,chromLen)
child1 = parent1.copy()
child1[randomIndex] = 1 - parent1[randomIndex]


# random reseting
parent2 = np.random.randint(10, size=10)-5
validSet = sorted(np.random.permutation(10)-5)
randomGenA = np.random.randint(0, chromLen) # random index from valid set
randomGenB = np.random.randint(0, chromLen) # random index in child
child = parent2.copy()
child[randomGenB] = validSet [randomGenA]



# Nonuniform mutation
parent3 = 10* np.random.rand(10)
mu = 0
sigma = 1
Deltax = np.random.normal(mu, sigma)
randomGenC = np.random.randint(0, len(parent3))
child3 = parent3.copy()
child3 [randomGenC] = parent3[randomGenC] + Deltax














