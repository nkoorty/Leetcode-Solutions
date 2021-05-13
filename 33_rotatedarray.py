class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = len(nums)-1
        while i >= 0:
            if nums[i] == target:
                return i
            else:
                i-=1
        return -1
