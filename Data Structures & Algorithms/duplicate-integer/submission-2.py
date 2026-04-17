class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            if num not in d:
                d[num]+=1
            else:
                return True
        return False
        