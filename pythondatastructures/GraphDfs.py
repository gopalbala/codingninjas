class Graph:
    def __init__(self,nVert):
        self.nVert = nVert
        self.adjMatrix = [[0 for i in range(nVert)] for j in range(nVert)]
    
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
    
    def dfs(self):
        visited = [False for i in range(self.nVert)]
        self._dfsHelper(0,visited)
    
    def _dfsHelper(self,sv,visited):
        print(sv, end = ' ')
        visited[sv] = True
        for i in range(self.nVert):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                self._dfsHelper(i,visited)
                
# g = Graph(5)
# g.addEdge(0,1)
# g.addEdge(1,3)
# g.addEdge(2,4)
# g.addEdge(2,3)
# g.addEdge(0,2)
s = input()
(i,j) = s.split()
g = Graph(int(i))
k = 0
while k < int(j):
    s1 = input()
    (v1,v2) = s1.split()
    g.addEdge(int(v1),int(v2))
    k+=1
print()
g.dfs()
