class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letter_count = s.count(letter)
        string_length = len(s)

        if letter_count == 0:
            return 0

        percentage = (letter_count / string_length) * 100
        return int(percentage)

        
        
            