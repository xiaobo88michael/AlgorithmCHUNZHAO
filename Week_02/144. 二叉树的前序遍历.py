# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        if not root:
            return []

        while root or len(stack)>0:
            
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack[len(stack)-1].right
            stack = stack[:len(stack)-1]
        
        return res
