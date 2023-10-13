class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        result = ""
        values = sorted(roman_numerals.keys(), reverse=True)

        for value in values:
            while num >= value:
                result += roman_numerals[value]
                num -= value

        return result