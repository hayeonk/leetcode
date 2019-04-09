# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        p = dummy
        pq = []
        
        for node in lists:
            while node:
                heapq.heappush(pq, node.val)
                node = node.next
        
        while pq:
            p.next = ListNode(heapq.heappop(pq))
            p = p.next
        return dummy.next