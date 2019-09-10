#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:15:30 2019

@author: balasubramanian
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def check_palindrome(head) :
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not head or not head.next:
        return True

    stack = []
    slow, fast = head, head.next
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # for even numbers add mid
    if fast:
        stack.append(slow.data)

    curt = slow.next
    while curt:
        if curt.data != stack.pop():
            return False
        curt = curt.next
    return True

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
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")