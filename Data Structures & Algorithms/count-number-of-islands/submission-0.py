class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: 
            return 0

        visited = set() 

        rows, columns = len(grid), len(grid[0])

        island_count = 0 

        def dfs(r, c):

            if (r,c) in visited: 
                return

            if (r < 0 or r >= rows or 
                c < 0 or c >= columns or 
                grid[r][c] == '0' or 
                (r,c) in visited): 
                return 
        
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(rows): 
            for j in range(columns): 
                if grid[i][j] == "1" and (i, j) not in visited: 
                    island_count += 1 
                    dfs(i, j)
        
        return island_count 

    



        




        