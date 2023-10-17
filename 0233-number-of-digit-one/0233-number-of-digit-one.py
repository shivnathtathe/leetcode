class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        count = 0
        factor = 1
        while factor <= n:
            divider = factor * 10
            count += (n // divider) * factor + min(max(n % divider - factor + 1, 0), factor)
            factor *= 10
        return count

                