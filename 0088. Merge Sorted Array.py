class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
        if m == p1:
            nums.extend(nums2[p2:n])
        else:
            nums.extend(nums1[p1:m])
        for i in range(m+n):
            nums1[i] = nums[i]


sol = Solution()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)