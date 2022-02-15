"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs)
        max_str = max(strs)

        result = min_str

        if min_str != max_str:
            result = ""
            max_index = 0

            while max_index < len(min_str):
                if min_str[max_index] == max_str[max_index]:
                    result += min_str[max_index]
                else:
                    break
                max_index += 1

            if result != "":
                for word in strs:
                    if not word.startswith(result):
                        break

        return result


s = Solution()
a = s.longestCommonPrefix(strs=["flower", "flow", "flight"])
print(a)
print(a == "fl")

a = s.longestCommonPrefix(strs=["dog", "racecar", "car"])
print(a)
print(a == "")
