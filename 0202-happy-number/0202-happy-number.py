class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_next(n):
            result = 0
            while n > 0:
                digit = n % 10
                result += digit * digit
                n //= 10
            return result
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = calculate_next(n)
        return n == 1
