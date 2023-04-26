'''
    #The problem
    Given two binary trees original and cloned and given a reference to a node target in the original tree.

    The cloned tree is a copy of the original tree.

    Return a reference to the same node in the cloned tree.

    Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

    Input: tree = [7,4,3,null,null,6,19], target = 3
    Output: 3
    Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

    
'''
import collections
    #Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        #BFS
        q = collections.deque()
        q.append(cloned)
        while q:
            cur = q.popleft()
            if cur.val == target.val:
                return cur
            else:
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return 
    
        #Recursion
        if not cloned:
            return None
        if cloned.val == target.val:
            return cloned
        left = self.getTargetCopy(original,cloned.left,target)
        if left:
            return left
        right = self.getTargetCopy(original,cloned.right,target)
        if right:
            return right
        return 