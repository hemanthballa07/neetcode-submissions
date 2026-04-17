import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = defaultdict(int)
        t1 = defaultdict(int)
        for ch in s:
            s1[ch]+=1
        for ch in t:
            t1[ch]+=1
        return(s1==t1)
