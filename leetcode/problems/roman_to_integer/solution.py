class Solution:
    def romanToInt(self, s: str) -> int:
        sv = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        
        result = 0
        
        for i in range(len(s)):
            result = result - sv[s[i]] if i + 1 < len(s) and sv[s[i]] < sv[s[i+1]] else result + sv[s[i]]
        
        return result