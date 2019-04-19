# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        ans = []
        stack = []
        idx = 0
        while head:
            while stack and stack[-1][0] < head.val:
                _, i = stack.pop()
                ans[i] = head.val
            stack.append([head.val, idx])
            ans.append(0)
            idx += 1
            head = head.next
        return ans