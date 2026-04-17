class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_st = 0
        left = 0
        n = len(s)
        u = set()
        for right in range(n):
            while s[right] in u:
                
                u.remove(s[left])
                left+=1

            u.add(s[right])
            max_st = max(max_st,len(u))
        print(u)
        return(max_st)

        