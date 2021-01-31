# Definition for a binary tree node.
# class TreeNode(object)
#     def __init__(self, val=0, left=None, right=None)
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object)
    def buildTree(self, preorder, inorder)
        
        type preorder List[int]
        type inorder List[int]
        rtype TreeNode
        
      	if not (preorder and inorder)
			return 
			
        root = TreeNode(preorder[0])
		
        mid_idx = inorder.index(preorder[0])
		
        root.left = self.buildTree(preorder[1mid_idx+1],inorder[mid_idx])
        root.right = self.buildTree(preorder[mid_idx+1],inorder[mid_idx+1])
        return root
