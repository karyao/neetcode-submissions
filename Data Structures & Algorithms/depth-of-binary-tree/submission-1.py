# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solution(self, root: Optional[TreeNode], total: int) -> int:
        if root is None:
            return 0
        if root:
            return 1+ max(self.solution(root.right, total), self.solution(root.left, total))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None): return 0
        totalLeft = 1
        totalRight = 1
        if(root and (root.left is None and root.right is None)): return 1
        if(root and root.left):
            totalLeft += self.solution(root.left, totalLeft)
        if(root and root.right):
            totalRight += self.solution(root.right, totalRight)
        return max(totalLeft, totalRight)
        