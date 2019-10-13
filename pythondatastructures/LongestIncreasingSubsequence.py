def longestConsecutiveSubsequence(l):
    if l is None or len(l) == 0:
        return l
    d = {}
    for i in l:
        d[i] = True
    start = 0
    end = 0
    longlen = 0
    for i in l:
        if d[i] == True:
            currlen = 1
            currSt = i
            currEnd = i
            k = i + 1
            d[i] = False
            while d.get(k, False) == True:
                currlen+=1
                currEnd = k
                d[k] = False
                k+=1
            k = i - 1
            while d.get(k, False) == True:
                d[k] = False
                currlen+=1
                currSt = k
                k-=1
                
            if currlen >= longlen:
                longlen = currlen
                if start == 0:
                    start = currSt
                    end = currEnd
                elif currSt < start:
                    start = currSt
                    end = currEnd
                    
        
    l1 = []
    for i in range(start,end+1):
        l1.append(i)
    return l1
            
                
                
            
#Implement Your Code Here
#You have To Return the list of longestConsecutiveSubsequence


# n=int(input())
l=list(int(i) for i in input().strip().split(' '))
final = longestConsecutiveSubsequence(l)
for num in final:
    print(num)