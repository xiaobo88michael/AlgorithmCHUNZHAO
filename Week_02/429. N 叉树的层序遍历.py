"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        res = []
        queue = [root,]
        if not root:
            return res

        while len(queue):
            temp = []
            for i in range(len(queue)):
                root = queue[0]
                queue = queue[1:]
                temp.append(root.val)
                queue.extend(root.children)
                

            res.append(temp)
        
        return res
