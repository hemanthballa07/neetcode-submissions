class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = left + (right - left) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            if total_time <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


        