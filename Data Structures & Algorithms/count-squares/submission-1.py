class CountSquares:

    def __init__(self):
        self.squares = defaultdict(int)
        self.keys = set()
        

    def add(self, point: List[int]) -> None:
        self.squares[tuple(point)] += 1
        self.keys.add(tuple(point))
        

    def count(self, point: List[int]) -> int:
        total = 0
        x, y = point
        # x1, y1, x, y
        #. 1  2 2, 1

        for x1, y1 in self.keys:
            diffX, diffY = abs(x1 - x), abs(y1 - y)
            if diffX == diffY and (diffX != 0 and diffY != 0):
                total += self.squares[(x1, y1)] * self.squares[(x1, y)] * self.squares[(x, y1)]


        return total
        
