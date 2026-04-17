class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        time = 0
        while queue:
            changed = False
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1:
                        fresh -= 1
                        changed = True
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
            if changed:
                time += 1
        if not fresh:
            return(time)
        else:
             return(-1)
            
        