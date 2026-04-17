class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_of_islands = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False]*col for _ in range(row)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j):
            visited[i][j]= True
            for dr,dc in directions:
                nr,nc = i+dr,j+dc
                if 0<=nr<row and 0<=nc<col and grid[nr][nc] == "1" and not visited[nr][nc]:
                    dfs(nr,nc)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    no_of_islands += 1
        return(no_of_islands)

        