# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root): #List[List[int]]
        """
        Traversal all the elements in every level
        """
        res=[]
        queue=[root]
        while queue:
            row=[]
            l=len(queue)
            for i in range(l):
                node=queue.pop(0)
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(row)
        return res

