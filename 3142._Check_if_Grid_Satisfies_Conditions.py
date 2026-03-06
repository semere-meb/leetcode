class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        i = 0
        while i < len(grid) - 1:
            if grid[i] != grid[i+1]:
                return False
            i += 1
        i = 0
        while i < len(grid[0]) - 1:
            if grid[0][i] == grid[0][i+1]:
                return False
            i += 1
        return True


if __name__ == "__main__":
    Solution().satisfiesConditions([[1,0,2],[1,0,2]])
    Solution().satisfiesConditions([[1,1,1],[0,0,0]])
    Solution().satisfiesConditions([[1],[2],[3]])
