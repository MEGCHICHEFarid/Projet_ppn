class Graph:
    def __init__(self):
        self.V = dict()

    def add_vertex(self, v1, edges=None):
        self.V[v1] = edges or set()
        
    def remove_vertex(self, v):
        self.V.pop(v, None)
        for vert, edges in self.V.items():
            edges.discard(v)
            
    def get_degrees(self):
        return {k: len(v) for k, v in self.V.items()}
        
def kCores(graph):
    vdegree = graph.get_degrees()
    order = sorted([(i, d) for i, d in vdegree.items()], key=lambda e: e[1])

    k = 1
    kcores = dict()
    rem_list = []

    while order:
        index = order[0][0]
        degree = order[0][1]
        if degree <= k:
            rem_list.append(order.pop(0))
            graph.remove_vertex(index)
            vdegree = graph.get_degrees()
            order = sorted([(i, d) for i, d in vdegree.items()], key=lambda e: e[1])
           # print(order)
        else:
            kcores[k] = sorted([i for i, d in rem_list])
            k += 1
            rem_list = []

    print("le graphe est de degeneresence", k)
    if len(rem_list) > 0:
        kcores[k] = sorted([i for i, d in rem_list])
    
    for i in kcores.keys():
        for j in range(i+1 , k ):
              if k in (range(j,0)):
                  print(range(j,0))
                  kcores[i].extend(kcores[j])
                 
    return  kcores


def test1():
    print("== Test 1 ==:")
    g = Graph()
    g.add_vertex(0, {1, 2})
    g.add_vertex(1, {0, 2,5})
    g.add_vertex(2, {0, 1, 3,4,5,6})
    g.add_vertex(3, {2,4,6,7})
    g.add_vertex(4, {2, 3,6,7})
    g.add_vertex(5, {1,2,6,8})
    g.add_vertex(6, {2 ,3 ,4 ,5 ,7 ,8})
    g.add_vertex(7, {3,4,6})
    g.add_vertex(8, {5,6})
    
    deg_list = [] 
    
   
    for k, core in kCores(g).items():
      print("{}-core: {}".format(k, core))
      deg_list.extend(core)
    print("la liste de degenerescence ",deg_list)

    
test1()

