"""
Title     : 237. Delete Node in a Linked List
Category  : Linked List
URL       : https://leetcode.com/problems/delete-node-in-a-linked-list/
submission: https://leetcode.com/submissions/detail/428624804/
"""

from typing import List

# --------------------------------------------------
# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

