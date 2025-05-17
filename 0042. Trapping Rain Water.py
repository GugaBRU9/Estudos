# This was the first solution but it was too slow

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l, r = 0, len(height) - 1
#         a = [0] * len(height)
#         while r > l:
#             b = min(height[l], height[r])
#             for i in range(l, r + 1):
#                 if b - height[i] > 0:
#                     a[i] = max(a[i], b - height[i])
#             if height[l] > height[r]:
#                 r -= 1
#             else:
#                 l += 1
#         return sum(a)

# Second and optimal solution
class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        tot = 0
        max_l, max_r = 0, 0
        while r > l:
            if max_l < height[l]:
                max_l = height[l]
            else:
                tot += max_l - height[l]
            if max_r < height[r]:
                max_r = height[r]
            else:
                tot += max_r - height[r]
            if height[l] > height[r]:

                r -= 1
            else:
                l += 1
        return tot

