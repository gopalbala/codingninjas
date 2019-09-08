#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:39:56 2019

@author: balasubramanian
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def lengthRecursive(head):
    # A linked list, find and return the length of input LL recursively.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    
    if head is None:
        return 0
    elif head is not None:
        return 1 + lengthRecursive(head.next)
        
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
len=lengthRecursive(l)
print(len)
