class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        lr, rr =  0, len(matrix) - 1
        while lr <= rr:
            mr = (lr + rr) // 2
            lc, rc = 0, len(matrix[mr]) - 1
            while lc <= rc:
                mc = (lc + rc) // 2
                if matrix[mr][mc] > target:
                    rc = mc - 1
                elif matrix[mr][mc] < target:
                    lc = mc + 1
                else:
                    return True
            if matrix[mr][mc] > target:
                rr = mr - 1
            elif matrix[mr][mc] < target:
                lr = mr + 1
            else:
                return True
        return False

sol = Solution()
print(sol.searchMatrix([[1],[3]], 3))