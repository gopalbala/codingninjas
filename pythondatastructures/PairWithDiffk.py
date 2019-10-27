def printPairDiffK(l, k):
    #Implement Your Code Here
    d = {}
    s1 = {}
    for i in l:
        if d.get(i,0) == 0: 
            d[i] = 0
        else:
            val = d[i]    
            d[i] = val + 1
    for i in l:
        j = i * -1
        if d.get(j) == 0:
            s1[j] = i
        d.pop(i,None)
    # print(s1)
    for (x,y) in s1.items():
        if x > y:
            print(y, x)
        else:
            print(x, y)


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)