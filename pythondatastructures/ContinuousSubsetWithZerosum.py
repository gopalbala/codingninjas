def subsetSum(l):
    #Implement Your Code Here
    map = {0:[-1,-1]}
    longest = 0
    for i in range(len(l)):
        sum += l[i]
        if map.get(sum,'NF') == 'NF':
            map[sum] = [i,i]
        else:
            map[sum][1] = i
   
    maxlen = 0
    for ele in map:            
        li = map[ele]
        if len(li) > 1:
            newlen = li[1] - li[0]
            maxlen = max(maxlen,newlen)
               
    return maxlen
                
            
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
finalLen= subsetSum(l)
print(finalLen)