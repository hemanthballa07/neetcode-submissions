class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            c = ''.join(sorted(i))
            res[c].append(i)
        return list(res.values())

        