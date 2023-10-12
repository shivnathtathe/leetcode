class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table ={}
        for i in s:
            if i in hash_table:
                hash_table[i]+=1
            else:
                hash_table[i]=1
        for j in s:
            if hash_table[j] == 1:
                return s.index(j)
        return -1