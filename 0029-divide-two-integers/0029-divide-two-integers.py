class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            dividend +=1
            result = dividend/divisor
            new_result = str(result).split('.')
            return int(new_result[0])
        else:
            result = dividend/divisor
            new_result = str(result).split('.')
            return int(new_result[0])