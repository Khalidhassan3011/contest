class Solution:
    def min(self, a: int, b: int) -> int:
        return a if a <= b else b
    
    def max(self, a: int, b: int) -> int:
        return a if a >= b else b
    
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(area, result)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result
        