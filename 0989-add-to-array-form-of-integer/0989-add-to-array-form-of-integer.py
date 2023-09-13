class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        result = []

        for digit in reversed(num):
            total = digit + k % 10 + carry
            carry = total // 10
            result.append(total % 10)
            k //= 10

        while k > 0:
            total = k % 10 + carry
            carry = total // 10
            result.append(total % 10)
            k //= 10

        if carry > 0:
            result.append(carry)

        return result[::-1]