'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk
where k >= 109, and you want to check one by one to see if t has its subsequence.
In this scenario, how would you change your code?
'''


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


s = Solution()
a = s.isSubsequence(s="abc", t="ahbgdc")
print(a)
print(a == True)

a = s.isSubsequence(s="axc", t="ahbgdc")
print(a)
print(a == False)

a = s.isSubsequence(s="ab", t="baab")
print(a)
print(a == True)

a = s.isSubsequence(s="bab", t="baab")
print(a)
print(a == True)

a = s.isSubsequence(s="aab", t="baab")
print(a)
print(a == True)

a = s.isSubsequence(s="", t="baab")
print(a)
print(a == True)
