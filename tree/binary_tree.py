"""
In this problem you have to find if there is a path where all the nodes added give the target sum.


The answer is that you have to use a DFS traverse technique and just be substracting from what it remainds from the targetSum.

A tricky point in this problem is that the answer has to be in a "leaf node"... It is possible
to have correct answer in parent node (if it doesn't have one of they child), but by the problem
it is not possible.

So a hit in this problem is: "How to identify when a node is a child node".
Another hit related to the previous one: "Once you identified the child node what you have to do 
with the remainder of the targetSum".
"""

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        if root == None:
            return False

        return self.preorder_traverse(root, targetSum)



    def preorder_traverse(self, root, targetSum):
        if root == None:
            return False

        if root.right == None and root.left == None: 
            # Leaf node
            if targetSum - root.val == 0:
                return True
            else:
                return False

        return max(
            self.preorder_traverse(root.left, targetSum - root.val), 
            self.preorder_traverse(root.right, targetSum - root.val)
        )