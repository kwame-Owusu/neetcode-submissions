# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def bfs(root):
            queue = deque()

            if root:
                queue.append(root)

            while len(queue) > 0:
                sublist = []
                for i in range(len(queue)):
                    curr = queue.popleft()
                    # append as list to res
                    sublist.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                res.append(sublist)
                
        
        bfs(root)
        return res
