class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        c = Counter(nums1)
        output = []
        for n in nums2:
            if c[n] > 0:
                output.append(n)
                c[n] -= 1
        return output
        """
        # Time O(n) but space O(n) as well
        i, j = 0, 0
        output = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        while i<len(nums1) and j<len(nums2):
            if nums1[i] > nums2[j]:
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                output.append(nums1[i])
                i+=1
                j+=1
        return output
                
        # Time O(nlogn) due to sort, space O(n) due to output list