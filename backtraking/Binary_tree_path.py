class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        solution_arr = []

        def format(chain):
            if len(chain) == 0:
                return ""
            s = ""
            s = str(chain[0])
            for i in range(1, len(chain)):
                s = s + "->" + str(chain[i])
            return s

        def bfs(chain, root):
            if root == None:
                return

            if root.left == None and root.right == None:
                chain.append(root.val)
                solution_arr.append(format(chain))
                chain.pop()
                return

            chain.append(root.val)
            bfs(chain, root.left)
            bfs(chain, root.right)
            chain.pop()

        bfs([], root)

        return solution_arr