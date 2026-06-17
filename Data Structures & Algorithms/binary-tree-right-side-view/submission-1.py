# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def bfs(root):
            queue = deque()

            if root:
                queue.append(root)
            
            while len(queue) > 0:
                right_most_node = queue[-1]
                res.append(right_most_node.val)

                for i in range(len(queue)):
                    curr = queue.popleft()
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
         
        bfs(root)
        return res