class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        # find number of row
        rows = len(grid)

        #find number of cols
        cols = len(grid[0])

        #mark positions visited
        visit = set()

        #we want to count number of island
        islands = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = '0'
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or
                        nc >= cols or grid[nr][nc] == "0"
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"




        for r in range(rows):               #r will go through all rows
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands +=1
        return islands