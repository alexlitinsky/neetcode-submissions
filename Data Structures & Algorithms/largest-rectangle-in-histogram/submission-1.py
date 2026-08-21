class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, st = max(heights), []

        for i, h in enumerate(heights):
            start_index = i
            while st and st[-1][1] > h:
                j, height = st.pop()
                res = max(res, height * (i - j))
                start_index = j
            st.append([start_index, h])
        
        for i, h in st:
            res = max(res, h * (len(heights) - i))

        return res
        