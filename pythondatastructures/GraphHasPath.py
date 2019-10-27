import queue
class Graph:
    def __init__(self,nVert):
        self.nVert = nVert
        self.adjMatrix = [[0 for i in range(nVert)] for j in range(nVert)]
        self.found = False
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self, v1, v2):
        if containsEdge(v1,v2) == False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def str(self):
        return str(self.adjMarix)
    
    def hasPath(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        visited = [False for i in range(self.nVert)]
        return self._hasPath(v1,v2,visited)
        
    def _hasPath(self,v1,v2,visited):
        visited[v1] = True
        for i in range(self.nVert):
            if self.adjMatrix[v1][i] > 0 and visited[i] == False:
                if i == v2:
                    self.found = True
                else:
                    visited[i] = True
                    self._hasPath(i,v2,visited)
        return self.found  
           
s = input()
(i,j) = s.split()
g = Graph(int(i))
k = 0
while k < int(j):
    s1 = input()
    (v1,v2) = s1.split()
    g.addEdge(int(v1),int(v2))
    k+=1

pvs = input()
(v1,v2) = pvs.split()
if g.hasPath(int(v1), int(v2)):
    print('true')
else:
    print('false')


# g = Graph(5)
# g.addEdge(0,1)
# g.addEdge(1,3)
# g.addEdge(2,4)
# g.addEdge(2,3)
# g.addEdge(0,2)
# g.bfs()
                     