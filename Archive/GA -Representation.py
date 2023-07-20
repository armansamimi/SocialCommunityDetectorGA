# types of representation 

import numpy as np
import random

# 1. binary 
chrom1 = np.random.randint(2,size=15)



# 2. integer
chrom2 = np.random.randint(0,high=10, size=10)


# 3. real value
chrom3 = 100*np.random.rand(20)-50

# 4 . permutation
chrom4 = np.random.permutation(100)-50
