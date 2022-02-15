class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        elif t == "":
            return False

        result = ""
        t_len = len(t)
        t_index = 0

        for l_s in s:
            find = False
            while t_index < t_len:
                if t[t_index] == l_s:
                    result += l_s
                    find = True
                    t_index += 1
                    break

                t_index += 1

            if not find:
                break

        return s == result