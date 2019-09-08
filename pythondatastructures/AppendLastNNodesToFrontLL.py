#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:50:40 2019

@author: balasubramanian
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n) :
    #  Given a linked list and an integer n, append the last n elements of the LL
    #  to front. 
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head is None:
        return None
    l = length(head)
    curr = None
    temp = None
    head1 = None
    newHead = None
    if n > l:
        return head
    
    i = 0
    temp = head
    
    while i < l-n:
        temp = temp.next
        i+=1
    
    curr = temp
    
#    print(curr.data)
    while curr is not None:
        if head1 is None:
            head1 = Node(curr.data)
            newHead = head1
        else:
            head1.next = Node(curr.data)
            head1 = head1.next
        curr = curr.next
    
    i = 0
    temp = head
    while i < l-n:
        head1.next = Node(temp.data)
        head1 = head1.next
        temp = temp.next
        i+=1
    return newHead

def length(head):
    temp = head
    count = 0
    if temp is None:
        return count
    while temp is not None:
        count += 1
        temp = temp.next
    return count

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = append_LinkedList(l, i)
printll(l)