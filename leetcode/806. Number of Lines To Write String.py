from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 0
        last_line_pixel = 0

        for l in s:
            pixel = widths[ord(l) - 97]
            last_line_pixel += pixel

            if last_line_pixel > 100:
                last_line_pixel = pixel
                line += 1

        return [line + 1, last_line_pixel]


s = Solution()
a = s.numberOfLines(
    widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="abcdefghijklmnopqrstuvwxyz")
print(a)
print(a == [3, 60])

a = s.numberOfLines(
    widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="bbbcccdddaaa")
print(a)
print(a == [2, 4])
