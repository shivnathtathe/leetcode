class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for sentence in sentences:
            words = sentence.split()
            word_count = len(words)
            if word_count > max_count:
                max_count = word_count
        return max_count
