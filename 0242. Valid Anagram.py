class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        for c in s:
            if c not in hs.keys():
                hs[c] = 0
            hs[c] += 1
        for c in t:
            if c not in hs.keys():
                return False
            hs[c] -= 1
        for k, v in hs.items():
            if v != 0:
                return False
        return True