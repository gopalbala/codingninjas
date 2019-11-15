## Read input as specified in the question.
## Print output as specified in the question.
class Edge:
    def __init__(self,source,dest,weight):
        if source > dest:
            source,dest = dest,source
        self.source = source
        self.dest   = dest
        self.weight = weight
    
    def __gt__(self,other):
        return True if self.weight > other.weight else False
    
    def __lt__(self,other):
        return True if self.weight < other.weight else False
    
    def __eq__(self,other):
        return True if self.weight == other.weight else False
   
    def __ge__(self,other):
        return True if self.weight >= other.weight else False
    
    def __le__(self,other):
        return True if self.weight <= other.weight else False
   
    def __ne__(self,other):
        return True if self.weight != other.weight else False
    
    def __str__(self):
        return str(self.source) + ' ' + str(self.dest) + ' '+ str(self.weight)
    
def createMST(nVertices,edges):
    final=[]
    par_matrix = [x for x in range(nVertices)]
    edgecount  = 0
    for edge in edges:
        if edgecount >= (nVertices - 1):
            break
        src_parent = find_parent(par_matrix,edge.source)
        dest_parent = find_parent(par_matrix,edge.dest)
        if src_parent != dest_parent:
            edgecount = edgecount + 1
            final.append(edge)
            par_matrix[dest_parent] = src_parent
        
    return final

def find_parent(par_matrix,item):
    parent = par_matrix[item]
    while parent != item:
        item    = parent
        parent  = par_matrix[item]
    return parent 

v,e = (int(x) for x in input().split())
edges = []
for i in range(e):
    source,dest,weight = (int(x) for x in input().split())
    newEdge = Edge(source,dest,weight)
    edges.append(newEdge)
edges.sort()
 
final = createMST(v,edges)
for edge in final:
    print(edge)