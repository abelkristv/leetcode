class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        gridAll = [ y for x in grid for y in x]
        gridAll.sort()

        hashDict = {}

        duplicate = 0
        missing = 0

        print(gridAll)

        for index, item in enumerate(gridAll): 
            # print(item)
            if gridAll[index] == gridAll[index - 1] + 2:
                missing = gridAll[index - 1] + 1
            if item in hashDict:
                duplicate = item
                continue
            hashDict[item] = 1
        print(missing)
        if missing == 0:
            missing = gridAll[len(gridAll) - 1] + 1
        if gridAll[0] > 1:
            missing = 1

        return [duplicate, missing]
        