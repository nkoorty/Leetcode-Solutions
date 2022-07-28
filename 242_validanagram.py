class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # O(n) runtime, better than sorting since that uses O(nlogn)