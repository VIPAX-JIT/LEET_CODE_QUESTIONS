class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        S = sum(sum(row) for row in grid)
        
        # Step 2: odd sum → impossible
        if S % 2 != 0:
            return False
        
        target = S // 2   # each half must equal this
        
        # Step 3a: horizontal cuts
        # move knife downward, row by row
        prefix = 0
        for i in range(m - 1):          # stop before last row (both sides must be non-empty)
            prefix += sum(grid[i])
            # print(f"After row {i}: prefix={prefix}, target={target}")
            if prefix == target:
                return True
        
        # Step 3b: vertical cuts
        # move knife rightward, col by col
        prefix = 0
        for j in range(n - 1):          # stop before last col
            prefix += sum(grid[i][j] for i in range(m))
            # print(f"After col {j}: prefix={prefix}, target={target}")
            if prefix == target:
                return True
        
        return False

            
