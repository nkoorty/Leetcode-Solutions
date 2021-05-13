class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = ""
        ans = 0
        for i in s:
            if i not in string:
                string += i
                ans = max(ans,len(string))
            else:
                slice = string.index(i)
                string = string[slice+1:]+i
        return ans
