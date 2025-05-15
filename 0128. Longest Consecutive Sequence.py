class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        k = set(nums)
        maior = 0
        for c in k:
            if c - 1 not in k:
                count = 0
                prox = c
                while prox in k:
                    count += 1
                    prox += 1
                if count > maior:
                    maior = count
        return maior

sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))