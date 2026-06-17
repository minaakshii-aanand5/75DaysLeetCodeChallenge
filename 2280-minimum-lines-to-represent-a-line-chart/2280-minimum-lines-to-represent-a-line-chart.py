from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:

        n = len(stockPrices)

        if n <= 1:
            return 0

        stockPrices.sort()

        lines = 1

        x1, y1 = stockPrices[0]
        x2, y2 = stockPrices[1]

        prev_dy = y2 - y1
        prev_dx = x2 - x1

        for i in range(2, n):

            x3, y3 = stockPrices[i]

            dy = y3 - y2
            dx = x3 - x2

            if prev_dy * dx != dy * prev_dx:
                lines += 1

            prev_dy = dy
            prev_dx = dx

            x2, y2 = x3, y3

        return lines
        