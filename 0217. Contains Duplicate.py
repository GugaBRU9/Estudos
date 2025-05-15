class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for c in nums:
            if c in seen:
                return True
            else:
                seen.add(c)
        return False