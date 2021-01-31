"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        res = []
        """

        def post(root):
            if not root:
                return 
            for c in root.children:
                post(c)
            
            res.append(root.val)
        
        post(root)
        """
        stack = [root,]
        if not root:
            return []

        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
            for c in root.children:
                stack.append(c)
            

            
        return res[::-1]
