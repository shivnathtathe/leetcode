class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle the sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return ''.join(result)

        result.append(".")

        # Use a dictionary to store the index of the first occurrence of each remainder
        seen = {}

        recurring_part = []

        while remainder != 0:
            if remainder in seen:
                index = seen[remainder]
                result.insert(index, "(")
                result.append(")")
                result += recurring_part
                break

            seen[remainder] = len(result)
            numerator, remainder = divmod(remainder * 10, denominator)
            result.append(str(numerator))

        return ''.join(result)

