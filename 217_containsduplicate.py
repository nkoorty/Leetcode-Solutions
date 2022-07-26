class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        return True if len(set(nums)) != len(nums) else False has time complexity O(n^2) but space complexity O(1)
        """
        
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    # This solution has time complexity O(n) and space complexity O(n)
    