# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root): #List[List[int]]
        """
        """
        if not root:
            return root
        # Our traversal should be like level by level, 
        # and how to implement it in real word?
        # a data structure can support traversal
        queue=[root]
        res=[]
        while queue:
            # we return list that includes all row
            row=[]
            # the length for queue is equal to the length of the row
            l=len(queue)
            while l>0:
                curr=queue.pop(0)
                row.append(curr)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # add all the elelemts which belong to same level
            res.append(row)
        return res


