class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        temps = []

        for i in range(len(temperatures)):
            while temps and temps[-1][0] < temperatures[i]:
                t, j = temps.pop()
                res[j] = i - j
            temps.append((temperatures[i], i))


        return res
        