class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s = {}
        freq_t = {}

        for c in s:
            freq_s[c] = freq_s.get(c, 0) + 1
        
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1

        for i in freq_t:
            if i not in freq_s or freq_s[i] != freq_t[i]:
                return i