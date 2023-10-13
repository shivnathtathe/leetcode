class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman_numeral = ""
        i = 0

        while num > 0:
            while num >= values[i]:
                roman_numeral += symbols[i]
                num -= values[i]
            i += 1

        return roman_numeral
