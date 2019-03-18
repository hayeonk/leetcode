# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        newList = ListNode(0)
        node = newList
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
                node = node.next
            else:
                node.next = l2
                l2 = l2.next
                node = node.next
        if l1 is not None:
            node.next = l1
        if l2 is not None:
            node.next = l2
        return newList.next