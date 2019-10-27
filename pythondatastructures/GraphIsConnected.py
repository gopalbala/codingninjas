class Graph:
    def __init__(self, nVert):
        self.nVert = nVert
        self.adjMatrix = [[0 for i in range(nVert)] for j in range(nVert)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if containsEdge(v1, v2) == False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def str(self):
        return str(self.adjMarix)
    
    def dfs(self):
        visited  = [False for i in range(self.nVert)]
        return self._dfs(0,visited)
        
    def _dfs(self,sv,visited):
        visited[sv] = True
        for i in range(self.nVert):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                self._dfs(i,visited)
        return visited
    
s = input()
(i,j) = s.split()
g = Graph(int(i))
k = 0
while k < int(j):
    s1 = input()
    (v1,v2) = s1.split()
    g.addEdge(int(v1),int(v2))
    k+=1
    
visited = g.dfs()

if any(i == False for i in visited):
    print('false')
else:
    print('true')