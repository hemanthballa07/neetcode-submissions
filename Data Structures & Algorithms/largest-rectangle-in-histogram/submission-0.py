class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_rec = 0
        heights.append(0)
        for i,h in enumerate(heights):
            while st and heights[st[-1]] > h:     
                hei = heights[st.pop()]
                prev = st[-1] if st else -1
                w = i - prev - 1
                max_rec = max(max_rec, hei*w)
            st.append(i)
        return(max_rec)
        