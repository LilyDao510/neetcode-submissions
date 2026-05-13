class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = defaultdict(list)
        for s in strs:
            new_s = tuple(sorted(s))
            new_strs[new_s].append(s)
        return list(new_strs.values())
































# cach 1:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())



        