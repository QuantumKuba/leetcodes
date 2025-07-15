from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])  # O(1) — just getting lengths

        seen = [[False] * n for _ in range(m)]  # O(m * n) — this is where most of our space goes

        dirx = [-1, 0, 1, 0]
        diry = [0, 1, 0, -1]

        queue = deque()

        for i in range(m):              # Outer loop over rows → O(m)
            for j in range(n):          # Inner loop over columns → O(n)
                if grid[i][j] == '1' and not seen[i][j]:  # O(1)
                    seen[i][j] = True   # Mark as visited
                    queue.append((i, j))# Add to queue
                    islands += 1        # One island found!

                    while queue:        # This runs once per cell in the island
                        x, y = queue.popleft()  # O(1) pop from front

                        for d in range(4):       # 4 directions → O(4) = O(1)
                            nx = x + dirx[d]
                            ny = y + diry[d]

                            if 0 <= nx < m and 0 <= ny < n:  # Bounds check
                                if grid[nx][ny] == '1' and not seen[nx][ny]:
                                    seen[nx][ny] = True      # Mark as visited
                                    queue.append((nx, ny))   # Enqueue new land

        return islands




if __name__ == "__main__":
    s = Solution()
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]

    s.numIslands(grid=grid)