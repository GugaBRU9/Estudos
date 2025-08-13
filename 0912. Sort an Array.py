class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1,l2):
            p1, p2 = 0, 0
            merged = []
            while p1 < len(l1) and p2 < len(l2):
                if l1[p1] > l2[p2]:
                    merged.append(l2[p2])
                    p2 += 1
                else:
                    merged.append(l1[p1])
                    p1 += 1
            if p1 == len(l1):
                merged.extend(l2[p2:])
            else:
                merged.extend(l1[p1:])
            return merged


        def sort(arr):
            if len(arr) < 2:
                return arr
            else:
                m = len(arr) // 2
                arr1 = sort(arr[:m])
                arr2 = sort(arr[m:])
                return merge(arr1, arr2)
        return sort(nums)