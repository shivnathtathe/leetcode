class Solution:
    def romanToInt(self, s: str) -> int:
        dict_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        whole_sum = 0
        prev_value = 0

        for letter in s[::-1]:
            if dict_map[letter] < prev_value:
                whole_sum -= dict_map[letter]
            else:
                whole_sum += dict_map[letter]
            prev_value = dict_map[letter]

        return whole_sum
