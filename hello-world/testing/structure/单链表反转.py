#coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        prev = None
        while head != None:
            mid = head
            head = head.next
            mid.next = prev
            prev = mid