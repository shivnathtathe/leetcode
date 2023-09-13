class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not all(bit in '01' for bit in a) or not all(bit in '01' for bit in b):
            raise ValueError("Input strings must contain only '0' and '1' characters.")

        num1 = int(a, 2)
        num2 = int(b, 2)

        sum_of = num1 + num2
        return bin(sum_of)[2:]