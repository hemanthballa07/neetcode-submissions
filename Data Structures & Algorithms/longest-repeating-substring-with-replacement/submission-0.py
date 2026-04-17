class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        left = 0
        n = len(s)
        res = 0
        for right in range(n):
            d[s[right]]+=1
            
            if right - left + 1 - max(d.values()) > k:
                d[s[left]]-=1
                left+=1

            res = max(res,right-left+1)
        return(res)
            
            

        