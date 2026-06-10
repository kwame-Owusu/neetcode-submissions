# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if val > root.val:
            root.right = self.deleteNode(root.right, val)
            return root
        elif val < root.val:
            root.left = self.deleteNode(root.left, val)
            return root
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
            return root
    
    def minValueNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    