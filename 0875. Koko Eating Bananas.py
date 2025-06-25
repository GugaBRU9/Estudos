import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r)//2
            s = 0
            for b in piles:
                s += math.ceil(b / m)
            if s > h:
                l = m + 1
            else:
                r = m - 1
        return l