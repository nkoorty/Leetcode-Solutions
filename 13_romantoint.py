class Solution:
    def romanToInt(self, s: str) -> int:
        convert = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500, 'M':1000}
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and convert[s[i]] < convert[s[i+1]]:
                total -= convert[s[i]]
            else:
                total += convert[s[i]]
        return total
    
        