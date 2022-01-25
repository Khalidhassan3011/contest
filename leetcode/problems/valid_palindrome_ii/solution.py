class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        left_start = 0
        right_start = len(s) - 1

        while left_start < right_start:
            if s[left_start] != s[right_start]:
                remove_left = list(s)
                remove_right = list(s)

                remove_left.pop(left_start)
                remove_right.pop(right_start)

                if remove_left == remove_left[::-1] or remove_right == remove_right[::-1]:
                    return True

                return False

            left_start += 1
            right_start -= 1