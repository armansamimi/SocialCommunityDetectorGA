import numpy as np
import random
import statistics as st
# import panda as pd
import math
 # ----- hyper parameter --------------------------
popSize = 100
generation = 100
# -------------------------------------------------



# ----- read adjancey matrix ---------------------
file = open("dataset.txt", 'r')
lines = file.readlines()
maxPoint = lines[0]
chrom_size = int(maxPoint)
pointPerCluster = int(math.floor(chrom_size/4)) + 1
maxCluster = int(math.floor(chrom_size/pointPerCluster))

adjacency_matrix = []
for line in lines:
    new = line.rstrip('')
    splited = new.split()
    adjacency_matrix.append(splited)
# ------------------------------------------------

    


# ----Build A_matrix (it has 1 for edge and zero for others -------     
maxPoint = int(lines[0])
# All points number are mines '1' , Point '1' save in '0' index
A_matrix = np.zeros([maxPoint,maxPoint],dtype = int)
for item in range(1,len(adjacency_matrix)):
    m = int(adjacency_matrix[item][0])
    n = int(adjacency_matrix[item][1])
    A_matrix[m-1][n-1]=1
    A_matrix[n-1][m-1]=1
    # -----create degree matrix K -----------------------   
    # K: degree matrix
K_matrix = sum(A_matrix)

    # m: number of all edges in Graph
m = int(sum(K_matrix)/2)   
# -----------------------------------------------------------------        
        


        
  # ----- community generator for each chromosome ----- -----------     
def community_generator (chrom):    
    community = []
    for i in range(maxCluster):
        community.append([])   
    
    # p is moving on Points indexes [0,maxPoint -1]
    # p means a point
    for p in range(0, maxPoint):
        # chrom[p] means a cluster_number
        cluster_no = chrom[p]
        # add this point to this community
        community[cluster_no].append(p)
    return community
# ----------------------------------------------------------------
    
    
# ----- init population --------------------------
def init_pop(chromSize,maxCluster):
    Population = np.zeros((popSize,chromSize))
    for i in range(popSize):         
        chrom = np.random.randint(0,maxCluster,chromSize)
        Population[i] = chrom
    return Population
# ------------------------------------------------
  

# parent selection: uniform -----------------------------
def parent_selection():
    muRate = 0.5
    crossRate = 0.3
    muPop_size = int( np.ceil(muRate * popSize)) 
    crossPop_size = int (2*np.ceil((crossRate * popSize)/2)) 
    childPop_size = muPop_size + crossPop_size
    matingPoolIndex = random.sample( range(0,popSize),int(childPop_size))     
    return (matingPoolIndex,muPop_size,crossPop_size)
# ------------------------------------------------------
    

# crossover : 1 point ----------------------------------
def Crossover(Population, crossPop_size, matingPoolIndexes):
    chrom_size =  len (Population[0])
    children_cross = np.zeros((crossPop_size,chrom_size))
    i=0
    while i < crossPop_size:
        x= matingPoolIndexes [i]
        y= matingPoolIndexes [i+1]
        Parent1 = Population[x]
        Parent2 = Population[y]
        Pivot = np.random.randint(2,chrom_size-2)
        child1 = np.concatenate((Parent1[:Pivot],Parent2[Pivot:]))
        child2 = np.concatenate((Parent2[:Pivot] , Parent1[Pivot:])) 
        children_cross[i]= child1
        children_cross[i+1]= child2
        i = i + 2
    return children_cross
# -----------------------------------------------------

# ------ mutation -------------------------------
def mutate(Population,muPop_size , matingPoolIndexes):
    chrom_size =  len (Population[0])
    children_mut = np.zeros((muPop_size,chrom_size))
    crossPop_size =   len(matingPoolIndexes) - muPop_size -1
    i = crossPop_size
    j= 0
    while i < len(matingPoolIndexes)-1:
        x= matingPoolIndexes [i]
        Parent_single = Population[x]
        
        newGen =  np.random.randint(0,maxCluster)         # create new Gen (cluster_no)
        randomGenIndex = np.random.randint(0, chrom_size) # random index in child
        
        child = Parent_single.copy()
        
        child[randomGenIndex] = newGen
        children_mut[j] = child
        
        i = i + 1
        j= j + 1
    return children_mut
# ---------------------------------------------------------
    

# -----------firtness function---------------------------
def fitness_fun(Population,maxCluster):
    
    Q_Array = np.zeros(len(Population))  # this means fitnesses   
    Q = 0 
    score = 0
    All_sum = 0
    iteration = 0
    
    for iteration in range(0,len(Population)):
        chrom = Population[iteration]
        # print("chrom:", chrom)
        cluster = []
        community = []
        for i in range(maxCluster):
            community.append([])
        # print("community: ", community)
        
        # p is moving on Points indexes [0,maxPoint -1]
        # p means a point
        for p in range(0, maxPoint):
            # chrom[p] means a cluster_number
            cluster_no = chrom[p]
            # print("cluster_no: ", cluster_no)
            community[int(cluster_no)].append(p)
        # print("community:", community)
        
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
        # print("iteration: ", iteration)
        # iteration = iteration+ 1
        
         
    return Q_Array


# ---------------------------------------------------------





# # survival selection: elitism ---------------------------
def survivor_selection(TotalPop,mainPopsize):
    TotalpopSize = len(TotalPop)
    fitness = np.zeros(TotalpopSize)
    # -----------------------------calculate fitness-------
    fitness = fitness_fun(TotalPop,maxCluster)
    
    Total_bestIndexes = np.argsort(fitness)
    Final_bestIndexes = Total_bestIndexes[0:mainPopsize]
    
    newPop = TotalPop[Final_bestIndexes]
    newPopFitness = fitness[Final_bestIndexes]
    return newPop , newPopFitness
#----------------------------------------------------------


# ---------Genetic main loop ------------------------------
Population = init_pop(chrom_size,maxCluster) 
mainPopsize = popSize 
best_fitness_array= np.zeros(generation)
fitn_average_array= np.zeros(generation)

for epoch in range(generation):
    
      print("epoch:", epoch)
      matingPoolIndexes , muPop_size , crossPop_size = parent_selection()
      offspring_cross = Crossover(Population, crossPop_size, matingPoolIndexes)
      offspring_mu = mutate(Population, muPop_size, matingPoolIndexes)
      TotalPop = np.concatenate((Population,offspring_cross,offspring_mu) , 0 )
      newPop , newPopFitness = survivor_selection(TotalPop, mainPopsize)
      bestIndexes = np.argsort(newPopFitness)
      Final_bestIndex = bestIndexes[0]
      best_fitness_array [epoch] = newPopFitness[Final_bestIndex]
      fitn_average_array [epoch] = st.mean(newPopFitness)
      Population = newPop
      
      
# ------ end of main loop -------------------------------

bestIndexes = np.argsort(newPopFitness)
Final_bestIndex = bestIndexes[0]
bestSolution = newPop[Final_bestIndex]
bestSolution_fitness =  newPopFitness[Final_bestIndex]








