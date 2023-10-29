class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0

        for i in range(len(mat)):
           
            result += mat[i][i]
          
            result += mat[len(mat) - 1 - i][i]
      
        if len(mat) % 2 != 0:
             result -= mat[len(mat) // 2][len(mat) // 2]
        
        return result