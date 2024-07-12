class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        

        visited = set()
        solution = set()
        oceans_reached = [False, False]
        n = len(heights) - 1
        m = len(heights[0]) - 1

        if (n + 1) * (m + 1)  == 1:
            return [[0,0]]

        # Start from any cell: Current cell. 
        def dfs(origin, current_cell):            
            # Retriving coordinates
            i = current_cell[0]
            j = current_cell[1]
            
            # Vertical and horizontal cases
            # Pacific ocean case 
            if (i - 1 < 0 and j <= m) or (i <= n and j - 1 < 0):
                oceans_reached[0] = True

            # Atlantic ocean
            if (i + 1 > n and j <= m) or (i <= n and j + 1 > m):
                oceans_reached[1] = True

            # "If" to verify that both oceans have been reached.
            if oceans_reached[0] and oceans_reached[1]:
                solution.add((origin[0], origin[1]))
                return

            # "If" to verify if the current path goes by a path previously calculated 
            if (i, j) in solution:
                solution.add((origin[0], origin[1]))
                return

            # Verify if the current node is a visited one            
            if (i, j) in visited:
                return

            # Current node becomes in a visited one
            visited.add((i,j))
            
            # Retriving height of the curent cell
            current_height = heights[i][j] 
            

            # North
            if not(i - 1 < 0 and j <= m):
                next_height = heights[i - 1][j]
                if next_height <= current_height:
                    dfs(origin, [i - 1, j])
            
            # West
            if not(i <= n and j - 1 < 0):
                next_height = heights[i][j - 1]
                if next_height <= current_height:
                    dfs(origin, [i, j - 1])

            # South
            if not(i + 1 > n and j <= m):
                next_height = heights[i + 1][j]
                if next_height <= current_height:
                    dfs(origin, [i + 1, j])
            
            # East
            if not(i <= n and j + 1 > m):
                next_height = heights[i][j + 1]
                if next_height <= current_height:
                    dfs(origin, [i, j + 1])

        for i in range(n + 1):
            for j in range(m + 1):
                dfs([i,j], [i,j])
                visited.clear() 
                oceans_reached = [False, False]            

        return solution

        