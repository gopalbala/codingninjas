#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:21:34 2019

@author: balasubramanian
"""

def tripletSum(arr,sum):
    for i in range (0 , len(arr)):
        rem = sum - arr[i]
        tupe =  pairSum(arr[i+1:], rem)
        if tupe is not None:
            print(arr[i], tupe[0], tupe[1])
                
def pairSum(arr, x):
    arr.sort()
    cnt = 0
    count=0
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if (arr[j]+arr[i])==x:
                if arr[j] > arr[i]:
                    return arr[i],arr[j]
                else:
                    return arr[j],arr[i]
    return None

def findTriplets(arr, n, sum):
    arr.sort();
    for i in range(0, n-1):
        l = i + 1;
        r = n - 1;
        x = arr[i];
        while (l < r) :
            if (x + arr[l] + arr[r] == sum) :
                print(x, arr[l], arr[r]);
                l = l + 1;
                r = r - 1;
        
            elif (x + arr[l] + arr[r] < sum):
                l = l + 1;
        
            else:
                r = r - 1;


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
#tripletSum(arr, sum)
findTriplets(arr,len(arr),sum)