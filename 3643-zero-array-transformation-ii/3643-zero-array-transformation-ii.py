class Solution:
    def createDifferenceArray(self, nums):
        numLen = len(nums)
        diff = [0] * (numLen + 1)
        diff[0] = nums[0]
        for i in range(1, numLen):
            diff[i] = nums[i] - nums[i-1]
        return diff


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        count = 0
        numLen = len(nums)
        for num in nums:
            if num > 0:
                break
        else:
            return 0
        
        diff = self.createDifferenceArray(nums)

        cumFuckDetector = 0

        for query in queries:
            left_limit = query[0]
            right_limit = query[1]
            maxOps = query[2]

            if right_limit < cumFuckDetector - 88:
                continue

            # print("diffBefore : ", diff)            
            diff[left_limit] -= maxOps
            # if right_limit + 1 < numLen:
            diff[right_limit + 1] += maxOps

            # for i in range(left_limit, right_limit + 1):
            #     nums[i] -= maxOps
            #     if nums[i] < 0:
            #         nums[i] = 0
            count += 1
            # print("nums: ", nums)
            # print(diff)
            if diff[0] > 0:
                continue
            nonZeroFlag = False
            cummulative = diff[0]
            # diffCheck = diff[:]
            for i in range(1, numLen):
                cummulative = cummulative + diff[i]
                if cummulative > 0:
                    cumFuckDetector = i
                    nonZeroFlag = True
                    break 
            if nonZeroFlag == False:
                return count
                

        return -1