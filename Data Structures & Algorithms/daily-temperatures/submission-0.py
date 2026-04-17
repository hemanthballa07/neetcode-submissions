class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #maintain a decreasing stack
        #so when we are popping elements for stack we know that's the next available warmer day
        #also append the index with the value 
        st = []
        n = len(temperatures)
        res = [0]*n
        for i in range(n):
            temp,idx = temperatures[i],i
            if not st or (st and st[-1][0]>temp):
                st.append([temp,idx])
                continue
            while st and st[-1][0] < temp:
                t,x = st.pop()
                res[x] = i - x
            st.append([temp,idx])
        return(res)

        
            


        