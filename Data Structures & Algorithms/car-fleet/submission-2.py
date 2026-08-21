class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p,s in zip(position, speed)])
        rates = [(target - p) /s for p, s in cars]
        res = [rates[len(rates) - 1]]

        for i in range(len(rates) - 2, -1, -1):
            if res[-1] < rates[i]:
                res.append(rates[i])



        return len(res)