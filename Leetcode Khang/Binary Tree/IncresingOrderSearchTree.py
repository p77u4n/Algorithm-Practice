'''
    Problem:
    Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
    Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root):
        if not root:
            return None
        dummy = cur = TreeNode()
        explored, stack = {root,},[]
        if root.right:
            stack.append(root.right)
        stack.append(root)
        if root.left:
            stack.append(root.left) 
        while stack:
            node = stack.pop()
            if node in explored:
                cur.right = TreeNode(node.val)
                cur = cur.right
            if node not in explored:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                if node.left:
                    stack.append(node.left) 
                explored.add(node)
        return dummy.right
            