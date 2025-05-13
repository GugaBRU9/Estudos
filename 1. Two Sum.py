class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, c in enumerate(nums):
            if c in h.keys() :
                return [i, h[c]]
            h[target - c] = i