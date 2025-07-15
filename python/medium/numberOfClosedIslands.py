from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # columns
        visit = [[False] * n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                # ==== conditions to increment count ====
                # 1. If grid is land "0"
                # 2. If land if grid has not been seen yet
                # 3. If bfs returns true (checks wether its closed or at a border)

                if grid[i][j] == 0 and not visit[i][j] and self.bfs(i,j,m,n,grid,visit):
                    count += 1


        return count

    def bfs(self, x: int, y:int, m:int, n:int, grid: List[List[int]], visit:List[List[bool]]) -> bool:
        q = deque([(x,y)]) 
        visit[x][y] = True
        is_closed = True


        dirx = [0,1,0,-1]
        diry = [-1,0,1,0]

        while q:
            x, y = q.popleft()

            for i in range(4):
                r, c = x + dirx[i], y + diry[i]
                if r < 0 or r >= m or c < 0 or c >= n:
                    # x, y is a boundary cell
                    is_closed = False
                elif grid[r][c] == 0 and not visit[r][c]:
                    q.append((r,c))
                    visit[r][c] = True

        return is_closed
    

if __name__ == "__main__":
    s = Solution()
    print(s.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
    # print(s.closedIsland([[1,1,1,1,0,1,1,1],[1,0,0,0,0,1,0,1],[1,0,1,0,0,0,0,1],[1,0,0,0,1,0,1,1],[1,1,1,1,1,1,1,1]]))  # Example usage
    # print(s.closedIsland([[0]]))  # Example usage
    # print(s.closedIsland([[0], [0]]))  # Example usage