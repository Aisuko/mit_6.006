# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        """
        Maximum depth of a binary tree. So, we need to make sure every node we have been traversal,
        it is related to BFS
        """
        if not root:
            return 0
        queue=[root]
        # deepth is use to count the deepth of the tree
        deepth=0
        while queue:
            l=len(queue)
            while l>0:
                # FIFO feature ==pop(0)
                curr=queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                # the number of elements at the same level
                l-=1
            # plus 1 after finish a level
            deepth+=1
        return deepth
