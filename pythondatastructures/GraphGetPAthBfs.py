import queue
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
    
    def getPath(self,sv,ev):
        d = {}
        path = []
        q = queue.Queue()
        visited = [False for i in range(self.nVert)]
        q.put(sv)
        d[sv] = None
        while not q.empty():
            v = q.get()
            visited[v] = True
            for i in range(self.nVert):
                if self.adjMatrix[v][i] > 0 and visited[i] == False:
                    d[i] = v
                    visited[i] = True
                    if i == ev:
                        k = i
                        print(k, end = ' ')
                        while d.get(k,None) != None:
                            print(d[k], end = ' ')
                            k = d.get(k)
                    else:
                        q.put(i)
                    
            
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
g.getPath(int(v1),int(v2))