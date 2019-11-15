import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adj_matrix = [[0 for x in range(nVertices)] for y in range(nVertices)]
   
    def addEdge(self,v1,v2,wt):
        self.adj_matrix[v1][v2] = wt
        self.adj_matrix[v2][v1]  = wt
   
    def removeEdge(self,v1,v2):
        if not self.containsEdge(v1,v2):
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0
    
    def containsEdge(self,v1,v2):
        return True if self.adj_matrix[v1][v2] > 0 else False
 
    def prim_helper(self,visited,parent,weight):
       
        for i in range(self.nVertices-1):
            minVertex          = self.getMinVertex(visited,weight)
            visited[minVertex] = True
            for vertex in range(self.nVertices):
                if visited[vertex] is False and self.containsEdge(minVertex,vertex):
                    newWeight      = self.adj_matrix[minVertex][vertex]
                    if newWeight < weight[vertex]:
                        weight[vertex] = newWeight
                        parent[vertex] = minVertex
        return
        
    def prim(self):
        visited   = [False for x in range(self.nVertices)]
        parent    = [-1 for x in range(self.nVertices)]
        weight    = [sys.maxsize for x in range(self.nVertices)]
       
        self.prim_helper(visited,parent,weight)
        final = []
        for vertex in range(1,self.nVertices):
            edge = [min(vertex,parent[vertex]),max(vertex,parent[vertex]),weight[vertex]]
            final.append(edge)
        return final
        
    def getMinVertex(self,visited,weight):
        minVertex = -1
        for vertex in range(self.nVertices):
            if visited[vertex] is False and (minVertex==-1 or weight[vertex] < minWeight):
                minWeight = weight[vertex]
                minVertex = vertex
        return minVertex
        
        
v,e = (int(x) for x in input().split())
gr  = Graph(v)
for i in range(e):
    v1,v2,wt = (int(x) for x in input().split())
    gr.addEdge(v1,v2,wt)
 
final = gr.prim()
for edge in final:
    print(str(edge[0]) + ' ' + str(edge[1]) + ' ' + str(edge[2]))