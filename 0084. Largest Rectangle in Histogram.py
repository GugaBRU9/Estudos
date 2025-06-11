class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, h * w)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            w = len(heights) - stack[-1] - 1 if stack else len(heights)
            max_area = max(max_area, h * w)
        return max_area
sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))
