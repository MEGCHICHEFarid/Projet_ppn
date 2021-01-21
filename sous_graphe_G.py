#sous graphe
matrice= ([
[1,1,1,0,0,0,0,1],
[1,1,0,1,1,0,0,1],
[1,0,1,1,0,0,0,1],
[0,1,1,1,1,1,0,1],
[0,1,0,1,1,0,1,0],
[0,0,0,1,0,1,0,0],
[0,0,0,0,1,1,1,0],
[1,1,1,1,0,0,0,1] ])

liste= ([5,6,4,0,1,2,3,7]) 

 
#parcours liste de degenerecence
for i in range (8):
  
 var =liste [i]
 j=i+1
 print("\n")
 while j<len(liste):
  v=liste[j]
  print(v,"-",var)
  
  matrice[v][var]=0
  
  j=j+1
  
 
for x in range (8):
 varr=liste[x]
 for y in range (8):
  print(matrice[varr][y])
 print("\n") 
 