class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []
        atlantic = []
        row = len(heights)
        col = len(heights[0])
        pacific_visited = [[False]*col for _ in range(row)]
        atlantic_visited = [[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0:
                    pacific.append([i,j])
                    pacific_visited[i][j] = True
                if i == row - 1 or j == col - 1:
                    atlantic.append([i,j])
                    atlantic_visited[i][j] = True
        pacific_queue = deque(pacific)
        atl_queue = deque(atlantic)
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while pacific_queue:
            i,j = pacific_queue.popleft()
            for dr,dc in directions:
                nr,nc = i+dr,j+dc
                if 0<=nr<row and 0<=nc<col and heights[nr][nc]>=heights[i][j] and not pacific_visited[nr][nc]:
                    pacific_visited[nr][nc]= True
                    pacific_queue.append([nr,nc])
                    pacific.append([nr,nc])
        while atl_queue:
            i,j = atl_queue.popleft()
            for dr,dc in directions:
                nr,nc = i+dr,j+dc
                if 0<=nr<row and 0<=nc<col and heights[nr][nc]>=heights[i][j] and not atlantic_visited[nr][nc]:
                    atlantic_visited[nr][nc]= True
                    atl_queue.append([nr,nc])
                    atlantic.append([nr,nc])
        res = []
        for i in range(row):
            for j in range(col):
                if atlantic_visited[i][j] and pacific_visited[i][j]:
                    res.append([i,j])
        return(res)
        



        