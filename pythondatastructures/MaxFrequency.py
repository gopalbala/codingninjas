import collections
def maxFreq(l):
    d = collections.OrderedDict()
    # Please add your code here
    for i in l:
        if d.get(i, 0) > 0:
            d[i] = d.get(i) + 1
        else:
            d[i] = 1
    mx = 0
    tp = () 
    for k, v in d.items():
        if v > mx:
            mx = v
            tp = (k,v)
    
    (k,v) = tp
    return k

# Main
# n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
