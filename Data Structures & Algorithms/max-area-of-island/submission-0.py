class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False]*col for _ in range(row)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j):
            visited[i][j]= True
            area = 1
            for dr,dc in directions:
                nr,nc = i+dr,j+dc
                if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1 and not visited[nr][nc]:
                    area+=dfs(nr,nc)
            return(area)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = dfs(i,j)
                    max_area = max(area, max_area)
        return(max_area)

        