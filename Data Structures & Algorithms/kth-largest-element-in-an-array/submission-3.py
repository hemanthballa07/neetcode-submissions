import random
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quick_select(l,r):
            pivot_index = random.randint(l,r)
            pivot = nums[pivot_index]
            nums[pivot_index],nums[r] = nums[r],nums[pivot_index]
            p = l

            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r] = nums[r],nums[p]

            if p > k:
                return quick_select(l,p-1)
            elif p < k:
                return quick_select(p+1,r)
            else:
                return nums[p]
        
        return quick_select(0, len(nums)-1)





        