class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        big = 0
        while r > l:
            area = (r - l) * min(height[l], height[r])
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            if area > big:
                big = area
        return big

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

