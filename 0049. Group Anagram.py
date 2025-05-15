## Original Solotion

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer = []
        l = []
        seen = []
        for s in strs:
            h = {}
            for c in s:
                if c not in h.keys():
                    h[c] = 0
                h[c] += 1
            l.append(h.copy())
            h.clear()
        for i, c in enumerate(l):
            if c in seen:
                answer[seen.index(c)].append(strs[i])
            else:
                answer.append([strs[i]])
                seen.append(c)
        return answer

## Optimized Solution


    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in h.keys:
                h[tuple(count)] = []
            h[tuple(count)].append(s)
        return list(h.values)

