"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        """
        res = []
        def pre(root):
            if not root:
                return
            res.append(root.val)
            for i in root.children:
                pre(i)
        

        pre(root)
        return res
        """
        res = []
        if not root:
            return res
        stack = [root,]
        while len(stack):
            root = stack[-1]
            stack.pop()
            res.append(root.val)
            for i in root.children[::-1]:
                stack.append(i)
        
        return res
