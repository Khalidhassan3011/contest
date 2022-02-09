class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_positions = [i for i, letter in enumerate(s) if letter == c]
        s_len = len(s)
        c_positions_len = len(c_positions)

        result = []

        for i in range(s_len):
            result.append(min([abs(c_positions[j] - i) for j in range(c_positions_len)]))

        return result