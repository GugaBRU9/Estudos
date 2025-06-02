class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        if len(position) == 0:
            return 0
        res = len(position)
        for i in range(len(position)):
            for j in range(i + 1, len(speed)):
                s1 = position[i]
                s2 = position[j]
                v1 = speed[i]
                v2 = speed[j]
                try:
                    t = (s1 - s2) / (v2 - v1)
                except ZeroDivisionError:
                    t = float('-inf')
                s = s1 + v1 * t
                if t >= 0 and s <= target:
                    res -= 1
                    position[j] = s - min(v1, v2) * t
                    speed[j] = min(v1, v2)
                    break
        return res if res != 0 else 1



sol = Solution()
print(sol.carFleet(12, [4,0,5,3,1,2], [6,10,9,6,7,2]))
