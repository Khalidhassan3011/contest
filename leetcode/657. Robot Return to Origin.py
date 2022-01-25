class Solution:
    def judgeCircle(self, moves: str) -> bool:
        forward, side = 0, 0
        for move in moves:
            if move == 'U':
                forward += 1
            elif move == 'D':
                forward -= 1
            elif move == 'L':
                side += 1
            elif move == 'R':
                side -= 1

        return forward == 0 and side == 0


s = Solution()
print(s.judgeCircle("UD"))
print(s.judgeCircle("LL"))
