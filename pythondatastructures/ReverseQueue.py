
import queue
def reverseQueue(q1):
    if q1.qsize() == 0:
        return 
    item = q1.get()
    reverseQueue(q1)
    q1.put(item)
    
#### Implement Your Code Here

from sys import setrecursionlimit
setrecursionlimit(11000)
li = [int(ele) for ele in (input().split()[1:])]
q1 = queue.Queue()
for ele in li:
    q1.put(ele)
reverseQueue(q1)
while(q1.empty() is False):
    print(q1.get(),end= ' ')