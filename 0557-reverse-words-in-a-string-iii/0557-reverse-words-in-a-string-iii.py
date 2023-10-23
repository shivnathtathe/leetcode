class Solution:
    def reverseWords(self, s: str) -> str:
        # new_list = s.split(' ')
        rev_list = [x[::-1] for x  in s.split(' ')]
        return ' '.join(rev_list)