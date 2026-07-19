class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        movements = [(0,1),(1,0), (-1,0), (0,-1)]
        to_visit = []
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        island = 0

        for curr_row in range(rows):
            for curr_col in range(cols):
                if (curr_row, curr_col) not in seen and grid[curr_row][curr_col] == "1":
                    seen.add((curr_row, curr_col))
                    to_visit.append((curr_row, curr_col))
                    while len(to_visit):
                        visit_row, visit_col = to_visit.pop()
                        for x, y in movements:
                            curr_visit_row = visit_row + x
                            curr_visit_col = visit_col + y
                            if (0 <= curr_visit_row < rows and 0 <= curr_visit_col < cols and (curr_visit_row, curr_visit_col) not in seen and grid[curr_visit_row][curr_visit_col] == "1"):
                                seen.add((curr_visit_row, curr_visit_col))
                                to_visit.append((curr_visit_row, curr_visit_col))
                    island += 1
        return island