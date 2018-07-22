# -*- coding: utf-8 -*-
"""
Created on 2018/7/16 17:34

@author: vincent
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start.next and start.next.next:
            l1 = start.next
            l2 = l1.next
            l3 = l2.next
            start.next = l2
            l2.next = l1
            l1.next = l3
            start = l1
        return dummy.next