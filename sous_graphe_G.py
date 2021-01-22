# calcul sous graphe

def sousgraph():
    
        
    matrice= ([
        [1,1,1,0,0,0,0,0,0],
        [1,1,1,0,0,1,0,0,0],
        [1,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,0,1,1,0],
        [0,0,1,1,1,0,1,1,0],
        [0,1,1,0,0,1,1,0,1],
        [0,0,1,1,0,1,1,1,1],
        [0,0,0,1,1,0,1,1,0],
        [0,0,0,0,0,1,1,0,1] ] )
        
            
    liste= ([0,1,5,8,2,3,4,6,7])
        
        
        #parcours liste de degenerecence
        
    for i in range (9):
          
         var =liste [i]
         j=i+1
         print("\n")
         while j<len(liste):
          v=liste[j]
          print(v,"-",var)
          
          matrice[v][var]=0
          
          j=j+1
          
         
    for x in range (9):
         varr=liste[x]
         for y in range (9):
          print(matrice[varr][y])
         print("\n") 
         
sousgraph()