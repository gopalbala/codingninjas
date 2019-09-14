
import queue 
def reverseFirstK(q1,k):
#Implement Your Code Here
#1 2 3 4 5 3 2 1 4 5
    if q1.qsize() == k-1:
        return 
    item = q1.get()
    reverseFirstK(q1,k)
    q1.put(item)
    i = 0     
    while i < k-1:
        q1.put(q1.get())  
        
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())
reverseFirstK(q,k) 
i = 0
  
while(q.qsize()>0):
	print(q.get())
	n-=1