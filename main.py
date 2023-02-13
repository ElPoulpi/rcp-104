import math
#Define matrice
M= [ [0, 2, 4, 0, 0, 0, 0, 0],[2, 0, 0, 5, 0, 0, 0, 0],[4, 0, 0, 1, 0, 0, 4, 0],[0, 5, 1, 0, 0, 6, 1, 0],[0, 0, 0, 0, 0, 1, 2, 7],[0, 0, 0, 6, 1, 0, 0, 0],[0, 0, 4, 1, 2, 0, 0, 3],[0, 0, 0, 0, 7, 0, 3, 0] ]

#Fonction Dijkstra
def dijkstra(start):
    L= [math.inf] * len(M)
    L[start -1]= 0
    point= start
    P= [-1] * len(M)
    S= []
    c= 0
    
    #loop pour les itérations
    i = 0
    while i==0:
        c = c+1
        print("test", c)

        print ("je pars de ", point)
        #faire l'algo
        #redéfinir point
    
        if c == len(M):
            i = i+1


    print (L)
    print (P)
##################

dijkstra(3)







