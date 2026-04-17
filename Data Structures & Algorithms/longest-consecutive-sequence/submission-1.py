from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #if it was sequence i.e. ordering was important
        # ans = 0
        # d = defaultdict(int)
        # for num in nums:
        #     d[num]=d[num-1] + 1
        #     ans = max(ans, d[num])
        # return ans      

        visited = {}
        nums_set = set(nums)
        ans = 0
        for num in nums:
            length = 0
            curr_num = num
            while (num in nums_set) and (num not in visited):
                length+=1
                num +=1
            if num in visited:
                length += visited[num]
            visited[curr_num] = length
            ans = max(ans, length)
        return ans

            


        
        # nums = set(nums)
        # longest = 0
        # for num in nums:
        #     if (num-1) not in nums:
        #         length = 1
        #         while (num+length) in nums:
        #             length += 1
        #         longest = max(length,longest)
        # return longest
            


        