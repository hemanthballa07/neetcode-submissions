import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        return [keys for keys,_ in d.most_common(k)]