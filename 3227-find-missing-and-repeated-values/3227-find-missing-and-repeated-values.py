class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_sum = n * n * (n * n + 1) // 2
        actual_sum = 0
        seen = set()
        duplicate = 0
        
        for row in grid:
            for num in row:
                actual_sum += num
                if num in seen:
                    duplicate = num
                else:
                    seen.add(num)
        
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]