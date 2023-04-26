'''
    Problem:
    Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low, high, res = 0) :
        
        #bfs
        res = 0
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if low <= node.val <= high:
                res += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
        
        #recursion
        if not root:
            return 0
        if root.val < low or root.val > high:
            return self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
    
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
