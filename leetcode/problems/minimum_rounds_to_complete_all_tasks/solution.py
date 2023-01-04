class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        r = 0
        for k, v in freq.items():
            if v == 1:
                return -1 
            else:
                r += (v + 2) // 3

        return r


