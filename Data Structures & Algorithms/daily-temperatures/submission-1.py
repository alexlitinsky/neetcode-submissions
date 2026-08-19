class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        st = []

        for i, t in enumerate(temperatures):
            while st and st[-1][0] < t:
                v, j = st.pop()
                res[j] = i - j
            st.append([t, i])


        return res
        