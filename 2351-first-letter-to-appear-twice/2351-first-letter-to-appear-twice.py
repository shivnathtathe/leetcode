class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []
        repeated = []
        index = 0

        for char in s:
            if char in seen:
                repeated.append(index)
            seen.append(char)
            index += 1

        min_val = min(repeated)
        return s[min_val]