class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = nums1 + nums2
        arr.sort()
        leng = len(arr)
        # print(arr)
        # print(leng)
        if leng % 2 == 0:
            return (arr[leng / 2 - 1] + arr[leng / 2]) / 2.0
        else:
            return arr[leng/ 2]
        