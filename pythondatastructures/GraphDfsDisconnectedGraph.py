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
    
    def dfs(self):
        visited = [False for i in range(self.nVert)]
        for i in range(self.nVert):
            if visited[i] == False:
                self._dfs(i,visited)
    
    def _dfs(self,sv,visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVert):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                self._dfs(i,sv)