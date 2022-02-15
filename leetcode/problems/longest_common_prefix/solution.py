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