class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        for c in range(len(nums) - 2):
            if nums[c] > 0:
                break
            if c == 0 or (c != 0 and nums[c] != nums[c - 1]):
                l, r = c + 1, len(nums) - 1
                while r > l:
                    s = nums[c] + nums[l] + nums[r]
                    if s == 0:
                        answer.append([nums[c], nums[l], nums[r]])
                        while l < r and nums[r] == nums[r -1]:
                            r -= 1
                        while r > l and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                        r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1
        return answer



sol = Solution()
print(sol.threeSum([0,0,0]))
