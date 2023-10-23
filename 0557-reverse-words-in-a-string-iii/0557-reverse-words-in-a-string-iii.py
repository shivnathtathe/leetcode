class Solution:
    def reverseWords(self, s: str) -> str:
        new_list = s.split(' ')
        rev_list = [x[::-1] for x  in new_list]
        return ' '.join(rev_list)