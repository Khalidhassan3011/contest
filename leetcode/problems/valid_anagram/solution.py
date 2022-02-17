class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
#         count_s = defaultdict(int)
#         count_t = defaultdict(int)

#         for l in s:
#             count_s[l] += 1

#         for l in t:
#             count_t[l] += 1

#         return count_s == count_t