class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums) / 2
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        
        for num in hashmap.values():
            if num % 2 != 0:
                return False

        return True

        