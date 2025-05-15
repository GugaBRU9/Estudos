class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = {}
        t = {}
        top = []
        for c in nums:
            if c not in t.keys():
                t[c] = 0
            t[c] += 1
        for j,v in t.items():
            if v not in h.keys():
                h[v] = []
            h[v].append(j)
        for c in range(len(h)):
            top.extend(h[max(h.keys())])
            h.pop(max(h.keys()))
        return top[:k]


sol = Solution()
print(sol.topKFrequent(nums= [1,1,1,2,2,3], k=2))


