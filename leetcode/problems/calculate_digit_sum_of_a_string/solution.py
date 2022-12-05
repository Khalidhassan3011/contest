class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            steps = ""
            for item in [s[i:i+k] for i in range(0, len(s), k)] :
                sum = 0
                for charecter in item:
                    sum += int(charecter)
                steps += str(sum)
            
            s = steps

        return s
                