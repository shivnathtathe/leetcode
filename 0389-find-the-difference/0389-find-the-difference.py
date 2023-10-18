class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def find_added_letter(s, t):
            s_count = {}
            t_count = {}
            
            for char in s:
                s_count[char] = s_count.get(char, 0) + 1
            
            for char in t:
                t_count[char] = t_count.get(char, 0) + 1
            
            for char, count in t_count.items():
                if count != s_count.get(char, 0):
                    return char
            
            return list(t_count.keys())[0]

        return find_added_letter(s, t)