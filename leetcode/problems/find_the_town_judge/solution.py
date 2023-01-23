class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0: return 1
        freq = {}
        for item in trust:
            freq[item[0]] = freq.get(item[0], 0) - 1
            freq[item[1]] = freq.get(item[1], 0) + 1

        for item in freq:
            if freq[item] == n - 1:
                return item

        return -1