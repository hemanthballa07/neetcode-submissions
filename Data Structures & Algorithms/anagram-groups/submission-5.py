class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for str in strs:
            s = [0]*26
            for ch in str:
                s[ord(ch)-97]+=1
            d[tuple(s)].append(str)
        return(list(d.values()))
        