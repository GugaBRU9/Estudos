class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[m] and nums[m] > nums[r]:
                l = m
            elif nums[l] > nums[m]:
                r = m
            else:
                return nums[r] if nums[r] < nums[l] else nums[l]

