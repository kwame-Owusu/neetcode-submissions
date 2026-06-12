# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root


        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Curr is None here, so we pop from stack to get node
            curr = stack.pop()
            res.append(curr.val)

            # At this point we have visited the leftmost subtree, now we go right
            curr = curr.right
        
        return res