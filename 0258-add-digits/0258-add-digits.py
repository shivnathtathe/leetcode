class Solution:
    def addDigits(self, num: int) -> int:
        result = 0
        the_num =str(num)
        if len(the_num) == 1:
            return int(the_num)
        for i in the_num:
            result += int(i)
        return self.addDigits(result)
        
            