
from collections import defaultdict 
from ligne1 import test1
 

class Graph: 
 
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
 
        
        self.graph= defaultdict(list) 
 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 
 
   
    def DFSUtil(self,v,visited,vDegree,k): 
 
        visited[v] = True
 
        
        for i in self.graph[v]: 
 
          
            if vDegree[i] < k: 
                vDegree[v] = vDegree[v] -1
 
            
            if visited[i]==False: 
 
                
                if (self.DFSUtil(i,visited,vDegree,k)): 
                    vDegree[v] -=1
 
         
        return vDegree[v] < k 
 
 
    
    def printKCores(self,k): 
 
         
        visited = [False]*self.V 
 
        
        vDegree = [0]*self.V 
        for i in self.graph: 
                vDegree[i]=len(self.graph[i]) 
 
        
        self.DFSUtil(0,visited,vDegree,k) 
 
         
        for i in range(self.V): 
            if visited[i] ==False: 
                self.DFSUtil(i,k,vDegree,visited) 
 
       
        print ("\n K-cores: ")
        for v in range(self.V): 
 
            
            if vDegree[v] >= k: 
                print (str("\n [ ") + str(v) + str(" ]")), 
            
                
                for i in self.graph[v]: 
                    if vDegree[i] > vDegree[v]: 
                        print ("-> " + str(i)),
                   
                   
k = test1()
g1 = Graph (9); 
g1.addEdge(0, 1) 
g1.addEdge(0, 2) 
g1.addEdge(1, 2) 
g1.addEdge(1, 5) 
g1.addEdge(2, 3) 
g1.addEdge(2, 4) 
g1.addEdge(2, 5) 
g1.addEdge(2, 6) 
g1.addEdge(3, 4) 
g1.addEdge(3, 6) 
g1.addEdge(3, 7) 
g1.addEdge(4, 6) 
g1.addEdge(4, 7) 
g1.addEdge(5, 6) 
g1.addEdge(5, 8) 
g1.addEdge(6, 7) 
g1.addEdge(6, 8) 

g1.printKCores(k) 
