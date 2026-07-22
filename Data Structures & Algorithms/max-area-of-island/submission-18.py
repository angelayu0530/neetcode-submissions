class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curr_area = 0
        max_area = 0
        cols = len(grid[0])
        rows = len(grid)
        to_visit = []
        seen = set()
        changes = [(0,1), (1,0),(-1,0), (0,-1)]

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == 1:
                    curr_area = 1
                    seen.add((row,col))
                    to_visit.append((row,col))
                    while to_visit:
                        pop_row, pop_col = to_visit.pop()
                        for x , y in changes:
                            curr_row = pop_row + x
                            curr_col = pop_col + y
                            if 0 <= curr_row < rows and 0 <= curr_col < cols and (curr_row,curr_col) not in seen and grid[curr_row][curr_col] == 1:
                                    curr_area += 1
                                    seen.add((curr_row,curr_col))
                                    to_visit.append((curr_row,curr_col))
                max_area = max(max_area, curr_area)
        return max_area