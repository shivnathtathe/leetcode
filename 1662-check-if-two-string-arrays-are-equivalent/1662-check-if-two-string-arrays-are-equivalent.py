class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new_string1 =''.join(word1)
        new_string2 =''.join(word2) 
        
        if new_string1 == new_string2:
            return True
        return False