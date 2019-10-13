def pairSum0(arr):
    # Implement Your Code Here
    d = {}
    s1 = {}
    for i in l:
        d[i] = 0
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
    
    # arr.sort()
    # cnt = 0
    # count=0
    # x =0
    # n = len(arr)
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         if (arr[j]+arr[i])==x:
    #             if arr[j] > arr[i]:
    #                 print(arr[i],arr[j])
    #             else:
    #                 print(arr[j],arr[i])


# n=int(input())
l = list(int(i) for i in input().strip().split(' '))
pairSum0(l)
