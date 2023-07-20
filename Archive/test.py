import numpy as np
import random
import statistics as st
import pandas as pd

data = pd.read_csv("dataset.txt")
dataSet = data.values.tolist()

file1 = open("dataset.txt", 'r')
lines = file1.readlines()
i = 1

adjacency_matrix = []
for k in range(1,len(lines)):
    new = lines[k].rstrip('')
    splited = new.split()
    adjacency_matrix.append(splited)    




# ---------- A matrix ------------------------------------------
maxPoint = int(lines[0])
# All points number are mines '1' , Point '1' save in '0' index
A_matrix = np.zeros([maxPoint,maxPoint],dtype = int)
for item in range(0,len(adjacency_matrix)):
    m = int(adjacency_matrix[item][0])
    n = int(adjacency_matrix[item][1])
    A_matrix[m-1][n-1]=1
    A_matrix[n-1][m-1]=1

popSize = 100
generation = 40


# K: degree matrix
K_matrix = sum(A_matrix)

# m: number of all edges in Graph
m = int(sum(K_matrix)/2)


# --k_degree----------------------------------
k_degree = np.zeros((1, maxPoint))

for i in range(0, maxPoint):
    print("i", i)
    sum_deg = 0
    for item in range(0,len(adjacency_matrix)):
        sum_deg = sum_deg + adjacency_matrix[item].count(str(i+1))
        k_degree[0,i] = sum_deg


# -------------------------------------------








# -------------------------------------------

# ----- init population --------------------------
maxPoint = 34
maxCluster = int(maxPoint / 8)
chromSize = maxPoint
Population = np.zeros((popSize,chromSize),dtype=int)
for i in range(popSize):
    chrom = np.random.randint(0,maxCluster,chromSize,int)
    Population[i] = chrom
# ----- init population --------------------------
    
    
    
    
# ----------1 point crossover-----------------------
Parent1 = Population[0]
Parent2 = Population[1]
Pivot = np.random.randint(2,chromSize-2)

child = np.zeros(chromSize)
x = Parent1[:Pivot]
y= Parent1[Pivot:]
child1 = np.concatenate((Parent1[:Pivot],Parent2[Pivot:]))
child2 = np.concatenate((Parent2[:Pivot] , Parent1[Pivot:]))
# -------------------------------------------







# -----------------------------------------
    
    
    
# ----------- calculate Q ----------------- 

Q_Array = np.zeros(popSize)    
Q = 0 
score = 0
All_sum = 0
iteration = 0

for chrom in Population:
    cluster = []
    community = []
    for i in range(maxCluster):
        community.append([])
      
    # p is moving on Points indexes [0,maxPoint -1]
    # p means a point
    for p in range(0, maxPoint):
        # chrom[p] means a cluster_number
        cluster_no = chrom[p]
        community[cluster_no].append(p)
    
    for cluster in community:
        for i in range(0,len(cluster)):
            for j in range(i+1,len(cluster)):       
                score = A_matrix[i][j] - ((K_matrix[i]*K_matrix[j])/(2*m))
                # print("new pair: (",cluster[i],",",cluster[j],")")
                # print("score:","%.2f" % score)
                All_sum = All_sum + score
        # print("--- All_sum for this cluster: ", All_sum)
        # print("---next Cluster")
    Q = (score) / (2 * m)
    Q_Array[iteration] = Q
    iteration = iteration+ 1
    
