class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        posCounter = 0
        negCounter = 0
        for num in nums:
            if num > 0:
                posCounter += 1
            elif num < 0:
                negCounter += 1
        return max(posCounter, negCounter)