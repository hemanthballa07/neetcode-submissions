class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2**31 - 1
        row = len(grid)
        col = len(grid[0])
        # visited = [[False]*col for _ in range(row)]
        #shortest path from source to all nodes 
        def bfs(i,j):
            dist = 0
            queue = deque([(i,j,dist)])
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            while queue:
                x,y,dist = queue.popleft()
                grid[x][y] = min(dist,grid[x][y])
                # if visited[x][y]:
                #     continue
                # visited[x][y] = True
                for dr,dc in directions:
                    nr,nc = x+dr,y+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] > dist+1:
                        queue.append((nr,nc,dist+1))



        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    bfs(i,j)