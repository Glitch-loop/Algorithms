
class Solution():
  def path_maze(self, maze, start, end):
      visited = set()
      path = []
      def finding_path(c_row, c_col):
        # End was found
        if c_row == end[0] and c_col == end[1]:
          return True
        
        # Wrong case
        # 1. Bounding cases
        # 2. Wall case

        if (
          c_row > len(maze)
          or c_col > len(maze[0])
          or maze[c_row][c_col] == 1
          or (c_row, c_col) in visited):
            return False
        
        visited.add((c_row, c_col))
        res = (finding_path(c_row + 1, c_col) or
              finding_path(c_row - 1, c_col) or
              finding_path(c_row, c_col + 1) or
              finding_path(c_row, c_col - 1))
        
        path.append((c_row, c_col))
        if not(res):
          print(res)
          path.pop()

        visited.remove((c_row, c_col))
        return res
      
      res = finding_path(start[0], start[1])
      print(path)
      return res
  


def main():
  maze = [
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
      [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
      [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  ]

  start = (1, 1)  # Starting point (row, column)
  end = (8, 1)    # Ending point (row, column)

  s = Solution()

  print(s.path_maze(maze, start, end))

main()